import os
import sys

# -----------------------------------------------------------------------------
import time
from datetime import datetime

this_folder = os.path.dirname(os.path.abspath(__file__))
root_folder = os.path.dirname(os.path.dirname(this_folder))
sys.path.append(root_folder + '/python')
sys.path.append(this_folder)

import ccxt  # noqa: E402

binance = ccxt.binance()
timeframe = '5m'


def print_chart(exchange, symbol, timeframe):
    start = time.time()
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=1000)
    stop = time.time()
    closing_time = datetime.utcfromtimestamp(ohlcv[-1][0]/1000).strftime('%Y-%m-%d %H:%M:%S')
    last_candle = datetime.utcfromtimestamp(ohlcv[-2][0]/1000).strftime('%Y-%m-%d %H:%M:%S')
    print(f"request @{datetime.utcnow()}: Downloading {symbol} finished in {stop - start} open time {closing_time} last_candle {last_candle}")
    return ohlcv


for symbol in ["BTC/USDT", "ETH/USDT", "BNB/USDT", "SAND/USDT", "MATIC/USDT", "LUNA/USDT", "FTM/USDT", "NEAR/USDT",
               "SOL/USDT", "DOT/USDT", "XRP/USDT", "GXS/USDT", "SHIB/USDT", "GALA/USDT", "AVAX/USDT", "ADA/USDT",
               "SUSHI/USDT", "ROSE/USDT", "CRV/USDT", "LINK/USDT", "DUSK/USDT", "FIL/USDT", "MANA/USDT", "DOGE/USDT",
               "VOXEL/USDT", "ATOM/USDT", "BTT/USDT", "ANT/USDT", "TRX/USDT", "USDC/USDT", "DYDX/USDT", "CTXC/USDT",
               "IOTA/USDT", "ALGO/USDT", "THETA/USDT", "LTC/USDT", "OOKI/USDT", "AAVE/USDT", "UNI/USDT", "VET/USDT",
               "OMG/USDT", "ICP/USDT", "EOS/USDT", "LINA/USDT", "CHR/USDT", "ALICE/USDT", "EGLD/USDT", "ALPACA/USDT",
               "QUICK/USDT", "AXS/USDT", "LPT/USDT", "LRC/USDT", "ZIL/USDT", "FARM/USDT", "ONE/USDT", "TUSD/USDT",
               "ENJ/USDT", "ZEC/USDT", "CHZ/USDT", "YFI/USDT", "GTC/USDT", "REQ/USDT", "GRT/USDT", "C98/USDT",
               "BICO/USDT", "MDT/USDT", "DREP/USDT", "KAVA/USDT", "1INCH/USDT", "ICX/USDT", "TLM/USDT", "DENT/USDT",
               "COS/USDT", "ETC/USDT", "PEOPLE/USDT", "SLP/USDT", "MBOX/USDT", "RUNE/USDT", "CAKE/USDT", "XTZ/USDT",
               "XLM/USDT", "ENS/USDT", "AUD/USDT", "CELR/USDT", "BAT/USDT", "BCH/USDT", "AR/USDT", "MASK/USDT",
               "JST/USDT", "FOR/USDT", "FTT/USDT", "MLN/USDT", "HOT/USDT", "NULS/USDT", "HNT/USDT", "COTI/USDT",
               "SNX/USDT", "SYS/USDT", "SFP/USDT", "RVN/USDT", "LTO/USDT", "SXP/USDT", "XMR/USDT", "IOTX/USDT",
               "DASH/USDT", "DAR/USDT", "WIN/USDT", "FLOW/USDT", "CVX/USDT", "COCOS/USDT", "BNX/USDT", "MINA/USDT",
               "HARD/USDT", "WAXP/USDT", "SRM/USDT", "EPS/USDT", "HBAR/USDT", "HIGH/USDT", "COMP/USDT", "ZEN/USDT",
               "RSR/USDT", "RAD/USDT", "CELO/USDT", "ANKR/USDT", "SPELL/USDT", "IDEX/USDT", "DOTUP/USDT", "WAVES/USDT",
               "UST/USDT", "ONT/USDT", "OCEAN/USDT", "UNFI/USDT", "TRU/USDT", "AUDIO/USDT", "AUTO/USDT", "KEY/USDT",
               "NEO/USDT", "PYR/USDT", "JOE/USDT", "DODO/USDT", "KSM/USDT", "JASMY/USDT", "FXS/USDT", "RNDR/USDT",
               "LIT/USDT", "ANY/USDT", "IOST/USDT", "WTC/USDT", "REEF/USDT", "KLAY/USDT", "QTUM/USDT", "STX/USDT",
               "BTS/USDT", "ALCX/USDT", "FLUX/USDT", "GNO/USDT", "SUPER/USDT", "TFUEL/USDT", "HIVE/USDT", "REN/USDT",
               "CTSI/USDT", "MC/USDT", "FIO/USDT", "CTK/USDT", "BLZ/USDT", "YGG/USDT", "MOVR/USDT", "NU/USDT",
               "GTO/USDT", "OGN/USDT", "CHESS/USDT", "POND/USDT", "BOND/USDT", "XEC/USDT", "RLC/USDT", "BAKE/USDT",
               "TCT/USDT", "BTCDOWN/USDT", "QNT/USDT", "SUN/USDT", "ATA/USDT", "MITH/USDT", "STORJ/USDT", "RAY/USDT",
               "ORN/USDT", "MKR/USDT", "BTCUP/USDT", "ILV/USDT", "SKL/USDT", "KEEP/USDT", "DF/USDT", "LAZIO/USDT",
               "VTHO/USDT", "BETA/USDT", "DGB/USDT", "USDP/USDT", "DOTDOWN/USDT", "SC/USDT", "YFII/USDT", "WRX/USDT"]:
    print_chart(binance, symbol, timeframe)