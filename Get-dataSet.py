from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame

df = pd.read_csv('./idval.csv',sep=',')

column_df = df['songNum']


songInfo = []



#myurl = "https://music.naver.com/lyric/index.nhn?trackId="+str(column_df)

myurl = "https://music.naver.com/lyric/index.nhn?trackId=28450269"
print(myurl)
url = urlopen(myurl)

soup = BeautifulSoup(url,"lxml")

for info in soup.find_all(name="span",attrs={"class":"info"}):
    
    try:
        
        info = info.get_text()
        
        songInfo.append(info)
        
        '''
        if info is "\n":
            pass
        elif info is "\t":
            pass
        else:
            songInfo.append(info)
        '''
        #\t,\n,\r이 같이 출력됨
               
            
    except:
        pass
        #print("href 없음")
   



print(songInfo)

#data1 = DataFrame(ranks,columns=['rank'])  
#data2 = DataFrame(temp,columns=['songInfo'])
#data = pd.concat([data1,data2], axis = 1)
#data.to_csv('idval.csv', encoding='utf-8')  
print("저장성공")   
