#index mantığı

""" 
    0  1  2  3  4  5  6  7  8  9  10  11 
    |  |  |  |  |  |  |  |  |  |   |   |   
    v  v  v  v  v     v  v  v  v   v   v 
    n  a  b  e  r     p  y  t  h   o   n

    [ starting index : stopping index : stepping size]

"""

myString = "naber python"
print(myString[:4]) #"nabe" 0'dan başlayarak 3.indexe kadar parçalayıp yazdırır.
print(myString[-2]) #sondan geriye doğru sayarak sondan ikinci harf olan "o" harfini yazdırdı.
print(myString[3:11:2]) #3. indexten başlar 11. indexe kadar her 2 indexte bir parçalar.

#Listeler
""" 
    Listeler, isminden de anlaşılacağı üzere sıralı nesnelerden oluşan liste ya da dizilerdir.

"""

calisanlar=["ali","veli","hüseyin","muhittin"] #köşeli parantez ile tanımlanır

cumle = "ALİ ATA BAK"
cumleninOgeleri = cumle.split()
print(cumleninOgeleri) #['ALİ', 'ATA', 'BAK'] stringden liste oluşturur

#Listelerin Methodları

""" 
    type() = tip sorguları.
    len() = eleman sayısını verir.
    .pop() = belirli bir elemanı listeden siler. parametre verilmezse sonuncuyu siler.
    .count() = eleman tekrarı sayar.
    .append() = eleman ekler.
    .index() = elemanın indeksini verir.
    .sorted() = sıralı elemanı sıraya dizer.
    .reverse() = sıralı elemanı tersten sıraya dizer.
    .extend() = iki listeyi birleştirir.
    .del() = elemanı siler.
    .remove() = elemanı siler.

"""
exampleList=["bir","iki","üç",4,5,6,4,4,4,4,4,4]
anotherList=[7,8,9,10]
print("type()",type(exampleList) ) #type() <class 'list'>
print("len()",len(exampleList)) #12
print(".pop()",exampleList.pop()) #sondaki indexteki 4'ü sildi
print(".pop('bir')",exampleList.pop(1)) #1. indexteki "iki" elemanını sildi
print(".count(4)",exampleList.count(4)) #6 adet 4 elemanı var
print(".append()",exampleList.append(3))
print(exampleList)                       #3 elemanını son indexe ekledi
print(".index()",exampleList.index("bir")) #0. index
print(".sorted()", anotherList.sort()) #sıralar
print(anotherList)
print(".reverse()", anotherList.reverse())
print(".extend(anotherlist)",exampleList.extend(anotherList))
del exampleList[2] 
print(exampleList)
print(".remove()", exampleList.remove("bir"))  #"bir" elemanını sildi
print(exampleList)
