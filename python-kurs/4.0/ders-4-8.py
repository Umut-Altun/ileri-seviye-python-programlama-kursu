#4️⃣.8️⃣ Python'da special methods (özel metotlar) veya dunder methods (double underscore methods) olarak adlandırılan
#  metotlar, __init__, __str__, __len__ gibi çift alt çizgi ile başlayan metotlardır.
#✅ Bu metotlar, sınıfların davranışlarını değiştirmemizi sağlar ve nesnelerin farklı şekillerde kullanılmasına imkan tanır.
#✅ __init__ → Nesne oluşturulurken çağrılır.
#✅ __str__ → Nesne print() ile yazdırıldığında çağrılır.
#✅ __len__ → len(obj) çağrıldığında çalışır.
#✅ __add__ → + operatörü ile nesneleri toplamak için kullanılır.

# ------------------------------------------- SPECİAL METHODS KULLANIMI  ----------------------------------------- #
#📌 __init__ (Kurucu Metot)
class Kitap:
    def __init__(self, ad, yazar, sayfa):
        self.ad = ad
        self.yazar = yazar
        self.sayfa = sayfa

kitap1 = Kitap("1984", "George Orwell", 328)
print(kitap1.ad)  # Çıktı: 1984



# 📌 __str__ (Nesneyi Kullanıcı Dostu Yazdırma)
class Kitap:
    def __init__(self, ad, yazar, sayfa):
        self.ad = ad
        self.yazar = yazar
        self.sayfa = sayfa

    def __str__(self):
        return f"{self.ad} - {self.yazar}, {self.sayfa} sayfa"

kitap1 = Kitap("1984", "George Orwell", 328)
print(kitap1)  # Çıktı: 1984 - George Orwell, 328 sayfa



# 📌 __repr__ (Nesneyi Temsili Olarak Yazdırma)
class Kitap:
    def __init__(self, ad, yazar, sayfa):
        self.ad = ad
        self.yazar = yazar
        self.sayfa = sayfa

    def __repr__(self):
        return f"Kitap('{self.ad}', '{self.yazar}', {self.sayfa})"

kitap1 = Kitap("1984", "George Orwell", 328)
print(repr(kitap1))  
# Çıktı: Kitap('1984', 'George Orwell', 328)



# 📌 __len__ (Nesne Uzunluğunu Döndürme)
class Kitap:
    def __init__(self, ad, yazar, sayfa):
        self.ad = ad
        self.yazar = yazar
        self.sayfa = sayfa

    def __len__(self):
        return self.sayfa

kitap1 = Kitap("1984", "George Orwell", 328)
print(len(kitap1))  # Çıktı: 328



# 📌 __del__ (Nesne Silindiğinde Çalışan Metot)
class Kitap:
    def __init__(self, ad, yazar):
        self.ad = ad
        self.yazar = yazar

    def __del__(self):
        print(f"{self.ad} kitabı silindi!")

kitap1 = Kitap("1984", "George Orwell")
del kitap1  # Çıktı: 1984 kitabı silindi!



# 📌 Matematiksel Operatörlerle Özel Metotlar
# Operatör	    Metot
#   +	        __add__(self, other)
#   -	        __sub__(self, other)
#   *	        __mul__(self, other)
#   /	        __truediv__(self, other)
#   //	        __floordiv__(self, other)



# 📌 Karşılaştırma Metotları
# Operatör	    Metot
#   ==	        __eq__(self, other)
#   !=	        __ne__(self, other)
#   <	        __lt__(self, other)
#   <=	        __le__(self, other)
#   >	        __gt__(self, other)
#   >=	        __ge__(self, other)