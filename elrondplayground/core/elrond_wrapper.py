from elrondplayground.config.config import Config

import math
from erdpy.proxy.core import ElrondProxy
from erdpy.accounts import Address


class ElrondWrapper:
    CLIENT = None

    def __init__(self):
        self.CLIENT = proxy = ElrondProxy(Config.PROXY)

    def get_account_data(self, address: str) -> dict():
        return self.CLIENT.get_account(Address(address))

    def get_account_transactions(self, address) -> dict():
        return self.CLIENT.get_account_transactions(Address(address))

    def get_num_shards(self) -> int:
        return self.CLIENT.get_num_shards()
    
    def get_last_block_nonce(self, shard_id: int = 4294967295) -> int:
        """
        Default to the metachain id 
        """
        return self.CLIENT.get_last_block_nonce(shard_id)

    def get_hyperblock(self, block_nonce: int) -> dict():
       return self.CLIENT.get_hyperblock(block_nonce)

    def decode_internal_int_value(self, int_value: int) -> int:
        try:
            return int(int_value) / int(math.pow(10, 18)), "EGLD"
        except ValueError as e:
            print(f"[ERROR] Could not decode {int_value} got error {e}")
            return int_value
        except Exception as e:
            print(f"[ERROR] Unknown error occured {e}")
            return int_value
