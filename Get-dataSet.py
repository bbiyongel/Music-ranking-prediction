import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame


f = open('idval.csv', 'r')
reader = csv.reader(f)

data1 = []
data2 = []
data3 = []
data4 = []

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
        data1.append(get_Sing)
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
            get_Composer.strip() #공백제거
            data2.append(get_Composer)
            print(get_Composer)
        except:
            print('작곡가정보없음')
            pass
        try:
            get_Lyricist = get_song_info.select('span')[1]
            get_Lyricist = get_Lyricist.select('a')[0]
            get_Lyricist = get_Lyricist.text
            get_Lyricist.strip() #공백제거
            data3.apped(get_Lyricist)
            print(get_Lyricist)
        except:
            print('작사가정보없음')
            pass
        try:
            get_Arrangement = get_song_info.select('span')[2]
            get_Arrangement = get_Arrangement.select('a')[0]
            get_Arrangement = get_Arrangement.text
            get_Arrangement.strip() #공백제거
            data4.append(get_Arrangement)
            print(get_Arrangement)
        except:
            print('편곡정보없음')
            pass
    except:
        print('song info NULL')
        pass

data1 = DataFrame(data1)
data2 = DataFrame(data2)
data3 = DataFrame(data3)
data4 = DataFrame(data4)
data = pd.concat([data1,data2,data3,data4], axis = 1)
data = pd.DataFrame(data)
data.to_csv('dataset.csv', mode='a', encoding='utf-8',header=None)
print("저장성공")   
f.close()





