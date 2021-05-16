import os
from elrondplayground.core.core import Core
from elrondplayground.config.config import Config


def run():
    Config.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    print(Config.BANNER)

    c = Core()
    c.start()

if __name__ == '__main__':
    run()