#5️⃣.2️⃣ Kullanıcı Yönetim Sistemi
#✅ Kullanıcıları ekleyip silebileceğimiz, yaşlarına göre sıralayabileceğimiz ve adlarına göre filtreleyebileceğimiz
#  bir sistem kuracağız. Fonksiyonları parametre olarak geçme, fonksiyonlardan fonksiyon döndürme gibi ileri seviye
#  fonksiyon özelliklerini kullanacağız.

# ----------------------------------------- KULLANICI YÖNETİM SİSTEMİ  -------------------------------------------- #
#📌 İlk adım olarak, kullanıcı bilgilerini tutacak bir sınıf oluşturuyoruz.
class Kullanici:
    def __init__(self, id, ad, yas, email):
        self.id = id  # Kullanıcının ID'si
        self.ad = ad  # Kullanıcının adı
        self.yas = yas  # Kullanıcının yaşı
        self.email = email  # Kullanıcının e-posta adresi

    def __str__(self):
        return f"Kullanıcı(ID: {self.id}, Ad: {self.ad}, Yaş: {self.yas}, E-posta: {self.email})"



#📌 Bu sınıf, kullanıcıları yönetmek için gerekli işlemleri sağlayacak.
class KullaniciYonetimSistemi:
    def __init__(self):
        self.kullanicilar = []  # Kullanıcıları tutan liste

    def kullanici_ekle(self, kullanici):
        self.kullanicilar.append(kullanici)  # Yeni kullanıcıyı ekler

    def kullanici_sil(self, kullanici_id):
        # Kullanıcıyı ID'ye göre siler
        self.kullanicilar = [k for k in self.kullanicilar if k.id != kullanici_id]

    def kullanici_listele(self):
        # Kullanıcıları liste halinde döndürür
        return [str(k) for k in self.kullanicilar]



#📌 Kullanıcıları Sıralama ve Filtreleme Fonksiyonları
def yas_ye_gore_sirala(kullanici):
    return f"{kullanici.ad}: {kullanici.yas}"  # Kullanıcıların yaşına göre sıralama fonksiyonu

def isim_ile_filtrele(kullanici, isim):
    return kullanici.ad == isim  # Kullanıcı adını kontrol eder

def kullanici_islemleri(kullanicilar, islemi_yap):
    return [islemi_yap(k) for k in kullanicilar]  # Kullanıcılar üzerinde işlemi uygular



#📌 Şimdi tüm bu bileşenleri birleştirelim.
def ana_menu():
    # Kullanıcı yönetim sistemi nesnesini oluşturuyoruz
    kullanici_yonetim = KullaniciYonetimSistemi()

    # Kullanıcılar ekliyoruz
    kullanici_yonetim.kullanici_ekle(Kullanici(1, "Ahmet", 30, "ahmet@example.com"))
    kullanici_yonetim.kullanici_ekle(Kullanici(2, "Mehmet", 25, "mehmet@example.com"))
    kullanici_yonetim.kullanici_ekle(Kullanici(3, "Zeynep", 35, "zeynep@example.com"))
    kullanici_yonetim.kullanici_ekle(Kullanici(4, "Elif", 28, "elif@example.com"))

    # Tüm kullanıcıları listele
    print("***** Tüm Kullanıcılar: *****")
    for kullanici in kullanici_yonetim.kullanici_listele():
        print(kullanici)

    # Yaşa göre sıralama
    print("\n***** Yaşa Göre Sıralı Kullanıcılar: *****")
    sirali_kullanicilar = kullanici_islemleri(kullanici_yonetim.kullanicilar, yas_ye_gore_sirala)
    for kullanici in sirali_kullanicilar:
        print(kullanici)

    # Ahmet adını taşıyan kullanıcıları filtrele
    print("\n***** Filtrelenmiş Kullanıcılar (Ahmet): *****")
    ahmet_kullanicilari = list(filter(lambda k: isim_ile_filtrele(k, "Ahmet"), kullanici_yonetim.kullanicilar))
    for kullanici in ahmet_kullanicilari:
        print(kullanici)

    # Kullanıcı silme
    print("\n********** Yeni Kullanıcı Listesi: *****")
    kullanici_yonetim.kullanici_sil(2)  # Mehmet'i sil
    for kullanici in kullanici_yonetim.kullanici_listele():
        print(kullanici)

if __name__ == "__main__":
    ana_menu()
