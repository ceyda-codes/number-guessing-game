#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 00:00:23 2025

@author: ceydaaygun
"""

import requests

API_KEY = "e386e085524bbf832285dbbe30704066"
city = input("Hangi şehrin hava durumunu öğrenmek istersin? ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"{city} için hava durumu:")
    print(f"Sıcaklık: {data['main']['temp']}°C")
    print(f"Durum: {data['weather'][0]['description']}")
    print(f"Nem: {data['main']['humidity']}%")
    print(f"Rüzgar: {data['wind']['speed']} m/s")
else:
    print("Şehir bulunamadı, lütfen tekrar deneyin.")