import pandas as pd
import pandas_datareader.data as web
import datetime as d
import matplotlib.pyplot as plt

start=d.datetime(2021,4,1)
middle=d.datetime(2021,4,30)
end=d.datetime(2021,5,21)
samsung=web.DataReader("005930.KS","yahoo", start, end)
LG=web.DataReader("066570.KS", "yahoo", start, end)
hyundai=web.DataReader("011760.KS", "yahoo", start, end)
kakao=web.DataReader("035720.KS", "yahoo", start, end)
kia=web.DataReader("000270.KS", "yahoo", start, end)
samsung4=web.DataReader("005930.KS","yahoo", start, middle)
LG4=web.DataReader("066570.KS", "yahoo", start, middle)
hyundai4=web.DataReader("011760.KS", "yahoo", start, middle)
kakao4=web.DataReader("035720.KS", "yahoo", start, middle)
kia4=web.DataReader("000270.KS", "yahoo", start, middle)
samsung5=web.DataReader("005930.KS","yahoo", middle, end)
LG5=web.DataReader("066570.KS", "yahoo", middle, end)
hyundai5=web.DataReader("011760.KS", "yahoo", middle, end)
kakao5=web.DataReader("035720.KS", "yahoo", middle, end)
kia5=web.DataReader("000270.KS", "yahoo", middle, end)

def mn(a):
    return round(a.mean(),1)
s=mn(samsung['Volume'])
L=mn(LG['Volume'])
h=mn(hyundai['Volume'])
ka=mn(kakao['Volume'])
ki=mn(kia['Volume'])
s4=mn(samsung4['Volume'])
L4=mn(LG4['Volume'])
h4=mn(hyundai4['Volume'])
ka4=mn(kakao4['Volume'])
ki4=mn(kia4['Volume'])
s5=mn(samsung5['Volume'])
L5=mn(LG5['Volume'])
h5=mn(hyundai5['Volume'])
ka5=mn(kakao5['Volume'])
ki5=mn(kia5['Volume'])

Data=[["SAMSUNG",s4,s5,s],["LG",L4,L5,L],["HYUNDAI",h4,h5,h],\
      ["KAKAO",ka4,ka5,ka],["KIA",ki4,ki5,ki]]
DF1=pd.DataFrame(Data, columns = ['종목','4월','5월','평균'],index=[0,1,2,3,4])
DF2=DF1.sort_values(by='평균', ascending=False)
DF3=DF2.reset_index(drop=True)
print(DF3)

plt.plot(samsung['Close'])
plt.plot(LG['Close'])
plt.plot(hyundai['Close'])
plt.plot(kakao['Close'])
plt.plot(kia['Close'])
plt.title("Korea Finance Close Graph")
plt.ylabel("Close")
plt.xlabel("Date")
plt.legend(['Samsung','LG','Hyundai','Kakao','Kia'])
plt.show()
