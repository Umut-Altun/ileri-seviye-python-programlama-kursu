#4️⃣.2️⃣ Instance Methods
#✅ Instance methods, bir sınıfın örneği (nesnesi) üzerinde işlem yapabilen metotlardır.
#✅ Sınıfın içinde tanımlanır.
#✅ self parametresini kullanarak, nesneye ait verilere erişebilir.
#✅ Nesneye özgü işlemleri gerçekleştirmek için kullanılır.

# ------------------------------------------ INSTANCE METHODS KULLANIMI  ------------------------------------------ #
#📌 Instance Method Nasıl Tanımlanır? 
class Ogrenci:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas
    
    def bilgileri_goster(self):
        return f"Öğrenci Adı: {self.ad}, Yaşı: {self.yas}"

# Nesne oluşturalım
ogr1 = Ogrenci("Ali", 20)

# Instance method çağırma
print(ogr1.bilgileri_goster())  
# Çıktı: Öğrenci Adı: Ali, Yaşı: 20



#📌 Instance Method ile Nesne Özelliklerini Güncelleme
class Araba:
    def __init__(self, marka, hiz):
        self.marka = marka
        self.hiz = hiz
    
    def hiz_arttir(self, miktar):
        self.hiz += miktar
        return f"{self.marka} hızlandı! Yeni hız: {self.hiz} km/s"

# Nesne oluşturalım
araba1 = Araba("BMW", 100)

# Hızı artır
print(araba1.hiz_arttir(20))  
# Çıktı: BMW hızlandı! Yeni hız: 120 km/s



#📌 Instance Method Kullanarak Liste Yönetimi
class AlisverisSepeti:
    def __init__(self):
        self.urunler = []  # Boş bir liste
    
    def urun_ekle(self, urun):
        self.urunler.append(urun)
        return f"{urun} sepete eklendi."
    
    def urunleri_goster(self):
        return f"Sepetteki Ürünler: {', '.join(self.urunler)}"

# Nesne oluşturalım
sepet = AlisverisSepeti()

print(sepet.urun_ekle("Elma"))  # Çıktı: Elma sepete eklendi.
print(sepet.urun_ekle("Muz"))   # Çıktı: Muz sepete eklendi.
print(sepet.urunleri_goster())  # Çıktı: Sepetteki Ürünler: Elma, Muz



#📌 Örnek: Banka Hesabı Uygulaması
class BankaHesabi:
    def __init__(self, hesap_sahibi, bakiye=0):
        self.hesap_sahibi = hesap_sahibi
        self.bakiye = bakiye
    
    def para_yatir(self, miktar):
        self.bakiye += miktar
        return f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL"
    
    def para_cek(self, miktar):
        if miktar > self.bakiye:
            return "Yetersiz bakiye!"
        self.bakiye -= miktar
        return f"{miktar} TL çekildi. Kalan bakiye: {self.bakiye} TL"
    
    def hesap_bilgisi(self):
        return f"Hesap Sahibi: {self.hesap_sahibi}, Bakiye: {self.bakiye} TL"

# Nesne oluşturalım
hesap1 = BankaHesabi("Mehmet", 1000)

print(hesap1.para_yatir(500))  # Çıktı: 500 TL yatırıldı. Yeni bakiye: 1500 TL
print(hesap1.para_cek(700))    # Çıktı: 700 TL çekildi. Kalan bakiye: 800 TL
print(hesap1.hesap_bilgisi())  # Çıktı: Hesap Sahibi: Mehmet, Bakiye: 800 TL






