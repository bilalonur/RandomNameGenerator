# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:37:56 2020

@author: onur@bilalonureskili.com
"""
import random

x = [] #Erkek İsim
y = [] #Soyadlar
z = [] #Kadın İsim

dosya = open("e_ad.txt","r") #Erkek İsim

for i in dosya:
    i = i[:-1]
    x.append(i)

dosya.close()

dosya1 = open("soyad.txt","r",) #Soyad
for n in dosya1:
    n = n[:-1]
    y.append(n)

dosya1.close()

dosya2 = open("k_ad.txt","r") #Kadın İsim
for ff in dosya2:
    ff = ff[:-1]
    z.append(ff)

dosya2.close()

new = random.choice(x)+" "+random.choice(y)
inp = "0"
e_m = input("Kadın için K ; Erkek için E : ")
if e_m == "E" :
    while inp != -1:
        yeni = []
        inp = int(input("Kaç kişi oluşturulsun ? (Çıkış:-1) "))
        if inp > 0:
            
            for t in range(inp):
                isimler = ""
                isim_s = random.randint(1,2)
                for cx in range(1,isim_s+1):
                    isimler += random.choice(x)+" "
                new = isimler +random.choice(y)
                yeni.append(new)
        print(yeni)
elif e_m == "K":
    while inp != -1:
        yeni = []
        inp = int(input("Kaç kişi oluşturulsun ? (Çıkış:-1) "))
        if inp > 0:
            
            for t in range(inp):
                isimler = ""
                isim_s = random.randint(1,2)
                for cx in range(1,isim_s+1):
                    isimler += random.choice(z)+" "
                new = isimler +random.choice(y)
                yeni.append(new)
        print(yeni)
else:
    print("E/M harflerini giriniz lütfen.")
