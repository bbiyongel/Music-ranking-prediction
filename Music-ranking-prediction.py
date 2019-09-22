from urllib.request import urlopen
from bs4 import BeautifulSoup

year = 2013
month = 1
week = 1

while (1):
    if week is 5:
        week = 1
        month += 1

    if month is 13:
        month = 1
        year += 1

    if year is 2019 and month is 9 and week is 4:
        print("end")
        break


   
    myurl = "https://music.naver.com/listen/history/index.nhn?type=TOTAL&year="+str(year)+"&month=0"+str(month)+"&week="+str(week)
    print(myurl)
    url = urlopen(myurl)

    soup = BeautifulSoup(url,"lxml")
    temp = []
    for link1 in soup.find_all(name="td",attrs={"class":"ico"}):
        try:
            a = link1.select('a')[0]['href'] #a 태그에서 href만 가져오기
            a = a.strip("#")
            if a is "":
                pass
            else:
                temp.append(a)      
        except:
            pass
            #print("href 없음")

    week += 1
    print(temp)


print(temp)

