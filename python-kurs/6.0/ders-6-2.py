#6️⃣.2️⃣ Örnek Uygulama Projesi
#✅ Bu projede, kullanıcıdan alınan bir metni analiz ederek aşağıdaki işlemleri gerçekleştireceğiz:
# E-posta Adreslerini Bulma: Metin içinde geçerli e-posta adreslerini tespit edeceğiz.
# Telefon Numaralarını Bulma: Metin içinde geçerli telefon numaralarını tespit edeceğiz.
# Tarihler: Metin içinde geçerli tarih formatlarını (gün/ay/yıl) bulacağız.
# URL Adreslerini Bulma: Metin içinde geçerli URL adreslerini bulacağız.

# ----------------------------------------- METİN ANALİZİ UYGULMASI  -------------------------------------------- #
import re

#✨ E-posta Adresi Regex'i
email_pattern = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

#✨ Telefon Numarası Regex'i
phone_pattern = r"\+90[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{3}"

#✨ Tarih Regex'i
date_pattern = r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b"

#✨ URL Regex'i
url_pattern = r"https?://[a-zA-Z0-9.-]+(?:/[^\s]*)?"


metin = """
Merhaba, benim adım Umut. E-posta adresim umut@gmail.com ve telefon numaram +90 123 456 7890.
Bugün 10/02/2025 tarihinde bir toplantı yapacağız. Ziyaret ettiğim site https://www.yapayrehber.store
"""


##✨ re.findall() fonksiyonunu kullanacağız. Bu fonksiyon, verilen desenle eşleşen tüm dizeleri bulur.
emails = re.findall(email_pattern, metin)
print(f"E-posta Adresleri ({len(emails)}):", emails)

phones = re.findall(phone_pattern, metin)
print(f"Telefon Numaraları ({len(phones)}):", phones)

dates = re.findall(date_pattern, metin)
print(f"Tarihler: ({len(dates)})", dates)

urls = re.findall(url_pattern, metin)
print(f"URL'ler: ({len(urls)})", urls)



