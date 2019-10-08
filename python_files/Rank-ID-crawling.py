from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame

#수집기간 2012년 1월 1째 주 부터 2019년 9월 까지
year = 2012
month = 1
week = 1
#temp = []
#ranks = []



while (1):
    temp = []
    ranks = []
    if year is 2019:
        #if문 무시하고 계속해서 숫자가 늘어나는 문제가 있음 
        if month is 10:
            #if week is 3:
            print("end")
            break
    else:
        pass
    if week is 5:
        week = 1
        month += 1
    else:
        pass
    if month is 13: 
        month = 1
        year += 1
    else:
        pass

    
    #현재 사이트에 2주까지 있어서 week은 3로 설정
    remonth = str(month).rjust(2, '0')
    myurl = "https://music.naver.com/listen/history/index.nhn?type=TOTAL&year="+str(year)+"&month="+str(remonth)+"&week="+str(week)
    print(myurl)
    url = urlopen(myurl)

    soup = BeautifulSoup(url,"lxml")
    
    for link1 in soup.find_all(name="td",attrs={"class":"name"}):
        
        try:
            a = link1.select('a')[3]['href'] #3번 a 태그에서 href만 가져오기
            a = a.strip("#")

            if a is "":
                pass
            else:
                temp.append(a)         
        except:
            pass
            #print("href 없음")
        
    for rank in soup.find_all(name="td",attrs={"class":"ranking"}):
        try:  
            span = rank.text
            ranks.append(span)

        except:
            pass
            #print("href 없음")   
    week += 1
    
    data1 = DataFrame(ranks)  
    data2 = DataFrame(temp)
    data = pd.concat([data1,data2], axis = 1)
    data = pd.DataFrame(data)
    data.to_csv('idval.csv', mode='a', encoding='utf-8',header=None)  
print("저장성공")   
