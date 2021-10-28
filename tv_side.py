import tradingview_ta
from tradingview_ta import Exchange, Interval, TA_Handler
import config
from binance.client import Client
from bnc_side import *


class PSAR_Strategy():
    def __init__(self,money,symbols,interval):
        self.money=money
        self.symbols=symbols
        self.interval=interval
        self.client=Client(config.apiKey,config.apiSecurity)
        self.prev_indi={}



    def get_signal(self,c_symbol,current_trades):
        handler= TA_Handler(symbol=c_symbol,exchange="binance",screener="crypto",interval=self.interval,timeout=None)
        anal=handler.get_analysis()

        is_unique=c_symbol in current_trades

        OPENING_PRICE=anal.indicators['open']
        EMA=anal.indicators['EMA200']
        P_SAR=anal.indicators['P.SAR']



        if self.prev_indi[c_symbol]>0 and OPENING_PRICE>P_SAR and EMA>P_SAR:
            INDI_=P_SAR-OPENING_PRICE
            self.prev_indi.update({c_symbol:INDI_})
            return True,P_SAR,OPENING_PRICE
        else:
            INDI_=P_SAR-OPENING_PRICE
            self.prev_indi.update({c_symbol:INDI_})
            return False,False,False

    def sl_limit(self,P_SAR,CURR_PRICE):
        STOP_LOSS=P_SAR
        LIMIT=CURR_PRICE+1.5(CURR_PRICE-STOP_LOSS)

        return STOP_LOSS,LIMIT

    def set_sl_limit(self):
        pass

    def buy_exchange(self,symbol):
        symbol=symbol

        self.client.order_market_buy(symbol=symbol,quoteOrderQty=self.money)
        self.money=0

    def start(self):
        pass

