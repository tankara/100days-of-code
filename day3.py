"""

    SÖZLÜKLER ,SET VE TUPLE

"""

newDict = { "elma":100, "armut":125,"muz":210} #sözlük tanımlama

#newDict.clear() #sözlüğü siler

newDict.keys() #key değerlerini verir
newDict.values() #değerleri verir

#dict.fromkeys() sadece anahtar değerleri ile bir sözlük başlatmaya yarar;

ilkArray=["ali","veli","ayşe"]
ikinciArray=[45,70,100]

sonuc = dict.fromkeys(ilkArray,ikinciArray)

newDict.get("elma") #anahtar verildiğinde değer döndürür
newDict.items()     #anahtar-değer eşleşmelerin item by item verir
#newDict.pop("armut") #armut anahtar kelimesini siler

#sonuc = newDict.popitem() #parametre almaz son değeri siler

sonuc = newDict.setdefault("ali",100) #sözlükte ali yoksa ali'yi ekler
newDict.setdefault("elma",200) #sözlükte elma olduğu için mevcut değeri döndürdü
newDict.setdefault("elma",400) #var olan keyi değiştirmedi

# oldDict.update(newDict) #bir sözlük varsa elemanları ikinci sözlüğe göre düzenler ve ikinci sözlükle birleştirir

# newDict.clear() #sözlüğü siler 

newDict["armut"] = 750 #key değerini günceller
print(newDict)

newDict.pop("ali") #elma silindi

"""NOT: PYTHON'DA VALUE'YA GÖRE SEÇİM YAPAN BİR METHOD BULUNMAMAKTADIR."""

print(newDict)