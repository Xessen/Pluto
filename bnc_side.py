def get_signal(c_symbol):
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