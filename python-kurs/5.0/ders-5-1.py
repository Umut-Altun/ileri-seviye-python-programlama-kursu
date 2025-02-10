#5️⃣.1️⃣ Fonksiyonları Parametre Olarak Gönderme
#✅ Fonksiyonlar, başka fonksiyonlara parametre olarak gönderilebilir. 
#✅ Bu sayede, fonksiyonların daha esnek hale gelmesini sağlayarak, kodun tekrarını engeller ve fonksiyonel programlamayı destekler.

# ----------------------------------- FONKSİYONLARI PARAMAETRE GÖNDERME KULLANIMI  ---------------------------------- #
#📌 Fonksiyonları Parametre Olarak Kullanma Mantığı
def selamla(isim):
    return f"Merhaba {isim}!"

def islem_yap(fonksiyon, isim):
    return fonksiyon(isim)                                  # Fonksiyon çağrılıyor

sonuc = islem_yap(selamla, "Ahmet")  
print(sonuc)  



#📌 Yüksek Mertebe Fonksiyonlar (Higher-Order Functions)
def toplama(a, b):
    return a + b

def carpma(a, b):
    return a * b

def hesapla(fonksiyon, x, y):
    return fonksiyon(x, y)                                  # Parametre olarak gelen fonksiyon çalıştırılıyor

print(hesapla(toplama, 10, 5))  # 15
print(hesapla(carpma, 10, 5))  # 50



#📌  Gerçek Hayatta Kullanımı
def cift_sayilar(sayi):
    return sayi % 2 == 0                                    # Çift sayı mı?

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cift_sonuc = list(filter(cift_sayilar, sayilar))  
print(cift_sonuc) 




