import random

motivasyonlar = [
    "Az kalsın!",
    "Yaklaşıyorsun!",
    "Olmak üzere!",
    "Pes etme, biraz daha düşün!",
    "Sayı seni bekliyor!"
]

while True:
    print("\nSayı Tahmin Oyununa Hoş Geldin!")
    print("Zorluk seç: kolay, orta, zor")

    seviye = input("Seçimin: ").lower()

    if seviye == "kolay":
        alt_sinir = 1
        ust_sinir = 50
    elif seviye == "zor":
        alt_sinir = 1
        ust_sinir = 200
    else:
        alt_sinir = 1
        ust_sinir = 100

    sayi = random.randint(alt_sinir, ust_sinir)
    tahmin_sayisi = 0

    while True:
        tahmin = int(input("Tahminin: "))
        tahmin_sayisi += 1

        if tahmin < sayi:
            print("Daha büyük bir sayı söyle.")
            print(random.choice(motivasyonlar))
        elif tahmin > sayi:
            print("Daha küçük bir sayı söyle.")
            print(random.choice(motivasyonlar))
        else:
            print(f"Tebrikler! {tahmin_sayisi} denemede bildin!")
            puan = max(0, 100 - tahmin_sayisi * 5)
            print(f"Puanın: {puan}")
            break  # içteki tahmin döngüsünü bitir

    tekrar = input("Yeniden oynamak ister misin? (evet/hayır): ").lower()
    if tekrar != "evet":
        print("Teşekkürler, tekrar görüşmek üzere!")
        break  # en dıştaki oyun döngüsünü bitir

    
        
        
   
    