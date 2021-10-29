from binance.client import Client  
from binance.enums import * 
import config
import tradingview_ta
from tradingview_ta import Exchange, Interval, TA_Handler

client=Client(config.apiKey,config.apiSecurity)
def round4binance(price):
    leng=len(str(price).split(".")[1])







#a=client.get_all_orders(symbol="BTCUSDT")

handler= TA_Handler(symbol="BTCUSDT",exchange="binance",screener="crypto",interval="15m",timeout=None)
anal=handler.get_analysis()
quantity=anal.indicators['close']
#print(28.0581861/quantity*0.99)
#print(round4binance(3121.0))

def get_oco_quantity(symbol):
    count=0
    balances=client.get_account()['balances']

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
    return f"{float(x.split('.')[0]+'.'+x.split('.')[1][0:count+2]):.{count+2}f}"



def sl_limit(P_SAR,CURR_PRICE):
        STOP_LOSS=P_SAR
        LIMIT=CURR_PRICE+1.5*(CURR_PRICE-STOP_LOSS)

        return round(STOP_LOSS,len(str(CURR_PRICE).split(".")[1])),round(LIMIT,len(str(CURR_PRICE).split(".")[1]))

def set_sl_limit(symbol,p_sar,curr_price):
    qty=get_oco_quantity(symbol=symbol)
    stop_loss,limit_p=sl_limit(p_sar,curr_price)
    client.order_oco_sell(symbol=symbol,quantity=qty,price=limit_p,stopPrice=stop_loss,stopLimitPrice=stop_loss,stopLimitTimeInForce="GTC")

#print(client.get_symbol_info("ALPACAUSDT"))
#set_sl_limit("ALPACAUSDT",0.8846,0.896)
#print(float(0.99 * (float(0.0015))))
#print(get_oco_quantity("USDTUSDT"))
print(sl_limit(34765.74,34594.16))