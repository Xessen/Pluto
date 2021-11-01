from decimal import Decimal
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
    if Decimal(x)>0:
        return(x.split('.')[0])
       
    return Decimal(x.split('.')[0]+'.'+x.split('.')[1][0:count+2])



def sl_limit(P_SAR,CURR_PRICE):
        STOP_LOSS=P_SAR
        LIMIT=CURR_PRICE+1.5*(CURR_PRICE-STOP_LOSS)
        precision=len(str(CURR_PRICE).split('.')[1])
        return round(Decimal(STOP_LOSS),precision),round(Decimal(LIMIT),precision)

def set_sl_limit(symbol,p_sar,curr_price):
    qty=get_oco_quantity(symbol=symbol)
    stop_loss,limit_p=sl_limit(p_sar,curr_price)
    print(type(stop_loss))
    print(type(limit_p))

    client.order_oco_sell(symbol=symbol,quantity=qty,price=limit_p,stopPrice=stop_loss,stopLimitPrice=stop_loss,stopLimitTimeInForce="GTC")

prev_indi={'COCOSUSDT':1}

def get_signal(c_symbol):
        handler= TA_Handler(symbol=c_symbol,exchange="binance",screener="crypto",interval="15m",timeout=None)
        anal=handler.get_analysis()


        OPENING_PRICE=anal.indicators['open']
        EMA=anal.indicators['EMA200']
        P_SAR=anal.indicators['P.SAR']



        if prev_indi[c_symbol]>0 and OPENING_PRICE>P_SAR and P_SAR>EMA :
            INDI_=P_SAR-OPENING_PRICE
            prev_indi.update({c_symbol:INDI_})
            print(prev_indi)
            return True,P_SAR,OPENING_PRICE
        else:
            INDI_=P_SAR-OPENING_PRICE
            prev_indi.update({c_symbol:INDI_})
            print(prev_indi)
            return False,False,False

        

#print(get_signal('COCOSUSDT'))
#print(prev_indi['COCOSUSDT']>0)
#print(client.get_symbol_info("ALPACAUSDT"))
#set_sl_limit("KNCUSDT",1.796,1.915)
#print(float(0.99 * (float(0.0015))))
print(get_oco_quantity("ZRXUSDT"))
set_sl_limit("ZRXUSDT",1.3065,1.4462)
#print(sl_limit(34765.74,34594.16))
#orders=client.get_open_orders()



#print(orders)

