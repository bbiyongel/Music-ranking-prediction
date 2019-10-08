#수집한 주소를 이용, 작사, 작곡, 가수... 데이터를 수집
#csv파일로 저장
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame


f = open('idval.csv', 'r')
reader = csv.reader(f)
temp2 = []

for row in reader:
    temp = []
    rank = row[0] #rank
    URL_ID = row[1] #URL Num ID
    myurl = "https://music.naver.com/lyric/index.nhn?trackId="+str(URL_ID)
    #print(myurl)
    url = urlopen(myurl)
    soup = BeautifulSoup(url,"lxml")
    try:
        get_Sing = soup.find(name="span",attrs={"class":"artist"})
        get_Sing = get_Sing.select('a')[0]['title']
        #print(get_Sing)
        temp.append(rank)
        temp.append(get_Sing)
    except:
        print('가수정보없음')
        temp.append('')
        pass
    try:
        get_song_info = soup.find(name="p",attrs={"class":"song_info"})#작곡가

        try:
            get_Composer = get_song_info.select('span')[0]
            get_Composer = get_Composer.select('a')[0]
            get_Composer = get_Composer.text
            #print(get_Composer.strip()) #공백제거
            temp.append(get_Composer.strip())
        except:
            print('작곡가정보없음')
            temp.append('')
            pass
        try:
            get_Lyricist = get_song_info.select('span')[1]
            get_Lyricist = get_Lyricist.select('a')[0]
            get_Lyricist = get_Lyricist.text
            #print(get_Lyricist.strip()) #공백제거
            temp.append(get_Lyricist.strip())
        except:
            print('작사가정보없음')
            temp.append('')
            pass
        try:
            get_Arrangement = get_song_info.select('span')[2]
            get_Arrangement = get_Arrangement.select('a')[0]
            get_Arrangement = get_Arrangement.text
            #print(get_Arrangement.strip()) #공백제거
            temp.append(get_Arrangement.strip())
        except:
            print('편곡정보없음')
            temp.append('')
            pass
    except:
        print('song info NULL')
        pass
    temp2.append(temp)
    if len(temp2) is 200:
        data = pd.DataFrame(temp2)
        data.to_csv('dataset.txt', mode='a', encoding='utf-8',header=None)
        temp2 = []
    #print(temp2)
#temp2.append(temp)
data = pd.DataFrame(temp2)
data.to_csv('dataset.txt', mode='a', encoding='utf-8',header=None)

f.close()





