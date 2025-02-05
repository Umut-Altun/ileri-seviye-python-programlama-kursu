#4️⃣.7️⃣ Properties (Özellikler)
#✅ Python'da property kavramı, bir nesne değişkenini (attribute) yönetmek için kullanılır.
#✅ Getter ve Setter metodları sayesinde, bir değişkenin değerini alırken veya değiştirirken özel kontroller yapabiliriz.
#✅ Doğrudan değişken erişimini kontrol etmek için
#✅ Veri doğrulama ve filtreleme işlemleri yapmak için
#✅ Hataları önlemek ve güvenli kod yazmak için
#✅ Python'da @property dekoratörü ile getter, setter ve deleter metodları oluşturabiliriz.

# -------------------------------------------- PROPERTİES KULLANIMI  --------------------------------------------- #
#📌 Neden Kullanırız?
class Araba:
    def __init__(self, hiz):
        self.hiz = hiz  # Doğrudan değişken ataması

araba = Araba(120)
print(araba.hiz)  # Çıktı: 120
araba.hiz = -50  # Negatif hız mantıklı değil!
print(araba.hiz)  # Çıktı: -50 (Hatalı!)



#📌 Örnek: Property ile güvenli erişim
class Araba:
    def __init__(self, hiz):
        self._hiz = hiz  # Özel değişken (_hiz)

    @property
    def hiz(self):  # Getter metodu
        return self._hiz

    @hiz.setter
    def hiz(self, yeni_hiz):  # Setter metodu
        if yeni_hiz < 0:
            print("Hız negatif olamaz!")
        else:
            self._hiz = yeni_hiz

    @hiz.deleter
    def hiz(self):  # Deleter metodu
        print("Hız bilgisi silindi!")
        del self._hiz

# Kullanım
araba = Araba(120)
print(araba.hiz)  # Çıktı: 120

araba.hiz = -50   # Çıktı: Hız negatif olamaz!
print(araba.hiz)  # Çıktı: 120 (Hız değişmedi!)

del araba.hiz     # Çıktı: Hız bilgisi silindi!



#📌 Uygulama: Çalışan Bilgi Sistemi
class Calisan:
    def __init__(self, ad, maas):
        self._ad = ad
        self._maas = maas

    @property
    def ad(self):
        return self._ad

    @ad.setter
    def ad(self, yeni_ad):
        if len(yeni_ad) < 2:
            print("İsim en az 2 karakter olmalıdır!")
        else:
            self._ad = yeni_ad

    @property
    def maas(self):
        return self._maas

    @maas.setter
    def maas(self, yeni_maas):
        if yeni_maas < 0:
            print("Maaş negatif olamaz!")
        else:
            self._maas = yeni_maas

    @maas.deleter
    def maas(self):
        print("Maaş bilgisi silindi!")
        del self._maas

# Kullanım
calisan1 = Calisan("Ahmet", 50000)

print(calisan1.ad)   # Çıktı: Ahmet
print(calisan1.maas) # Çıktı: 50000

calisan1.maas = -1000  # Çıktı: Maaş negatif olamaz!
calisan1.ad = "A"      # Çıktı: İsim en az 2 karakter olmalıdır!

del calisan1.maas      # Çıktı: Maaş bilgisi silindi!











