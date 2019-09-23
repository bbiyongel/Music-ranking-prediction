from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

year = 2019
month = 9
week = 1
temp = []
ranks = []

while (1):
    if week is 5:
        week = 1
        month += 1

    if month is 13:
        month = 1
        year += 1

    if year is 2019 and month is 9 and week is 3:
        print("end")
        break
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
            print(rank.text)
            ranks.append(span)
        except:
            pass
            #print("href 없음")
        
    week += 1
    print(ranks)
#data = pd.DataFrame(temp)
#data.to_csv('idval.csv', encoding='utf-8')  
#print("저장성공")   