import requests
import time

t = time.strftime("%d, %m, %Y")
geschrieben = False
while True:
    h = time.strftime("%H") 
    m = time.strftime("%M")
    if (h=="21") and (m=="05") and geschrieben == False:
        a = requests.get('http://ip.42.pl/raw').text
        t = time.strftime("%d, %m, %Y")
        with open("ip.txt", "a") as fh:
            fh.write(a + "---" + t + "   ")
        print("Feritg")
        geschrieben = True
    
    if (h=="00") and (m=="00") and (geschrieben == True):
        geschrieben = False
