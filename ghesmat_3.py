import requests

url_1 = "https://api.telegram.org/botتوکن بات خودتون/GetUpdates"
url_2 = "https://api.telegram.org/botتوکن بات خودتون/SendMessage?chat_id=ایدی عددی تون&text="

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
reseveMessage()
sendMessage()
