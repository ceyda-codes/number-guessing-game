#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 00:00:23 2025

@author: ceydaaygun
"""

import requests
from datetime import datetime

API_KEY = "e386e085524bbf832285dbbe30704066"

def hava_durumu_al(sehir):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={API_KEY}&units=metric&lang=tr"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f"\n{sehir.title()} için hava durumu ({datetime.now().strftime('%d %B %Y %H:%M')}):")
        print(f"Sıcaklık: {data['main']['temp']}°C")
        print(f"Durum: {data['weather'][0]['description'].title()}")
        print(f"Nem: {data['main']['humidity']}%")
        print(f"Rüzgar: {data['wind']['speed']} m/s")
        ikon_kodu = data['weather'][0]['icon']
        print(f"İkon (link): http://openweathermap.org/img/wn/{ikon_kodu}@2x.png")
    else:
        print("Şehir bulunamadı. Lütfen tekrar deneyin.")

while True:
    sehir = input("\nHangi şehrin hava durumunu öğrenmek istersin? (Boş bırakırsan İstanbul): ").strip()
    if not sehir:
        sehir = "istanbul"
    hava_durumu_al(sehir)
    
    tekrar = input("\nBaşka bir şehir için hava durumu bakmak ister misin? (e/h): ").strip().lower()
    if tekrar != "e":
      print("Görüşürüz!")
      break  