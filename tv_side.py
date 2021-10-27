import tradingview_ta
from tradingview_ta import Exchange, Interval, TA_Handler


class PSAR_Strategy():
    def __init__(self,money,symbols,interval):
        self.money=money
        self.symbols=symbols
        self.interval=interval



    def get_signal(self,c_symbol,current_trades):
        handler= TA_Handler(symbol=c_symbol,exchange="binance",screener="crypto",interval=self.interval,timeout=None)
        anal=handler.get_analysis()

        is_unique=c_symbol in current_trades

        OPENING_PRICE=anal.indicators['open']
        EMA=anal.indicators['EMA200']
        P_SAR=anal.indicators['P.SAR']

        if is_unique and OPENING_PRICE>P_SAR and EMA>P_SAR:
            return True,P_SAR,OPENING_PRICE
        else:
            return False,False,False

    def sl_limit(self,P_SAR,CURR_PRICE):
        STOP_LOSS=P_SAR
        LIMIT=CURR_PRICE+1.5(CURR_PRICE-STOP_LOSS)

        return STOP_LOSS,LIMIT
