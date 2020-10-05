import requests

url = "https://api.telegram.org/bot1230162522:AAGiRSx0lDsc8klMov02vSgvTS-Ki7ZL5w4/GetUpdates"

result = requests.post(url)
result = result.text
a = result.rfind('"id":1281712645')
b = result.find('"text":"',a)
c = result.find('"}}]}',b)
#print (result)
print(result[b+8:c])