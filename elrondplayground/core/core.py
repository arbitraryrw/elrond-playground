import logging
from datetime import datetime
import time
import random
from elrondplayground.config.config import Config
from elrondplayground.core.elrond_wrapper import ElrondWrapper
from elrondplayground.util.util import Util


class Core:
    _ELROND_WRAPPER = None

    def __init__(self):
        logging.getLogger().setLevel(logging.INFO)

        # Initialise an instance of the Config class to run initialisation functions
        Config()

        self._ELROND_WRAPPER = ElrondWrapper()

    def start(self):
        self.query_account_data(Config.ADDRESS)

        start = datetime.now()

        for i in range(0,11,1):
            self.monitor_transactions()
            random_sleep_time = round(random.uniform(5,10), 1)
            time.sleep(random_sleep_time)

        print(f"Ran for {datetime.now()-start}")

    def query_account_data(self, address: str) -> None:
        account = self._ELROND_WRAPPER.get_account_data(address)
        print(f"Account data {account}")
        
        balance = self._ELROND_WRAPPER.decode_internal_int_value(account.get('balance'))
        print(balance)

        account_tx = self._ELROND_WRAPPER.get_account_transactions(address)
        print(f"Account has {len(account_tx)} transactions")

    def monitor_transactions(self) -> None:
        METACHAIN_ID = 4294967295
        shards = [METACHAIN_ID]
        # shards.extend([shard for shard in range(0, proxy.get_num_shards(), 1)])

        for shard in shards:
            block_nonce = self._ELROND_WRAPPER.get_last_block_nonce(shard)
            hyperblock =  self._ELROND_WRAPPER.get_hyperblock(block_nonce)
            # hyperblock =  proxy.get_hyperblock(4150000)  # test block
            # print(Util.pretty_format_json(hyperblock))
            print(f"Contains a total of {hyperblock.get('numTxs')} transactions")

            for tx in hyperblock.get('transactions', list()):
                if not tx.get('data'):
                    continue

                data_attribute = Util.base64_decode(tx.get('data'))

                if "delegate" == data_attribute:
                    print("[INFO] Raw delegate")
                elif "reDelegateRewards" == data_attribute:
                    print("[INFO] Re-invested staked gains")
                elif "claimRewards" == data_attribute:
                    print("[INFO] Took out staked gains")
                elif "withdraw" == data_attribute:
                    print("Withdaw! printing additional debug info")
                    print(tx)

                elif "@6f6b" == data_attribute or "relayedTx@" in data_attribute:
                    continue  # Ignore relayed transactions
                else:
                    print(f"Unknown tx type {data_attribute}")

                receiver_account = self._ELROND_WRAPPER.get_account_data(tx.get('receiver'))
                receiver_balance = self._ELROND_WRAPPER.decode_internal_int_value(receiver_account.get('balance'))

                sender_account = self._ELROND_WRAPPER.get_account_data(tx.get('sender'))
                sender_balance = self._ELROND_WRAPPER.decode_internal_int_value(sender_account.get('balance'))

                tx_value = self._ELROND_WRAPPER.decode_internal_int_value(tx.get('value'))

                print(f"\tAddress {receiver_account.get('address')} to {sender_account.get('address')} "
                    f"transaction of {tx_value}")
                print(f"\t\tReceiver account balance -> {receiver_balance}")
                print(f"\t\tSender account balance -> {sender_balance}")
