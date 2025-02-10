#7️⃣.1️⃣  CSV DictReader
#💡 CSV dosyasındaki her satırı bir sözlük (dictionary) olarak okumanızı sağlar. 
#💡 Bu, verilerin daha anlamlı ve daha kolay erişilebilir olmasını sağlar. 
#💡 Her bir satırın anahtarları dosyanın başlıkları olur, ve değerleri ise o satırdaki veriler olur.

# -------------------------------------------- DİCTREADER KULLANIMI  ------------------------------------------ #
#💲 DictReader Kullanımının Temel Yapısı
import csv

with open('7.0/youtube.csv', mode='r', newline='', encoding='utf-8') as file:
    csv_dict_reader = csv.DictReader(file)
    
    # Her satırı sözlük olarak yazdırıyoruz
    for row in csv_dict_reader:
        print(row)
        print(row["Video"])


    #➕ Yaşı 25'ten büyük olanları yazdırıyoruz
    for row in csv_dict_reader:
        if int(row['published']) > 2020:
            print(row)
            # print(row["Video"])




#💲 CSV Dosyasındaki Verileri İstatistiksel Olarak İnceleme
toplam_begeni = 0
video_sayisi = 0

with open('7.0/youtube.csv', mode='r', newline='', encoding='utf-8') as file:
    csv_dict_reader = csv.DictReader(file)
    
    for row in csv_dict_reader:
        toplam_begeni += int(row['Likes'].replace(',', '').strip()) 
        video_sayisi += 1

ortalama_begeni = toplam_begeni / video_sayisi
print("Ortalama Begeni:", ortalama_begeni)  # {ortalama_begeni:,.0f}



#💲 DictReader ile Gelişmiş Kullanım: Başlıklar ile Erişim
with open('7.0/youtube.csv', mode='r', newline='', encoding='utf-8') as file:
    csv_dict_reader = csv.DictReader(file)
    
    # Başlıkları dinamik olarak alalım
    for row in csv_dict_reader:
        for key, value in row.items():
            print(f"{key}: {value}")
