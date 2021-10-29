import tradingview_ta
from tradingview_ta import Exchange, Interval, TA_Handler
import config
from binance.client import Client
from decimal import *
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



        if self.prev_indi[c_symbol]>0 and OPENING_PRICE>P_SAR and P_SAR>EMA :
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

        precision=len(str(CURR_PRICE).split('.')[1])
        return round(Decimal(STOP_LOSS),precision),round(Decimal(LIMIT),precision)


    def get_oco_quantity(self,symbol):
        count=0
        balances=self.client.get_account()['balances']

        for i in balances:
            if symbol[0:-4] in i.values():
                x=i['free']
                break
        if '.' in x:        
            for i in x.split('.')[1]:
                if i=='0':
                    count+=1
                    #0.0003235346
                else:
                    break    
        else:
            return int(x)
        
        return Decimal(x.split('.')[0]+'.'+x.split('.')[1][0:count+2])

    def set_sl_limit(self,symbol,p_sar,curr_price):
        qty=self.get_oco_quantity(symbol=symbol)
        stop_loss,limit_p=self.sl_limit(p_sar,curr_price)
        self.client.order_oco_sell(symbol=symbol,quantity=qty,price=limit_p,stopPrice=stop_loss,stopLimitPrice=stop_loss,stopLimitTimeInForce="GTC")


    def buy_exchange(self,symbol):
        symbol=symbol

        self.client.order_market_buy(symbol=symbol,quoteOrderQty=self.money)
        self.money=0

    def start(self,symbol):
        

        self.client.order_oco_sell(symbol=symbol,)

