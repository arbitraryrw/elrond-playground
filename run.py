import os
import argparse
from elrondplayground.core.core import Core
from elrondplayground.config.config import Config

def handle_cli_arguments():
    parser = argparse.ArgumentParser(
        description='Sample project to demonstrate interacting with the Elrdon blockchain'
    )

    parser.add_argument(
        '-a',
        '--address', 
        type=str,
        required=False,
        help='The address to handle'
    )

    parser.add_argument(
        '-m', 
        '--monitor', 
        help='monitor transactions', 
        action = 'store_true'
    )

    args = parser.parse_args()

    Config.MONITOR_MODE = args.monitor

    if args.address is not None:
        Config.ADDRESS = args.address
        

def run():
    Config.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    print(Config.BANNER)

    c = Core()
    c.start()

if __name__ == '__main__':
    handle_cli_arguments()
    run()