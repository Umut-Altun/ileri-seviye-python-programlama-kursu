#7️⃣.0️⃣  CSV DictWriter
#💡 Python'da CSV dosyasına veri yazarken, DictWriter sınıfını kullanarak verileri bir sözlük formatında 
# ekleyebiliriz. Bu yöntem, her satırın bir anahtar-değer çiftinden oluştuğu bir yapı sunar,bu sayede veriler
# daha kolay ve anlaşılır bir şekilde yazılabilir.
#💡 DictWriter: CSV dosyasına veri yazarken, her veri satırının anahtarları ile sütun başlıklarını eşleştirir.
#--- writeheader(): CSV dosyasına başlık satırını ekler.
#--- writerow(): Bir satır ekler.
#--- writerows(): Birden fazla satır ekler.

# -------------------------------------------  DİCTWRİTER KULLANIMI  ----------------------------------------- #
#💲 DictWriter Kullanımı - CSV Dosyasına Veri Yazma
import csv

data = [
    {'isim': 'Ali', 'yaş': 33, 'şehir': 'Bursa'},
    {'isim': 'Ayşegül', 'yaş': 27, 'şehir': 'Antalya'},
    {'isim': 'Veli', 'yaş': 40, 'şehir': 'İzmir'}
]

with open('7.0/personeller.csv', mode='w', newline='', encoding='utf-8') as file:
    # Sütun başlıkları
    fieldnames = ['isim', 'yaş', 'şehir']

    # DictWriter oluşturuluyor
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Başlıkları yazıyoruz
    csv_writer.writeheader()

    # Sözlük verisini dosyaya yazıyoruz
    csv_writer.writerows(data)



# Var Olan CSV Dosyasına Veri Ekleme (Append Mode)
import csv

new_data = [
    {'isim': 'Murat', 'yaş': 35, 'şehir': 'Ankara'},
    {'isim': 'Zeynep', 'yaş': 29, 'şehir': 'Bursa'}
]

with open('7.0/personeller.csv', mode='a', newline='', encoding='utf-8') as file:
    fieldnames = ['isim', 'yaş', 'şehir']
    
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Yeni veri satırlarını ekliyoruz
    csv_writer.writerows(new_data)
