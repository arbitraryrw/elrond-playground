import logging
import math
import base64
from elrondplayground.config.config import Config
from elrondplayground.util.util import Util

from erdpy.proxy.core import ElrondProxy
from erdpy.accounts import Address

class Core:

    def __init__(self):
        logging.getLogger().setLevel(logging.INFO)

        # Initialise an instance of the Config class to run initialisation functions
        Config()

    def start(self):
        logging.info ("Starting!")

        proxy = ElrondProxy(Config.PROXY)
        
        METACHAIN_ID = 4294967295

        shards = [METACHAIN_ID]

        num_shards = proxy.get_num_shards()
        # shards.extend([shard for shard in range(0, num_shards, 1)])

        for shard in shards:
            block_nonce = proxy.get_last_block_nonce(shard)
            hyperblock =  proxy.get_hyperblock(block_nonce)
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

                receiver_account = proxy.get_account(Address(tx.get('receiver')))
                receiver_balance = int(receiver_account.get('balance')) / int(math.pow(10, 18)), "EGLD"

                sender_account = proxy.get_account(Address(tx.get('sender')))
                sender_balance = int(sender_account.get('balance')) / int(math.pow(10, 18)), "EGLD"

                tx_value = int(tx.get('value')) / int(math.pow(10, 18)), "EGLD"

                print(f"\tAddress {receiver_account.get('address')} to {sender_account.get('address')} "
                    f"transaction of {tx_value}")
                print(f"\t\tReceiver account balance -> {receiver_balance}")
                print(f"\t\tSender account balance -> {sender_balance}")
