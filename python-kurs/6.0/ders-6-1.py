#6️⃣.1️⃣ Meta Karakterleri
#✅ Meta karakterler, düzenli ifadelerde kullanılan özel karakterlerdir. 
#✅ Bu karakterler, basit eşleşmelerin ötesine geçmemizi sağlar ve daha güçlü arama, değiştirme ve doğrulama 
#  işlemlerine olanak tanır. 
#✅ Meta karakterler, özel anlamlar taşır ve sadece belirli durumlarda kullanılırlar.

#✅ Yaygın Olarak Kullanılan Meta Karakterler
#*** ^ karakteri, bir deseni yalnızca satır başında eşleştirir.
#*** $ karakteri, bir deseni yalnızca satır sonunda eşleştirir.
#*** . karakteri, herhangi bir tek karakteri eşleştirir, ancak yeni satır (\n) karakterini eşleştirmez.
#*** [] karakterleri, belirtilen karakterlerden herhangi birini eşleştirir.
#*** | operatörü, bir desenin alternatiflerini belirtir. Yani, bir desenin biri ya da diğerini eşleştirir.
#*** () karakteri, bir deseni gruplamak için kullanılır. Bu sayede, daha sonra grup işlemleri yapılabilir.
#*** \ karakteri, özel karakterlerin (örneğin, nokta, yıldız vs.) normal karakter olarak kullanılmasını sağlar.

# ------------------------------------------ META KARAKTER KULLANIMI  -------------------------------------------- #
import re

#📌 ^ (Satır Başı)
metin = "Merhaba Dünya"
result = re.match(r"^Merhaba", metin)   #"Merhaba" kelimesini sadece satır başında arar.
if result:
    print("Satır başında 'Merhaba' var.")


#📌 $ (Satır Sonu)
metin = "Dünya"
result = re.search(r"Dünya$", metin)  #"Dünya" kelimesini yalnızca satır sonunda arar.
if result:
    print("Satır sonunda 'Dünya' var.")


#📌 . (Nokta)
metin = "acb"
result = re.match(r"a.b", metin)   # "a" ve "b" arasındaki herhangi bir karakteri eşleştirir.
if result:
    print("Eşleşme bulundu.")


#📌 [] (Karakter Kümesi)
metin = "Python"
result = re.match(r"[aeiou]", metin)  # bir sesli harfi arar.
if result:
    print("İlk harf bir sesli harf.")


#📌 | (Veya/Alternatif)
metin = "Java Python"
result = re.search(r"Python|Java", metin)   #"Python" ya da "Java" kelimesini arar.
if result:
    print("Eşleşme bulundu.")


#📌 () (Gruplama)
metin = "ababab"
result = re.match(r"(ab)+", metin)    #"ab" dizisinin bir veya daha fazla tekrarını arar.
if result:
    print("Grup eşleşmesi bulundu.")


#📌 \ (Kaçış Karakteri)
metin = "Python."
result = re.match(r"Python\.", metin)    #bir nokta karakterini eşleştirir.
if result:
    print("Eşleşme bulundu.")






























