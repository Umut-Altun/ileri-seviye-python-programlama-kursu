#7️⃣.4️⃣  CSV Örnek Uygulama - Proje Senaryosu: Alışveriş Kaydı
#💡 Projemiz, kullanıcının alışveriş yaparken seçtiği ürünlerin adını, miktarını ve fiyatını kaydedeceğiz
#💡 Sonrasında bu bilgileri bir CSV dosyasına yazacağız ve aynı dosyadan alışveriş özetini alabileceğiz
#💡 Veri: Ürün adı, ürün fiyatı, ürün miktarı.
#💡 CSV Dosyası: alisveris.csv (Alışveriş kaydını tutacağız).

# ----------------------------------------- ALIŞVERİS SEPETİ UYGULAMASI  ----------------------------------- #
#💲 Adım 1: Kullanıcıdan Alışveriş Verisi Almak
import csv

# Dosya adı
filename = '7.0/alisveris.csv'

# Kullanıcıdan veri almak
def veri_al():
    urun_adi = input("Ürün adı: ")
    urun_fiyati = float(input("Ürün fiyatı: "))
    urun_miktari = int(input("Ürün miktarı: "))
    return {'urun_adi': urun_adi, 'urun_fiyati': urun_fiyati, 'urun_miktari': urun_miktari}

# CSV'ye yazma fonksiyonu
def csv_yaz(veriler):
    with open(filename, mode='r+', newline='', encoding='utf-8') as file:
        fieldnames = ['urun_adi', 'urun_fiyati', 'urun_miktari']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Başlıkları yaz
        csv_writer.writeheader()
        
        # Yeni alışverişi yaz
        csv_writer.writerow(veriler)

# Kullanıcıdan veri al ve yaz
veri = veri_al()
csv_yaz(veri)

print(f"{veri['urun_adi']} başarıyla kaydedildi.")




#💲 Adım 2: CSV Dosyasını Okuma ve Alışveriş Özeti Hesaplama,
def csv_okuma():
    toplam_harcama = 0
    with open(filename, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        
        # Verileri oku ve özet hesapla
        for row in csv_reader:
            urun_adi = row['urun_adi']
            urun_fiyati = float(row['urun_fiyati'])
            urun_miktari = int(row['urun_miktari'])
            
            # Toplam harcamayı hesapla
            toplam_harcama += urun_fiyati * urun_miktari
            
            # Alışverişi yazdır
            print(f"\n{urun_adi} - {urun_miktari} adet, {urun_fiyati} TL")
    
    print(f"Toplam Harcama: {toplam_harcama} TL")

# Alışveriş özetini yazdır
csv_okuma()



#💲 Adım 3: CSV Dosyasındaki Veriyi Güncelleme veya Silme
def csv_guncelle():
    urun_adi = input("\nGüncellenen Ürün adı: ")
    yeni_fiyat = input("Güncelenen Fiyatı: ")

    yeni_deger = []
    güncellendi_mi = False
    
    with open(filename, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        
        for sira in csv_reader:
            if sira['urun_adi'] == urun_adi:
                sira['urun_fiyati'] = yeni_fiyat
                güncellendi_mi = True
            yeni_deger.append(sira)
    
    # Dosyayı tekrar yazma
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['urun_adi', 'urun_fiyati', 'urun_miktari']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        csv_writer.writeheader()
        csv_writer.writerows(yeni_deger)
    
    if güncellendi_mi:
        print(f"\n{urun_adi} ürününün fiyatı başarıyla güncellendi.")
    else:
        print(f"{urun_adi} ürünü bulunamadı.")

# Örnek güncelleme
csv_guncelle()
csv_okuma()
