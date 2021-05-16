import logging
import math
import base64
from elrondplayground.config.config import Config
from elrondplayground.util.util import Util

from erdpy.proxy.core import ElrondProxy
from erdpy.accounts import Address

class Core:
    _binance_wrapper = None
    _asset_wrapper = None
    _analyse_signal = None
    TRADED_TOKENS = None

    def __init__(self):
        logging.getLogger().setLevel(logging.INFO)

        # Initialise an instance of the Config class to run initialisation functions
        Config()

    def start(self):
        logging.info ("Starting!")

        proxy = ElrondProxy(Config.PROXY)

        account = proxy.get_account(Address(Config.ADDRESS))
        print(f"Account data {account}")


        

