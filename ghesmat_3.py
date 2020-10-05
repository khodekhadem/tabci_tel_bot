import requests

url_1 = "https://api.telegram.org/bot1230162522:AAGiRSx0lDsc8klMov02vSgvTS-Ki7ZL5w4/GetUpdates"
url_2 = "https://api.telegram.org/bot1230162522:AAGiRSx0lDsc8klMov02vSgvTS-Ki7ZL5w4/SendMessage?chat_id=1281712645&text="

def sendMessage ():
    text_1 = input("matn vared con \n")
    text_1 = url_2+text_1
    requests.post(text_1)
def reseveMessage():
    result = requests.post(url_1)
    result = result.text
    a = result.rfind('"id":1281712645')
    b = result.find('"text":"',a)
    c = result.find('"}}]}',b)
    result = result[b+8:c]
    print(result)
#sendMessage()
reseveMessage()