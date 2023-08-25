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