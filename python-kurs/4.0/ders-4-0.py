#4️⃣.0️⃣ Nesne Yönelimli Programlama (OOP) Nedir?
#✅ Nesne Yönelimli Programlama, yazılımın daha modüler, okunaklı ve yönetilebilir olmasını sağlayan bir program yapısdır. 
#✅ OOP'de her şey bir nesne (object) olarak ele alınır.
#✅ OOP ile kod tekrarını azaltabilir, sistemleri daha iyi organize edebilir ve esnek yazılımlar geliştirebiliriz.

#📕 OOP, 4 temel kavrama dayanır:
#🥇 Sınıflar (Class): Nesnelerin bir şablonudur.
#🥈 Nesneler (Objects): Sınıflardan türetilen gerçek örneklerdir.
#🥉 Öznitelikler (Attributes): Nesnelerin sahip olduğu veriler (örneğin bir arabanın rengi, modeli vb.).
#🏅 Metodlar (Methods): Nesnelerin yapabildiği işlevler (örneğin bir arabanın hızlanması, fren yapması vb.).


#📕 OOP, daha güçlü yazılımlar oluşturmak için dört temel prensibe dayanır:
#🥇 Encapsulation (Kapsülleme): Verileri dışarıdan erişime kapatmak ve güvenliği sağlamak için kullanılır.
#🥈 Inheritance (Kalıtım): Bir sınıfın (parent class) özelliklerini başka bir sınıfa (child class) aktarmak için kullanılır.
#🥉 Polymorphism (Çok Biçimlilik): Aynı metodu farklı sınıflarda farklı şekillerde kullanmamızı sağlar.
#🏅 Abstraction (Soyutlama): Gereksiz detayları gizleyerek sadece önemli özellikleri gösterir.

# -------------------------------------------- PYTHONDA OOP KULLANIMI  ---------------------------------------------- #
# Bir Araba sınıfı oluşturuyoruz
class Araba:
    def __init__(self, marka, model, renk):
        self.marka = marka  # Arabanın markası
        self.model = model  # Arabanın modeli
        self.renk = renk    # Arabanın rengi

    def bilgi_goster(self):
        return f"{self.renk} renkli {self.marka} {self.model}"

# Nesne (Object) oluşturuyoruz
araba1 = Araba("Toyota", "Corolla", "Kırmızı")
araba2 = Araba("BMW", "M3", "Mavi")

# Nesnelerin bilgilerini yazdıralım
print(araba1.bilgi_goster())  # Çıktı: Kırmızı renkli Toyota Corolla
print(araba2.bilgi_goster())  # Çıktı: Mavi renkli BMW M3


# Bir Kullanici sınıfı oluşturuyoruz
class Kullanici:
    def __init__(self, ad, email):
        self.ad = ad
        self.email = email

    def giris_yap(self):
        return f"{self.ad} adlı kullanıcı giriş yaptı!"

# Kullanıcı nesnesi oluşturuyoruz
kullanici1 = Kullanici("Ahmet", "ahmet@gmail.com")

# Kullanıcı giriş yapıyor
print(kullanici1.giris_yap())  # Çıktı: Ahmet adlı kullanıcı giriş yaptı!

