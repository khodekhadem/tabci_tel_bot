import requests

url = "https://api.telegram.org/botتوکن بات خودتون/GetUpdates"

result = requests.post(url)
result = result.text
a = result.rfind('"id":1281712645')
b = result.find('"text":"',a)
c = result.find('"}}]}',b)
#print (result)
print(result[b+8:c])
