#4️⃣.1️⃣ Class Constructors (Yapıcı Metotlar - __init__)
#✅ Bir sınıf (class) nesne (object) oluştururken başlangıç değerlerini ayarlamak için yapıcı metotlar kullanılır. 
#✅ Python’da bu metot, __init__ (init fonksiyonu) olarak adlandırılır.
#✅ Nesne oluşturulduğunda ilk değerleri atayabiliriz
#✅ Sınıfın her nesnesi için özelleştirilmiş başlangıç değerleri tanımlayabiliriz.
#✅ Kod tekrarını azaltarak, daha modüler ve düzenli hale getirebiliriz.

# ------------------------------------------ CLASS CONSTRUCTORS KULLANIMI  ------------------------------------------ #
# 📌 __init__ Metodu Olmadan Sınıf Kullanımı
class Araba:
    pass

araba1 = Araba()
araba1.marka = "BMW"
araba1.model = "M3"

print(araba1.marka, araba1.model)



#📌 Yapıcı Metot (__init__) Nasıl Tanımlanır?
class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model 

# Yeni nesneler (object) oluşturalım
arac_1 = Araba("BMW", "m3")
arac_2 = Araba("Toyotoa", "Corolla")

# Nesne bilgilerini yazdıralım
print(arac_1.marka, arac_1.model) 
print(arac_2.marka, arac_2.model) 



#📌 Varsayılan (Default) Değerlerle Yapıcı Metot Kullanımı
class Calisan:
    def __init__(self, isim, maas=5000):
        self.isim = isim
        self.maas = maas  # Varsayılan olarak 5000 atanır

# Farklı nesneler oluşturalım
calisan1 = Calisan("Mehmet", 7000)
calisan2 = Calisan("Ayşe")  # Maaş belirtilmezse varsayılan 5000 olur

print(calisan1.isim, calisan1.maas)  # Çıktı: Mehmet 7000
print(calisan2.isim, calisan2.maas)  # Çıktı: Ayşe 5000



#📌 Yapıcı Metotta Hesaplama ve İşlem Yapma
class Kullanici:
    def __init__(self, ad, sifre):
        self.ad = ad
        self.sifre = self.sifre_kodla(sifre)  # Şifreyi şifrele

    def sifre_kodla(self, sifre):
        return "*" * len(sifre)  # Basit bir gizleme (Şifre uzunluğu kadar * koyar)

# Kullanıcı nesnesi oluşturalım
kullanici1 = Kullanici("Ali", "12345")

print(kullanici1.ad)  # Çıktı: Ali
print(kullanici1.sifre)  # Çıktı: *****



#📌 Yapıcı Metodu Kullanarak Daha Karmaşık Bir Örnek
class Kitap:
    def __init__(self, ad, yazar, sayfa_sayisi):
        self.ad = ad
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi

    def bilgi_goster(self):
        return f"Kitap: {self.ad} | Yazar: {self.yazar} | Sayfa: {self.sayfa_sayisi}"

# Kitap nesneleri oluşturalım
kitap1 = Kitap("1984", "George Orwell", 328)
kitap2 = Kitap("Savaş ve Barış", "Tolstoy", 1225)

print(kitap1.bilgi_goster())
print(kitap2.bilgi_goster())




