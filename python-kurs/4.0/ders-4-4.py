#4️⃣.4️⃣ Class Constructors (Yapıcı Metotlar - __init__)
#✅ Class methods (sınıf metotları), sınıf seviyesinde çalışan ve sınıf niteliklerine erişebilen özel metotlardır.
#✅ @classmethod dekoratörü ile tanımlanır.
#✅ İlk parametre olarak cls (class) alır.
#✅ Sınıf seviyesinde çalışır, instance (nesne) seviyesinde değil.
#✅ Sınıfın class attributes (sınıf nitelikleri) ile çalışmak için kullanılır.

# ------------------------------------------ CLASS CONSTRUCTORS KULLANIMI  ------------------------------------------ #
#📌 Class Method Tanımlama ve Kullanımı
class Araba:
    uretici_ulke = "Almanya"  # Class Attribute

    @classmethod
    def ulke_bilgisi(cls):
        return f"Bu aracın üretildiği ülke: {cls.uretici_ulke}"

print(Araba.ulke_bilgisi())  



#📌 Instance ve Class Method Farkı
class Araba:
    uretici_ulke = "Almanya"

    def __init__(self, marka):
        self.marka = marka

    def marka_bilgisi(self):  # Instance Method
        return f"Bu araba {self.marka} markadır."

    @classmethod
    def ulke_bilgisi(cls):  # Class Method
        return f"Bu araçların üretildiği ülke: {cls.uretici_ulke}"

# Nesne oluşturalım
araba1 = Araba("BMW")
print(araba1.marka_bilgisi())  # Instance Method
print(Araba.ulke_bilgisi())  # Class Method



#📌 Class Methods Kullanım Alanları (Sınıf Niteliklerini Güncelleme)
class Ogrenci:
    toplam_ogrenci = 0  # Class Attribute

    def __init__(self, ad):
        self.ad = ad
        Ogrenci.toplam_ogrenci += 1

    @classmethod
    def ogrenci_sayisini_guncelle(cls, yeni_sayi):
        cls.toplam_ogrenci = yeni_sayi

# Yeni öğrenciler ekleyelim
ogr1 = Ogrenci("Ali")
ogr2 = Ogrenci("Ayşe")

print(Ogrenci.toplam_ogrenci)

# Sınıf metodunu kullanarak güncelleyelim
Ogrenci.ogrenci_sayisini_guncelle(100)

print(Ogrenci.toplam_ogrenci)



#📌 Class Methods Kullanım Alanları (Doğum yılından yaş hesaplama)
from datetime import date
class Kisi:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    @classmethod
    def dogum_yili_ile(cls, ad, dogum_yili):
        yas = date.today().year - dogum_yili
        return cls(ad, yas)

# Normal nesne oluşturma
kisi1 = Kisi("Ali", 30)
print(kisi1.ad, kisi1.yas)  # Çıktı: Ali 30

# Class method kullanarak nesne oluşturma
kisi2 = Kisi.dogum_yili_ile("Veli", 1995)
print(kisi2.ad, kisi2.yas)  # Çıktı: Veli 29



#📌 Class Methods Kullanım Alanları (JSON verisinden nesne oluşturma)
import json

class Ogrenci:
    def __init__(self, ad, not_ort):
        self.ad = ad
        self.not_ort = not_ort

    @classmethod
    def json_oku(cls, json_verisi):
        data = json.loads(json_verisi)
        return cls(data["ad"], data["not_ort"])

# JSON formatındaki veri
json_verisi = '{"ad": "Mehmet", "not_ort": 85}'

# Class method ile nesne oluşturma
ogrenci = Ogrenci.json_oku(json_verisi)
print(ogrenci.ad, ogrenci.not_ort)  
