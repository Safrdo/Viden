import requests

#r= requests.post('https://api.telegram.org/bot1234567890:AAAAxY6udNO5u-9fO793yFdZaL1qU2RIkGT/sendMessage?chat_id=-704631232&text=hello world')
print("Enter the message")
message= input()
r= requests.post("https://api.telegram.org/bot5725334288:AAF-Kd7nadnASAuMZWLY2ExVGWV1TiNzLvY/sendMessage?chat_id=-704631232&text={}".format(message))
