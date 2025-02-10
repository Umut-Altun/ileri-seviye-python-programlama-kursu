#6️⃣.0️⃣ Regular Expressions (Düzenli İfadeler) 
#✅ Düzenli ifadeler ("regex"), metinleri belirli desenlere göre eşleştirmek ve işlemek için kullanılan araçtır.
#✅ Regex kullanarak, metin içinde belirli bir desen aramak, eşleşmeleri bulmak, metinleri değiştirmek veya
#  doğrulamak çok daha kolay hale gelir.
#✅ Düzenli ifadeler, karakterlerin ve sembollerinin özel anlamlar taşıdığı bir dil kullanır. Bu sembollerle, 
# aradığımız deseni tanımlarız.
#✅ Python, düzenli ifadeleri kullanabilmek için "re" adlı bir modül sunar. 

#✅ Temel Regex Sembolleri
#*** . (nokta): Herhangi bir karakteri temsil eder (yeni satır hariç).
#*** \d: Bir rakamı temsil eder (0-9).
#*** \D: Bir rakam olmayan karakteri temsil eder.
#*** \w: Bir kelime karakterini temsil eder (alfabetik karakterler, rakamlar ve alt çizgi _).
#*** \W: Bir kelime olmayan karakteri temsil eder.
#*** \s: Bir boşluk karakterini temsil eder (boşluk, tab, yeni satır, vb.).
#*** \S: Boşluk olmayan bir karakteri temsil eder.
#*** \b: Kelime sınırını temsil eder (başlangıç veya bitiş).
#*** ^: Desenin başında eşleşme yapılmasını sağlar.
#*** $: Desenin sonunda eşleşme yapılmasını sağlar.
#*** []: Karakter sınıfı tanımlar. Belirli bir karakter setinden birini seçer.
#*** (): Grup oluşturur. Deseni gruplamak ve işlem yapmak için kullanılır.
#*** |: Alternatifleri belirtir (veya).

# -------------------------------------- REGULAR EXPRESSİONS KULLANIMI  ----------------------------------------- #
#📌 re Modülünde Kullanılabilecek Fonksiyonlar

# re.match(): Bir desenin, bir metnin başında olup olmadığını kontrol eder. Eğer eşleşirse, eşleşen kısmı döner.
import re
result = re.match(r"Merhaba", "Merhaba Dünya")
if result:
    print("Eşleşme bulundu!")

# re.search(): Deseni, metnin herhangi bir yerinde arar. Eğer eşleşme bulursa, eşleşen kısmı döner.
result = re.search(r"Python", "Ben Python programlama dili öğreniyorum.")
if result:
    print("Eşleşme bulundu!")

# re.sub(): Deseni bulur ve belirtilen yeni metinle değiştirir.
result = re.sub(r"Python", "Java", "Ben Python öğreniyorum.")
print(result)  # "Ben Java öğreniyorum."




#📌 Örnekler ile Düzenli İfade Kullanımı
import re

def eposta_dogrula(eposta):
    desen = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(desen, eposta):
        print("Geçerli e-posta adresi")
    else:
        print("Geçersiz e-posta adresi")

eposta_dogrula("example@example.com")
eposta_dogrula("invalid-email")


def telefon_dogrula(telefon):
    desen = r"^\+?\d{1,3}?[-. ]?\(?\d{1,4}?\)?[-. ]?\d{1,4}[-. ]?\d{1,4}$"
    if re.match(desen, telefon):
        print("Geçerli telefon numarası")
    else:
        print("Geçersiz telefon numarası")

telefon_dogrula("+90 123 456 7890")
telefon_dogrula("12345")


def tarih_bul(text):
    desen = r"\d{4}-\d{2}-\d{2}"
    return re.findall(desen, text)

metin = "Rehber Yazılım; Bugünün Tarihi 2023-10-15, dün ise 2023-10-14 idi."
print(tarih_bul(metin)) 
