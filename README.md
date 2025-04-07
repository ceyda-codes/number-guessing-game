# Weather App - Hava Durumu Uygulaması

Bu Python uygulaması, OpenWeatherMap API kullanarak anlık hava durumu bilgilerini getirir.  
Kullanıcıdan şehir bilgisi alır, sıcaklık, nem, rüzgar hızı ve hava durumu gibi verileri terminalde gösterir.

## Özellikler

- Şehir bilgisi girişi (boş bırakılırsa varsayılan İstanbul)
- Anlık tarih ve saat bilgisi
- Hava durumu açıklaması (Türkçe)
- Hava durumu ikonu (OpenWeather linki)
- Kullanıcıya tekrar sorma özelliği

## Kullanım

1. Python 3 yüklü olmalıdır  
2. Gerekli paket: `requests`  
   ```bash
   pip install requests
3. Uygulamayı çalıştır:
   ```bash
   python3 hava_durumu.py
4. Örnek çıktı:
    Hangi şehrin hava durumunu öğrenmek istersin? (Boş bırakırsan İstanbul): bursa
    Bursa için hava durumu (08 Nisan 2025 15:45):
    Sıcaklık: 21.3°C
    Durum: Açık
    Nem: 48%
    Rüzgar: 2.3 m/s
    İkon: http://openweathermap.org/img/wn/01d@2x.png

## API
   Veriler OpenWeatherMap üzerinden alınmaktadır.
   Kendi API anahtarınızı almak için ücretsiz üye olabilirsiniz.

  