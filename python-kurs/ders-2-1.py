# 2️⃣.1️⃣ List Comprehension İçinde if Kullanımı
# List Comprehension içinde if kullanarak filtreleme yapabiliriz.

# ⛔ Yanlış Kullanım (else yanlış yerde)	[sayi for sayi in sayilar if sayi % 2 == 0 else "tek"]   ❌Bu hata verir çünkü:
# if yalnızca bir filtreleme işlemi yapar, ama else eklenince bir dönüş değeri gerektirir.
# if ve else içeren bir ifadede, dönüş değeri başta belirtilmelidir.

# Özet Kullanım	Yazım Şekli
# Sadece if	          [sayi for sayi in sayilar if sayi % 2 == 0] ✅
# if-else Kullanımı	  [sayi if sayi % 2 == 0 else "tek" for sayi in sayilar] ✅
# Yanlış Kullanım   	[sayi for sayi in sayilar if sayi % 2 == 0 else "tek"] ❌

# ---------------------------------- LIST COMPREHENSION İÇİNDE if-else KULLANIMI ------------------------------------- #
# for item in liste:
#     if (kossul):
#         expression

# [expression for item in liste if (kosul) ]


# sayilar = [1,2,3,4,5,6,7,8,9]

# cift_sayilar = []
# for sayi in sayilar:
#     if sayi % 2 == 0:
#         cift_sayilar.append(sayi)
#     else:
#         cift_sayilar.append("tek")

# print(cift_sayilar)


# cift_sayilar_comp = [sayi if sayi % 2 == 0 else "tek" for sayi in sayilar ]
# print(cift_sayilar_comp)


# personeller = ["ali", "veli", "ayse","fatma"]
# personel_secimi = []

# for kisi in personeller:
#     if kisi == "ali":
#         personel_secimi.append(kisi)
#     else:
#         personel_secimi.append("uymana veri")

# print(personel_secimi)

# personeller = ["ali", "veli", "ayse","fatma"]
# personel_secimi = [kisi for kisi in personeller  if kisi == "ali"]

# print(personel_secimi)
