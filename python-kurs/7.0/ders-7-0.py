#7️⃣.0️⃣  CSV Files Nedir, Dosyadan Bilgi Okuma.
#💡 CSV, verileri saklamak ve paylaşmak için yaygın olarak kullanılan basit bir dosya formatıdır. 
#💡 Her satır bir kaydı temsil eder ve her sütun bir değeri temsil eder. 
#💡 Veriler, virgül (veya başka bir ayırıcı) ile ayrılır.
#💡 Veri, genellikle bir tablonun satır ve sütunlarına karşılık gelir. 
#💡 CSV dosyasını okumak için Python'un csv modülünü kullanıyoruz.
#💡 https://www.kaggle.com     

# ---------------------------------------------- CSV FİLES KULLANIMI  ------------------------------------------- #
#💲Python ile CSV Dosyasını Okuma
import csv

with open('7.0/youtube.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    #Listeyi yazdırıyoruz
    youtube_list = list(csv_reader)
    print(list(youtube_list))

    #➕ Başlıkları yazdırıyoruz
    headers = next(csv_reader)
    print("Başlıklar:", headers)

    #➕ Başlık satırını atlıyoruz ve Her satırı alt alta yazdırıyoruz
    next(csv_reader)
    for youtube in csv_reader:
        print(youtube)

