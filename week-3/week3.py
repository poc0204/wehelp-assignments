import urllib.request as req
import json
import re
import csv

url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
request=req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"})
with req.urlopen(request) as respone:
    data=respone.read().decode("utf-8")
j = json.loads(data)

data1 = j['result']['results']

with open('week3.csv', 'w', newline='',encoding='utf-8') as student_file:
    writer = csv.writer(student_file)
    for i  in range(len(data1)):
        http1 = re.search(r'^http',data1[i]['file']).span()
        jpg1 = re.search(r'jpg',data1[i]['file'], re.IGNORECASE).span()
        jsondata = data1[i]['stitle'] , data1[i]['address'][5:8],data1[i]['longitude'],data1[0]['longitude'],data1[i]['file'][http1[0]:jpg1[1]]
        writer.writerow(jsondata)
