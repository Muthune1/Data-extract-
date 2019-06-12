import requests
import csv
from csv import writer

r = requests.get('https://gameads-admin.applifier.com/stats/monetization-api?apikey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&splitBy=zone,country&fields=platform,views,revenue&start=-4&end=-1&scale=day&sourceIds=2998620,1598743,1598742')
#print (r.status)
print (r.text)
with open('out_unity.csv','w') as f:   
 f.write(r.text)
f.close()

   
with open('out_unity.csv', 'r') as src, open('output_file_1.csv', 'w', newline='') as dst:
    wr = csv.writer(dst, dialect='excel', delimiter=',', quoting=csv.QUOTE_NONE, escapechar=' ')
    next(src)
    reader = csv.reader(src)
    for row in reader:
       wr.writerow(row)

