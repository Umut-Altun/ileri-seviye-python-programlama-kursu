#4️⃣.3️⃣ Class Attributes (Sınıf Nitelikleri)
#✅ Class attributes (sınıf nitelikleri), bir sınıfa ait ortak değişkenlerdir ve tüm nesneler tarafından paylaşılır.
#✅ Sınıf seviyesinde tanımlanır (Metotların dışında).
#✅ Tüm nesneler tarafından paylaşılır (Her nesne için ayrı bir kopya oluşturulmaz).
#✅ Nesneye değil, sınıfa aittir.


#📕 2. Class Attribute ile Instance Attribute Arasındaki Fark
# Özellik---------------ClassAttribute------------------Instance Attribute
# Tanımlandığı Yer	    Sınıf içinde, metodun dışında	__init__ metodunun içinde
# Bağlı Olduğu Yer	    Tüm nesnelere ortak	            Sadece ilgili nesneye ait
# Güncellenirse	        Tüm nesneleri etkiler	        Sadece o nesneyi etkiler

# ------------------------------------------ CLASS ATTRİBUTES KULLANIMI  ------------------------------------------ #
#📌 Class Attribute Nasıl Tanımlanır? 
class Araba:
    # Class Attribute
    tekerlek_sayisi = 4  

    def __init__(self, marka, model):
        # Instance Attributes
        self.marka = marka  
        self.model = model  

# Nesne oluşturalım
araba1 = Araba("BMW", "X5")
araba2 = Araba("Mercedes", "C200")
print(araba1.tekerlek_sayisi)  
print(araba2.tekerlek_sayisi)  

# Eğer sınıf üzerinden değiştirirsek, tüm nesneleri etkiler:
Araba.tekerlek_sayisi = 6
print(araba1.tekerlek_sayisi) 
print(araba2.tekerlek_sayisi) 

# Eğer bir nesne üzerinden değiştirilirse, sadece o nesne için değişir:
araba1.tekerlek_sayisi = 8  
print(araba1.tekerlek_sayisi)  
print(araba2.tekerlek_sayisi)  



#📌 Örnek: Class Attribute Kullanım Alanları
class Araba:
    uretici_ulke = "Almanya"  # Class Attribute

    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

araba1 = Araba("BMW", "X5")
araba2 = Araba("Mercedes", "C200")

print(araba1.uretici_ulke) 
print(araba2.uretici_ulke)  



class Ogrenci:
    toplam_ogrenci = 0  # Class Attribute

    def __init__(self, ad):
        self.ad = ad
        Ogrenci.toplam_ogrenci += 1  # Her yeni nesnede artır

ogr1 = Ogrenci("Ali")
ogr2 = Ogrenci("Ayşe")
ogr3 = Ogrenci("Mehmet")

print(f"Toplam öğrenci sayısı: {Ogrenci.toplam_ogrenci}")  



















