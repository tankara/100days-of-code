
"""
    OYUNDA MAÇ SONU KAZANINCA YAZMAK İÇİN SONU EASY KELİMESİNİN KISALTMASI OLAN 'EZ' İLE BİTEN
    KELİMELERİ BİR SÖZLÜKTEN AYIKLAMAMIZI SAĞLAYAN KOD

"""

kelimeler= ["anamnez","kalem","çerez","feleaket","mayonez","fotosentez","falez","obez","bez","kramp","tavuk","kurt"]

aranankelimeler=[]

for i in kelimeler:
    if i[-1] == "z" :
        if i[-2]== "e":
            aranankelimeler.append(i)
        else:
            continue
    else:
        continue 

print(aranankelimeler)