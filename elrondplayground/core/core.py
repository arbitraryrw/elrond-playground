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
            print(Util.pretty_format_json(hyperblock))


