import logging

from freqtrade.commands import start_trading
from tests.conftest import get_args

logging.basicConfig(level=logging.DEBUG)
args = [
    'trade',
    '-c', "/Users/joehaddad/Desktop/trading/joe/freqtrade/user_data/dry_run_config.json",
    "--strategy", "DryRunSampleStrategy",
]
start_trading(get_args(args))