import os
from elrondplayground.util.util import Util


class Config:
    ROOT_DIR=None
    CONFIG_FILE = None

    ADDRESS=None
    VERBOSE_MODE=None
    MONITOR_MODE=None

    VERSION = "0.1"
    BANNER = f"""

elrond-playground v{VERSION}
    """

    PROXY = "https://api.elrond.com"


    def __init__(self):
        if Config.ADDRESS is None:
            self.read_json_config()

    def __del__(self):
        pass

    def read_json_config(self):
        Config.CONFIG_FILE = os.path.join(self.ROOT_DIR, "elrondplayground/config/elrond_playground_config.json")
        deserialised_json_config = Util.deserialise_json_file(Config.CONFIG_FILE)

        Config.ADDRESS = deserialised_json_config.get('Address', None)

        if Config.ADDRESS is None:
            exit("ERROR - unable to get ADDRESS from config")
