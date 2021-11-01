import requests
import tradingview_ta
from tradingview_ta import Exchange, Interval, TA_Handler
import config
from binance.client import Client
from decimal import *
import time
from datetime import datetime

def get_symbols():
    st_time=time.time()
    response=requests.get("https://api.binance.com/api/v3/exchangeInfo")
    j=response.json()
    pairs_data=j['symbols']
    full_data_dic = {s['symbol']: s for s in pairs_data if "USDT" in s['symbol']}
    fdd=list(full_data_dic.keys())
    for i in fdd:
        if "UP" in i or "DOWN" in i:
            fdd.remove(i)
    for i in fdd:
        try:
            handler= TA_Handler(symbol=i,exchange="binance",screener="crypto",interval="15m",timeout=None)
            handler.get_analysis()
        except:
            fdd.remove(i)
    end_time=time.time()

    print(f"{len(fdd)} symbols found. in {end_time-st_time} seconds")          
    return fdd

symbols=['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'NEOUSDT', 'LTCUSDT', 'QTUMUSDT', 'ADAUSDT', 'XRPUSDT', 'EOSUSDT', 'TUSDUSDT', 'IOTAUSDT', 'XLMUSDT', 'ONTUSDT', 'TRXUSDT', 'ETCUSDT', 'ICXUSDT', 'NULSUSDT', 'VETUSDT', 'USDCUSDT', 'LINKUSDT', 'WAVESUSDT', 'BTTUSDT', 'ONGUSDT', 'HOTUSDT', 'ZILUSDT', 'ZRXUSDT', 'FETUSDT', 'BATUSDT', 'XMRUSDT', 'ZECUSDT', 'IOSTUSDT', 'CELRUSDT', 'DASHUSDT', 'NANOUSDT', 'OMGUSDT', 'THETAUSDT', 'ENJUSDT', 'MITHUSDT', 'MATICUSDT', 'ATOMUSDT', 'TFUELUSDT', 'ONEUSDT', 'FTMUSDT', 'ALGOUSDT', 'GTOUSDT', 'DOGEUSDT', 'DUSKUSDT', 'ANKRUSDT', 'WINUSDT', 'COSUSDT', 'COCOSUSDT', 'MTLUSDT', 'TOMOUSDT', 'PERLUSDT', 'DENTUSDT', 'MFTUSDT', 'KEYUSDT', 'DOCKUSDT', 'WANUSDT', 'FUNUSDT', 'CVCUSDT', 'CHZUSDT', 'BANDUSDT', 'BUSDUSDT', 'BEAMUSDT', 'XTZUSDT', 'RENUSDT', 'RVNUSDT', 'HBARUSDT', 'NKNUSDT', 'STXUSDT', 'KAVAUSDT', 'ARPAUSDT', 'IOTXUSDT', 'RLCUSDT', 'CTXCUSDT', 'BCHUSDT', 'TROYUSDT', 'VITEUSDT', 'FTTUSDT', 'BUSDTRY', 'USDTTRY', 'USDTRUB', 'EURUSDT', 'OGNUSDT', 'DREPUSDT', 'TCTUSDT', 'WRXUSDT', 'BTSUSDT', 'LSKUSDT', 'BNTUSDT', 'LTOUSDT', 'AIONUSDT', 'MBLUSDT', 'COTIUSDT', 'STPTUSDT', 'WTCUSDT', 'DATAUSDT', 'SOLUSDT', 'USDTIDRT', 'CTSIUSDT', 'HIVEUSDT', 'CHRUSDT', 'GXSUSDT', 'ARDRUSDT', 'MDTUSDT', 'STMXUSDT', 'KNCUSDT', 'REPUSDT', 'LRCUSDT', 'PNTUSDT', 'USDTUAH', 'COMPUSDT', 'USDTBIDR', 'SCUSDT', 'ZENUSDT', 'SNXUSDT', 'VTHOUSDT', 'DGBUSDT', 'GBPUSDT', 'SXPUSDT', 'MKRUSDT', 'DCRUSDT', 'STORJUSDT', 'MANAUSDT', 'AUDUSDT', 'YFIUSDT', 'BALUSDT', 'BLZUSDT', 'IRISUSDT', 'KMDUSDT', 'USDTDAI', 'JSTUSDT', 'SRMUSDT', 'ANTUSDT', 'CRVUSDT', 'SANDUSDT', 'OCEANUSDT', 'NMRUSDT', 'DOTUSDT', 'LUNAUSDT', 'RSRUSDT', 'PAXGUSDT', 'WNXMUSDT', 'TRBUSDT', 'BZRXUSDT', 'SUSHIUSDT', 'YFIIUSDT', 'KSMUSDT', 'EGLDUSDT', 'DIAUSDT', 'RUNEUSDT', 'FIOUSDT', 'UMAUSDT', 'USDTNGN', 'BELUSDT', 'WINGUSDT', 'UNIUSDT', 'NBSUSDT', 'OXTUSDT', 'SUNUSDT', 'AVAXUSDT', 'HNTUSDT', 'FLMUSDT', 'ORNUSDT', 'UTKUSDT', 'XVSUSDT', 'ALPHAUSDT', 'USDTBRL', 'AAVEUSDT', 'NEARUSDT', 'FILUSDT', 'INJUSDT', 'AUDIOUSDT', 'CTKUSDT', 'AKROUSDT', 'AXSUSDT', 'HARDUSDT', 'DNTUSDT', 'STRAXUSDT', 'UNFIUSDT', 'ROSEUSDT', 'AVAUSDT', 'XEMUSDT', 'SKLUSDT', 'SUSDUSDT', 'GRTUSDT', 'JUVUSDT', 'PSGUSDT', 'USDTBVND', '1INCHUSDT', 'REEFUSDT', 'OGUSDT', 'ATMUSDT', 'ASRUSDT', 'CELOUSDT', 'RIFUSDT', 'BTCSTUSDT', 'TRUUSDT', 'CKBUSDT', 'TWTUSDT', 'FIROUSDT', 'LITUSDT', 'SFPUSDT', 'DODOUSDT', 'CAKEUSDT', 'ACMUSDT', 'BADGERUSDT', 'FISUSDT', 'OMUSDT', 'PONDUSDT', 'DEGOUSDT', 'ALICEUSDT', 'LINAUSDT', 'PERPUSDT', 'RAMPUSDT', 'CFXUSDT', 'EPSUSDT', 'AUTOUSDT', 'TKOUSDT', 'PUNDIXUSDT', 'TLMUSDT', 'BTGUSDT', 'MIRUSDT', 'BARUSDT', 'FORTHUSDT', 'BAKEUSDT', 'BURGERUSDT', 'SLPUSDT', 'SHIBUSDT', 'ICPUSDT', 'ARUSDT', 'POLSUSDT', 'MDXUSDT', 'MASKUSDT', 'LPTUSDT', 'NUUSDT', 'XVGUSDT', 'ATAUSDT', 'GTCUSDT', 'TORNUSDT', 'KEEPUSDT', 'ERNUSDT', 'KLAYUSDT', 'PHAUSDT', 'BONDUSDT', 'MLNUSDT', 'DEXEUSDT', 'C98USDT', 'CLVUSDT', 'QNTUSDT', 'FLOWUSDT', 'TVKUSDT', 'MINAUSDT', 'RAYUSDT', 'FARMUSDT', 'ALPACAUSDT', 'QUICKUSDT', 'MBOXUSDT', 'FORUSDT', 'REQUSDT', 'GHSTUSDT', 'WAXPUSDT', 'TRIBEUSDT', 'GNOUSDT', 'XECUSDT', 'ELFUSDT', 'DYDXUSDT', 'POLYUSDT', 'IDEXUSDT', 'VIDTUSDT', 'USDPUSDT', 'GALAUSDT', 'ILVUSDT', 'YGGUSDT', 'SYSUSDT', 'DFUSDT', 'FIDAUSDT', 'FRONTUSDT', 'CVPUSDT', 'AGLDUSDT', 'RADUSDT', 'BETAUSDT', 'RAREUSDT', 'LAZIOUSDT', 'CHESSUSDT', 'ADXUSDT', 'AUCTIONUSDT']


class PSAR_Strategy():
    def __init__(self,interval,symbols):
        #daha sonra mevcut paranın yüzde kaçının kullanılacağını seç
        #self.money=money
        self.symbols=symbols
        self.interval=interval
        self.client=Client(config.apiKey,config.apiSecurity)
        self.prev_indi={}
        for i in self.symbols:
            self.prev_indi[i]=-1


    def get_signal(self,c_symbol):
        handler= TA_Handler(symbol=c_symbol,exchange="binance",screener="crypto",interval="15m",timeout=None)
        anal=handler.get_analysis()


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
        LIMIT=CURR_PRICE+1.5*(CURR_PRICE-STOP_LOSS)

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


    
        if Decimal(x)>0:
            return int(x.split('.')[0])

        return Decimal(x.split('.')[0]+'.'+x.split('.')[1][0:count+2])



    def set_sl_limit(self,symbol,p_sar,curr_price):
        qty=self.get_oco_quantity(symbol=symbol)
        stop_loss,limit_p=self.sl_limit(p_sar,curr_price)
        self.client.order_oco_sell(symbol=symbol,quantity=qty,price=limit_p,stopPrice=stop_loss,stopLimitPrice=stop_loss,stopLimitTimeInForce="GTC")





    def buy_exchange(self,symbol):
        symbol=symbol
        money=self.get_oco_quantity("USDTUSDT")
        self.client.order_market_buy(symbol=symbol,quoteOrderQty=money)

    def start(self):
        
        while True:
            st_time=time.time()
            print(str(datetime.now())[0:-7])
            print("++++++++++++++++++++++++++++++++++++++++++")
            for symbol in self.symbols:
                signal,pSar,currPrice=self.get_signal(symbol)
                if signal and len(self.client.get_open_orders())==0:
                    try:
                        self.buy_exchange(symbol)
                        print(f"{symbol} has been succesfully bought!")
                    except:
                        print(f"An error occured with {symbol} purchase!")
                    try:    
                        self.set_sl_limit(symbol,pSar,currPrice)
                        print(f"sl/limit order succesfully placed for {symbol}!")
                        print("-------------------------------------------------")
                        
                    except:
                        print(f"An error occured with sl/limit order of {symbol}!")
                        print("-------------------------------------------------")
            print("Loop done.")
            end_time=time.time()
            

            time.sleep(self.interval*60-(end_time-st_time)+0.2)
        


strategy=PSAR_Strategy(15,symbols)
strategy.start()
