#7️⃣.0️⃣  CSV Dosyadan Bilgi Yazma
#💡 Bu derste, CSV dosyasına nasıl veri yazabileceğimizi, mevcut CSV dosyasını nasıl güncelleyebileceğimizi ve yeni
#      veriler ekleyebileceğimizi öğreneceğiz.
#💡 Python'da csv.writer ile CSV dosyasına veri yazabilirsiniz. writerow() veya writerows() metodları ile dosyaya
#      satır ekleyebilirsiniz.
#----- csv.writer: Bu sınıf, verileri bir CSV dosyasına satır satır eklemenizi sağlar.
#----- writerow(): Tek bir satır ekler.
#----- writerows(): Birden fazla satır ekler.
#💡 CSV dosyasına veri yazarken dikkat etmemiz gereken birkaç nokta vardır:
#----- 'w': Yeni dosya oluşturur veya var olan dosyayı silip yeniden oluşturur.
#----- 'a': Var olan dosyaya veri ekler.

# ------------------------------------------- CSV BİLGİ YAZMA KULLANIMI  ----------------------------------------- #
#💲 CSV Dosyasına Veri Yazma - Tek Satır Yazma
import csv

with open('7.0/personeller.csv', mode='w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    
    # Başlık satırını yazıyoruz
    csv_writer.writerow(['isim', 'yaş', 'şehir'])
    
    # Veri satırlarını yazıyoruz
    csv_writer.writerow(['Ahmet', 25, 'İstanbul'])
    csv_writer.writerow(['Ayşe', 30, 'Ankara'])
    csv_writer.writerow(['Mehmet', 22, 'İzmir'])



#💲 CSV Dosyasına Birden Fazla Satır Yazma
data = [
    ['Ahmet', 25, 'Rize'],
    ['Ayşe', 30, 'Samsun'],
    ['Mehmet', 22, 'Ordu']
]

with open('7.0/personeller.csv', mode='w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    
    # Başlık satırını yazıyoruz
    csv_writer.writerow(['isim', 'yaş', 'şehir'])
    
    # Birden fazla satır yazıyoruz
    csv_writer.writerows(data)



#💲 CSV Dosyasına Veri Eklemek (Append Mode)
new_data = [
    ['Can', 28, 'Bursa'],
    ['Zeynep', 26, 'Antalya']
]

with open('7.0/personeller.csv', mode='a', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    
    # Yeni veri satırlarını ekliyoruz
    csv_writer.writerows(new_data)


