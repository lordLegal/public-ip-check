import requests
import time

t = time.strftime("%d, %m, %Y")
geschrieben = False
while True:
	h = time.strftime("%H") 
	m = time.strftime("%M")
	if (h=="16") and (m=="40") and geschrieben == False:
		a = requests.get('http://ip.42.pl/raw').text
		t = time.strftime("%d, %m, %Y")
		with open("ip.txt", "w") as fh:
			fh.write(a + "--" + t)
		print("Feritg")
		geschriben = True
	
	if (h=="00") and (m=="00") and geschrieben == True:
        geschrieben = False
