from urllib.request import urlopen
from bs4 import BeautifulSoup

year = 2019
month = 9
week = 2

 
url = urlopen("https://music.naver.com/listen/history/index.nhn?type=TOTAL&year=%d&month=0%d&week=%d" %(year,month,week))
#url = urlopen("https://music.naver.com/listen/history/index.nhn?type=TOTAL&year=2019&month=09&week=02") 위와 URL주소 동일
#현재 주소가 차트 히스토리 주소, 주별로 뽑기위해 위 링크로 설정

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
print(temp)
  
 
# 현재 2012년부터 2017년은 번호 자릿수가 두 칸 잘려나오고 50위까지 전부 나오지 않음
# 번호가 틀렸던 우리 둘 URL이 잘못 됐었음. 난 차트 히스토리 URL 넌 Top 100차트 URL 이것 때문에 번호가 다르게 나옴
