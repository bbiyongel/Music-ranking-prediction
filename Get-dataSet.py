import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame


f = open('idval.csv', 'r')
reader = csv.reader(f)

for row in reader:
    rank = row[0] #rank
    URL_ID = row[1] #URL Num ID
    myurl = "https://music.naver.com/lyric/index.nhn?trackId="+str(URL_ID)
    #print(myurl)
    url = urlopen(myurl)
    soup = BeautifulSoup(url,"lxml")
    try:
        get_Sing = soup.find(name="span",attrs={"class":"artist"})
        get_Sing = get_Sing.select('a')[0]['title']
        print(get_Sing)
    except:
        print('가수정보없음')
        pass
    try:
        get_song_info = soup.find(name="p",attrs={"class":"song_info"})#작곡가

        try:
            get_Composer = get_song_info.select('span')[0]
            get_Composer = get_Composer.select('a')[0]
            get_Composer = get_Composer.text
            print(get_Composer.strip()) #공백제거
        except:
            print('작곡가정보없음')
            pass
        try:
            get_Lyricist = get_song_info.select('span')[1]
            get_Lyricist = get_Lyricist.select('a')[0]
            get_Lyricist = get_Lyricist.text
            print(get_Lyricist.strip()) #공백제거
        except:
            print('작사가정보없음')
            pass
        try:
            get_Arrangement = get_song_info.select('span')[2]
            get_Arrangement = get_Arrangement.select('a')[0]
            get_Arrangement = get_Arrangement.text
            print(get_Arrangement.strip()) #공백제거
        except:
            print('편곡정보없음')
            pass
    except:
        print('song info NULL')
        pass
#csv 파일 이름은 dataset.csv 로 한다.

f.close()





