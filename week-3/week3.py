import urllib.request as req
import pandas as pd
import json
import re
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
request=req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"})
with req.urlopen(request) as respone:
    data=respone.read().decode("utf-8")
j = json.loads(data)

data1 = j ['result']['results']

df_SAMPLE = pd.DataFrame(data1)
df_SAMPLE.to_csv('week3.csv')
jsondata = pd.read_csv("week3.csv")


for i in range(len(jsondata)):
        
        http1 = re.search(r'^http',jsondata['file'][i]).span()
        jpg1 = re.search(r'jpg',jsondata['file'][i]).span()
        #print(jsondata['file'][i][http1[0]:jpg1[1]])
        print('景點名稱:',jsondata['stitle'][i],'區域:',jsondata['address'][i][5:8],'經緯度:',jsondata['longitude'][i],'網址:',jsondata['file'][i][http1[0]:jpg1[1]],"\n")
