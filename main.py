#1 Kullanıcıdan kelime al
#2 alınan kelimeyi sesli harfler içinde arat
#3 bulduğu zaman sayacı 1 arttır.
#4 sonucu ekrana yazdır.

sesli_harfler = "aeıioöuü"
sayac = 0
def kelime_al():
  return input("Bir kelime giriniz: ")

def sesli_mi(harf):
  return harf in sesli_harfler

def arttır(sayac, kelime):
  for harf in kelime:
    if sesli_mi(harf):
      sayac += 1
  return sayac

def ekrana_yaz(kelime):
  mesaj = "{} kelimesinde {} sesli harf var"
  print(mesaj.format(kelime, arttır(sayac, kelime)))

def çalıştır():
  kelime=kelime_al()
  ekrana_yaz(kelime)

çalıştır()