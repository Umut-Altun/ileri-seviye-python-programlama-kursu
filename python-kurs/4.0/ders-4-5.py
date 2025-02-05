#4️⃣.5️⃣ Uygulama Dersi: Personel Yönetim Sistemi (PYS)
#✅ Bu uygulamada, öğrendiğimiz Class Methods (Sınıf Metotları) konusunu Personel Yönetim Sistemi (PYS) üzerinde kullanacağız.
#✅ Personel ekleme
#✅ Toplam personel sayısını takip etme
#✅ Farklı şekillerde nesne oluşturma (Alternatif Constructor kullanımı)

# ----------------------------------------- Personel Yönetim Sistemi (PYS) ----------------------------------------- #
#📌 Personel Sınıfını Tanımlayalım
class Personel:
    toplam_personel = 0  # Class Attribute
    
    # %10 Maaş Zammı Uygulayan Class Method
    zam_orani = 1.10  

    def __init__(self, ad, departman, maas):
        self.ad = ad
        self.departman = departman
        self.maas = maas
        Personel.toplam_personel += 1  # Her yeni personel eklendiğinde artır

    def bilgiler(self):  # Instance Method
        return f"Ad: {self.ad}, Departman: {self.departman}, Maaş: {self.maas}"

    @classmethod
    def toplam_personel_sayisi(cls):  # Class Method
        return f"Şirkette toplam {cls.toplam_personel} personel var."
    
    # Class Method ile Farklı Nesne Oluşturma
    @classmethod  
    def string_ile_olustur(cls, bilgi_str):
        ad, departman, maas = bilgi_str.split(",")
        return cls(ad, departman, int(maas))  # Yeni nesne döndür

    # Maaş Zammı Uygulayan Class Method
    @classmethod
    def toplu_zam(cls, yeni_oran):
        cls.zam_orani = yeni_oran

p1 = Personel("Ali", "IT", 15000)
p2 = Personel("Ayşe", "Muhasebe", 12000)

print(p1.bilgiler())  
print(p2.bilgiler())  
print(Personel.toplam_personel_sayisi())  

# Class Method ile Farklı Nesne Oluşturma
p3 = Personel.string_ile_olustur("Mehmet,Satış,11000")
print(p3.bilgiler())   

# Maaş Zammı Uygulayan Class Method
print(f"Eski zam oranı: {Personel.zam_orani}")  
Personel.toplu_zam(1.15)
print(f"Yeni zam oranı: {Personel.zam_orani}")  




#📌 Uygulamayı Test Edelim
def menu():
    while True:
        print("\nPersonel Yönetim Sistemi")
        print("1- Yeni Personel Ekle")
        print("2- Toplam Personel Sayısını Gör")
        print("3- Tüm Personelleri Listele")
        print("4- Zam Oranını Güncelle")
        print("5- Çıkış")

        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            veri = input("Personel Bilgileri (Ad,Departman,Maaş): ")
            yeni_personel = Personel.string_ile_olustur(veri)
            print(yeni_personel)
            personeller.append(yeni_personel)
            print(f"{yeni_personel.ad} eklendi.")

        elif secim == "2":
            print(Personel.toplam_personel_sayisi())

        elif secim == "3":
            for p in personeller:
                print(p.bilgiler())

        elif secim == "4":
            oran = float(input("Yeni zam oranını girin (örnek: 1.20): "))
            Personel.toplu_zam(oran)
            print("Zam oranı güncellendi.")

        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim!")

# Personel listesi
personeller = []

# Menü başlat
menu()
