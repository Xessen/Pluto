def round4binance(num):
    count=0
    num=str(num)
    for i in num:
        if i=='0' or i=='.':
            count+=1
        else:
            break
    return float(num[0:(count+2)])