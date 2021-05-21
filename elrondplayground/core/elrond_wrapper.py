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
