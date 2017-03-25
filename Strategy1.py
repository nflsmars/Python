import pandas as pd
import pandas.io.data as web
import datetime
import numpy
#Download data from yahoo finance
start = datetime.datetime(2011,9,1)
end = datetime.datetime(2016,12,31)
writer=pd.ExcelWriter('./File/Strategy1.xlsx')
ticker = ('2330.tw','2303.tw','3008.tw','2498.tw','2311.tw','2409.tw','2357.tw','2317.tw','^TWII') 

for i in range(0,len(ticker)):
    stock_id=ticker[i]   
    f=web.DataReader(stock_id,'yahoo',start,end)
    adj_close = numpy.array(f['Adj Close'], dtype=float)
    rows=len(f.index)
    def sma(r,t):
        smav=[]
        for a in range (0,t,1):
            if a>r-1:
                c=a-r
                sum=0
                for i in range(0,r,1):
                    q=i+c
                    sum=sum+adj_close[q]
                smav.append(sum/r)              
            else:
                smav.append(0)  
        return smav
    f['SMA_20'] = sma(20,rows)
    f['SMA_50'] = sma(50,rows)
    sma_20 = numpy.array(f['SMA_20'], dtype=float)
    sma_50 = numpy.array(f['SMA_50'], dtype=float)
    f['DIFF'] = sma_20-sma_50
    def LoS(number):
        if number>0:
            return 1
        else:
            return 0
    f['Long or Short'] = f['DIFF'].map(LoS)
    def Ret(t):
        Retv=[0]
        for j in range (1,t,1):
            rt=numpy.log(adj_close[j]/adj_close[j-1])
            Retv.append(rt)
        return Retv
    f['Return'] = Ret(rows)
    los = numpy.array(f['Long or Short'], dtype=float)
    ret = numpy.array(f['Return'], dtype=float)
    f['Performance'] = los*ret
    f.drop(f.columns[[0,1,2,3,4,8]],axis=1,inplace=True) 
    opt=f[85:rows]
    opt.to_excel(writer,ticker[i])
writer.save()