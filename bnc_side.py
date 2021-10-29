def round4binance(num):
    count=0
    num=str(num)
    for i in num:
        if i=='0' or i=='.':
            count+=1
        else:
            break
    return float(num[0:(count+2)])

import requests

print(round(0.124125124,6))

def precision_finder(symbol):
    response=requests.get("https://api.binance.com/api/v3/exchangeInfo")

    return next(element for element in response.json()['symbols'] if element['symbol']==symbol)['baseAssetPrecision']
    
x="0.0000009784000"
count=6
print(f"{float(x.split('.')[0]+'.'+x.split('.')[1][0:count+2]):.{count+2}f}")


