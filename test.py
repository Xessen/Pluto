from binance.client import Client  
from binance.enums import * 
import config
import tradingview_ta
from tradingview_ta import Exchange, Interval, TA_Handler

client=Client(config.apiKey,config.apiSecurity)
def round4binance(num):
    count=0
    num=str(num)  
    for i in num:
        if i=='0' or i=='.':
            count+=1
        else:
            break
    if count==0:
        return float(num)
    else:
        return float()







a=client.get_all_orders(symbol="BTCUSDT")

handler= TA_Handler(symbol="BTCUSDT",exchange="binance",screener="crypto",interval="15m",timeout=None)
anal=handler.get_analysis()
quantity=anal.indicators['close']
#print(28.0581861/quantity*0.99)
#print(round4binance(3121.0))
client.create_test_order(symbol="BTCUSDT",side=SIDE_BUY,type=ORDER_TYPE_MARKET,quoteOrderQty=self.money)