#4️⃣.6️⃣ Kalıtım
#✅ Kalıtım (inheritance), bir sınıfın (class) başka bir sınıftan özellikleri ve metotları miras almasıdır.
#✅ Bu sayede kod tekrarını önler, mevcut kodları genişletmemizi sağlar.
#✅ super() fonksiyonu ile üst sınıfın metodunu çağırıp kullanabiliriz
#✅ Metotları ezerek (override) farklı çıktılar alabiliriz

# ----------------------------------------------- KALITIM KULLANIMI  --------------------------------------------- #
#📌Kalıtım (Inheritance) Nedir?
class Insan:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def tanit(self):
        return f"Benim adım {self.ad}, yaşım {self.yas}."

# Öğrenci sınıfı Insan sınıfından miras alıyor
class Ogrenci(Insan):
    def __init__(self, ad, yas, okul):
        super().__init__(ad, yas)  # Üst sınıfın init fonksiyonunu çağır
        self.okul = okul

    def tanit(self):
        return f"Benim adım {self.ad}, yaşım {self.yas} ve {self.okul} öğrencisiyim."

# Kullanım
ogrenci1 = Ogrenci("Ali", 20, "İTÜ")
print(ogrenci1.tanit())  

#📌 Kalıtımda Metot ve Özellik Değiştirme (Overriding)
class Hayvan:
    def ses_cikar(self):
        return "Bilinmeyen ses"

class Kedi(Hayvan):
    def ses_cikar(self):  # Üst sınıfın metodunu eziyoruz
        return "Miyav!"

class Kopek(Hayvan):
    def ses_cikar(self):
        return "Hav hav!"

# Kullanım
kedi1 = Kedi()
kopek1 = Kopek()

print(kedi1.ses_cikar()) 
print(kopek1.ses_cikar()) 



#📌 Çok Seviyeli Kalıtım (Multilevel Inheritance)
class Canli:
    def yasam_bilgisi(self):
        return "Ben bir canlıyım."

class Memeli(Canli):
    def beslenme(self):
        return "Memeliler doğurur ve süt ile besler."

class Insan(Memeli):
    def dusunme(self):
        return "İnsanlar düşünme yeteneğine sahiptir."

# Kullanım
insan1 = Insan()
print(insan1.yasam_bilgisi())  # Çıktı: Ben bir canlıyım.
print(insan1.beslenme())       # Çıktı: Memeliler doğurur ve süt ile besler.
print(insan1.dusunme())        # Çıktı: İnsanlar düşünme yeteneğine sahiptir.


#📌 Uygulama: Şirket Hiyerarşisi Simülasyonu
class Personel:
    def __init__(self, ad, departman, maas):
        self.ad = ad
        self.departman = departman
        self.maas = maas

    def bilgiler(self):
        return f"Ad: {self.ad}, Departman: {self.departman}, Maaş: {self.maas} TL"

class Yonetici(Personel):
    def __init__(self, ad, departman, maas, ekip_sayisi):
        super().__init__(ad, departman, maas)
        self.ekip_sayisi = ekip_sayisi

    def bilgiler(self):  # Metodu ezdik
        return f"Ad: {self.ad}, Departman: {self.departman}, Maaş: {self.maas} TL, Ekip: {self.ekip_sayisi} kişi"

    def zam_yap(self, zam_miktari):
        self.maas += zam_miktari
        return f"{self.ad}'nin yeni maaşı: {self.maas} TL"

class Muhendis(Personel):
    def __init__(self, ad, departman, maas, uzmanlik):
        super().__init__(ad, departman, maas)
        self.uzmanlik = uzmanlik

    def bilgiler(self):
        return f"Ad: {self.ad}, Departman: {self.departman}, Maaş: {self.maas} TL, Uzmanlık: {self.uzmanlik}"

# Kullanım
yonetici1 = Yonetici("Ahmet", "Yönetim", 30000, 10)
muhendis1 = Muhendis("Zeynep", "Mühendislik", 20000, "Yapay Zeka")

print(yonetici1.bilgiler())  
# Çıktı: Ad: Ahmet, Departman: Yönetim, Maaş: 30000 TL, Ekip: 10 kişi

print(muhendis1.bilgiler())  
# Çıktı: Ad: Zeynep, Departman: Mühendislik, Maaş: 20000 TL, Uzmanlık: Yapay Zeka

print(yonetici1.zam_yap(5000))  
# Çıktı: Ahmet'in yeni maaşı: 35000 TL
