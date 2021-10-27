import tradingview_ta
from tradingview_ta import Exchange, Interval, TA_Handler

handler= TA_Handler(symbol="BTCUSDT",exchange="binance",screener="crypto",interval="1h",timeout=None)
anal=handler.get_analysis()

