#4️⃣.9️⃣ Metaclass (Meta Sınıflar)
#✅ Python'da her şey bir nesnedir. Peki sınıflar da bir nesne mi?
#✅ Evet! Bir sınıf oluşturduğumuzda aslında bir nesne oluşturuyoruz.
#✅ Python'da her sınıfın bir metaclass'ı vardır ve bu metaclass, sınıfın nasıl oluşturulacağını belirler.
#✅ Metaclass, sınıfları oluşturan sınıftır.
#✅ Sınıflar, nesneler üretir.
#✅ Metaclass'lar, sınıfları üretir.

# --------------------------------------------- METACLASS KULLANIMI  --------------------------------------------- #
#📌 Python'da Sınıfların Çalışma Mantığı
class MyClass:
    pass

print(type(MyClass))  
# Çıktı: <class 'type'>



#📌 type Kullanarak Dinamik Sınıf Oluşturma
class NormalClass:
    x = 10

DynamicClass = type("DynamicClass", (), {"x": 10})

print(NormalClass.x)  # Çıktı: 10
print(DynamicClass.x)  # Çıktı: 10



#📌 Metaclass Oluşturma
class MyMeta(type):  
    def __new__(cls, name, bases, attrs):
        print(f"{name} sınıfı oluşturuluyor!")
        return super().__new__(cls, name, bases, attrs)

# Metaclass kullanarak sınıf tanımlama
class MyClass(metaclass=MyMeta):
    x = 10

# Çıktı: MyClass sınıfı oluşturuluyor!



#📌 Metaclass Kullanarak Sınıfları Otomatik Değiştirme
class UpperCaseMeta(type):
    def __new__(cls, name, bases, attrs):
        uppercase_attrs = {key.upper(): value for key, value in attrs.items()}
        return super().__new__(cls, name, bases, uppercase_attrs)

# Bu metaclass'ı kullanarak bir sınıf oluşturalım
class MyClass(metaclass=UpperCaseMeta):
    var1 = "Merhaba"
    var2 = 42

# Artık değişkenler büyük harfle tanımlandı
print(hasattr(MyClass, "var1"))  # Çıktı: False
print(hasattr(MyClass, "VAR1"))  # Çıktı: True
print(MyClass.VAR1)  # Çıktı: Merhaba
