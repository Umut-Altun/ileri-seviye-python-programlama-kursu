#5️⃣.0️⃣ İç İçe Fonksiyon Kullanımı - Fonksiyondan Geriye Fonksiyon Döndürme 
#✅ İç içe fonksiyonlar, bir fonksiyonun içinde başka bir fonksiyon tanımlanmasıdır. 
#✅ Bu yapıyı kullanarak, fonksiyonlar arasında kapsülleme ve daha temiz kod yazabiliriz. 
#✅ İç fonksiyon, yalnızca dış fonksiyon içinde erişilebilir.

# ------------------------------------------- İÇ İÇE FONKSİYON KULLANIMI  ----------------------------------------- #
# 📌 İç İçe Fonksiyon Nedir?
def dis_fonksiyon():
    print("Dış fonksiyon çalıştı.")

    def ic_fonksiyon():
        print("İç fonksiyon çalıştı.")

    ic_fonksiyon()   # İç fonksiyonu çağırıyoruz

dis_fonksiyon()   # İç fonksiyon, sadece dış fonksiyonun içinde çalışır.



#📌 İç Fonksiyonun Kapsamı (Scope)
def selamla(isim):
    def mesaj():
        print(f"Merhaba {isim}, hoş geldin!")   # Dış değişkene erişim var
    mesaj()

selamla("Ali")   # İç fonksiyon, dış fonksiyonun değişkenlerine erişebilir!



#📌 Closure (Kapanış) Fonksiyonları
def carpma_islemi(sayi1):
    def carp(sayi2):
        return sayi1 * sayi2  # Dış fonksiyonun değişkenini saklıyor
    return carp   # İç fonksiyonu döndürüyoruz

carp_ile_5 = carpma_islemi(5) 
print(carp_ile_5(3))
print(carp_ile_5(10))



#📌 İç İçe Fonksiyonlarla Dinamik Fonksiyonlar Oluşturma
def hesap_makinesi(islem):
    def toplama(a, b):
        return a + b

    def cikarma(a, b):
        return a - b

    if islem == "toplama":
        return toplama   # İç fonksiyonu döndür
    elif islem == "cikarma":
        return cikarma   # İç fonksiyonu döndür

topla = hesap_makinesi("toplama")
cikar = hesap_makinesi("cikarma")

print(topla(10, 5))
print(cikar(10, 5)) 



#📌 Gerçek Hayat Örneği: Kullanıcı Yetkilendirme
def yetki_kontrolu(yetkili_kullanici):
    def giris(kullanici):
        if kullanici == yetkili_kullanici:
            print("Giriş başarılı!")
        else:
            print("Erişim reddedildi!")
    return giris

admin_giris = yetki_kontrolu("admin")

admin_giris("admin") 
admin_giris("misafir")
