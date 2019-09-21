from urllib.request import urlopen
from bs4 import BeautifulSoup
 
url = urlopen("https://music.naver.com/listen/top100.nhn?domain=TOTAL")
soup = BeautifulSoup(url,"lxml")
temp = []
for link1 in soup.find_all(name="td",attrs={"class":"ico"}):
    try:
        a = link1.select('a')[0]['href'] #a 태그에서 href만 가져오기
        a = a.strip("#")
        if a is '':
            pass
        else:
            temp.append(a)      
    except:
        pass
        #print("href 없음")
print(temp)
  
 
# 도메인에 year month for 돌려서 받아와 9월 3주까지
# print로 날짜 설정하고
