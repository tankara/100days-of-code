    #Değişkenler
""" 
    Pythonda yorum satırı 3lü çift tırnakla ya da diyez # işareti ile yapılır. 
    Aynı zamanda farklı yerlerde farklı değerler ile kullandığımız şeyler değişkenlerdir
    Özetle verileri saklamamıza yarayan şeylere değişken denir. 
    Örnek; 

"""
age= 15

    #Temel Veri Tipleri
""" 
    Integer ve float sayıları gösteren veri tipidir. String çeşitli karakter dizilerini tutar
    Boolean ise verinin doğruluk değerini tutar (true,false).

"""
    #integer
money = 200
    # float
pi = 3,14
    #string
name="john wick" #"" ile ya da '' ile tanımlanır

    #String Methodları
""" 
    Stringler immutable yani değiştirilemezdir. Bu herhangi bir karakteri başka bir karakterle
    değiştiremeyeceğimiz anlamına gelir. Ancak bir string en baştan farklı şekilde oluşturulabilir. 
    
    .count()= metin içerisindeki karakterleri sayar.
    .upper()= metnin tüm harflerini büyük harf yapar.
    len(metin)= metnin karakter sayısını verir.
    .title() = metindeki her kelimenin ilk harfini büyük; diğerlerini küçük yapar.
    .capitalize() = metindeki ilk hatfi büyük yapar.
    .lower() = metindeki harfleri küçük yapar.
    .rstrip() = metnin sağ tarafındaki boşlukları kaldırır.
    .lstrip() = metnin sol tarafındaki boşlukları kaldırır.
    .strip() = metnin sağındaki ve solundaki boşlukları kaldırır.
    .split() = metni kelime kelime ayırır.
    .replace() = metnin bazı kısımlarını değiştirmek için kullanılır.
    .startswith() = metnin hangi karakterle başlayıp başlamadığını sorgulamak için kullanılır.
    Sonucu bool veri tipiyle verir.
    .endswith() = metnin hangi karakterle bitip bitmediğini sorgulamak için kullanılır.
    Sonucu bool veri tipiyle verir.
    .find() = metindeki bir karakterin index'ini bulmak için kullanılır.

    .isupper(), .istitle(), .isspace(), .isnumeric(), .islower(), .isdigit(), .isdecimal() ise
    metnin belirtilen formatta olup olmadığını sorgulamaya yarayan methodlardır.

  """

#örnekler

metin1="hello wORLd!"
metin2="     Yazilim benim için bir tutku     "
print(metin1)
print(metin2)
print(".count('l') -->",metin1.count("l")) #2 
print(".upper() -->",metin1.upper()) #HELLO WORLD!
print("len(metin) -->",len(metin1)) #12
print(".title() -->",metin1.title()) #Hello World!
print(".capitalize() -->",metin1.capitalize()) #Hello world!
print("lower() -->", metin1.lower()) #hello world!
print("lstrip() -->",metin2.lstrip()) #Yazilim benim için bir tutku
print("rstrip() -->",metin2.rstrip()) #     Yazilim benim için bir tutku
print("strip() -->",metin2.strip()) #Yazilim benim için bir tutku
print("replace('h','t') -->",metin1.replace("h","t")) #tello wORLd!
print("startswith('h') -->",metin1.startswith("h"))  #True
print("endswith('!') -->", metin1.endswith("!")) #True
print("find('l') -->",metin1.find("l")) #2