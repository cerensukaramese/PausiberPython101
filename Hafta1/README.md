# PausiberPython101


### **1. Hafta: Python ve Programlama Temelleri**
---

### **1. Bölüm: Programlama Dillerine Giriş **

#### **1. Programlama Nedir?** 
Programlama, bilgisayarlara belirli görevleri yapmaları için komutlar vermemizi sağlayan bir süreçtir. Bilgisayarlar kendi başlarına herhangi bir işi yapamazlar; onların anlayabileceği bir dille yazılmış talimatlara ihtiyaç duyarlar. Programlama dilleri, bu talimatları yazmamızı sağlayan araçlardır.

Bilgisayarların anladığı dil makine dilidir. Makine dili, 0 ve 1'lerden oluşur ve insanlar için anlaşılması zordur. Bu nedenle, programlama dilleri insanların okuyup yazabileceği şekildedir. Python gibi programlama dilleri bu açıdan kullanıcılara büyük kolaylık sağlar.
Instagram, Reddit, Dropbox python ile oluşturulmuştur. 

#### **2. Programlama Dillerinin Sınıflandırılması** 
Programlama dilleri, insan diline ne kadar yakın olduklarına göre iki ana kategoriye ayrılır:

- **Yüksek Seviyeli Programlama Dilleri**: Python, Java, C++ ,Ruby gibi diller insan diline yakın olan, bilgisayar donanımından bağımsız şekilde çalışan, yazılması ve anlaşılması daha kolay dillerdir. Bunlar genellikle günlük hayatta karşılaştığımız problemleri çözerken kullanılır.
  
- **Düşük Seviyeli Programlama Dilleri**: Assembly ve makine dili gibi diller donanıma daha yakın çalışır. Bilgisayar donanımı üzerinde daha fazla kontrol sağlarlar, işlemcinin komut setine daha yakındır bu yüzden kod daha hızlı ve verimli çalışabilir ancak anlaşılması ve yazılması zordur.

Python, **yüksek seviyeli ve yorumlayıcı bir dil** olduğu için yazılan kod, satır satır çalıştırılır ve anında geri bildirim alınır. Bu da Python'u öğrenmeyi ve hata ayıklamayı kolaylaştırır.

#### **3. Neden Python?** 
Python, **veri bilimi, yapay zeka, web geliştirme, otomasyon** ve daha birçok alanda popüler bir dildir. Kullanıcı dostu olması, geniş kütüphane desteği ve basit syntax yapısı ile özellikle yeni başlayanlar için ideal bir dil olarak kabul edilir.
Python bircok platformda kullanilabilir(Windows, Mac, Linux, Raspberry Pi, etc). 
Ayni zamanda Python, prosedürel, nesne yönelimli veya fonksiyonel olarak ele alınabilir.
##  C/C++                                     
![image](https://github.com/user-attachments/assets/85b12dd3-8b93-4ba8-8321-796cd04a18dc)

## Java
![image](https://github.com/user-attachments/assets/32680554-6da8-4efc-98ee-34a524512566)

## C\#
![image](https://github.com/user-attachments/assets/11ae3622-e058-4f2a-8f70-2852166c4fea)

#### **4. Python Kurulum ve IDE Tanıtımı **
Python’u bilgisayarınıza indirip kurabilirsiniz. Python'un resmi sitesinden bilgisayarınıza uygun dosyayı seçip indirebilirsiniz.
- https://www.python.org/downloads/
  
Ayrıca, kod yazmak için kullanabileceğimiz çeşitli **IDE**'ler (Entegre Geliştirme Ortamları) vardır. En popüler IDE’lerden bazıları:
- **PyCharm**
- **VS Code**
- **Jupyter Notebook**
Derste VS Code üzerinden anlatım yapacağız.
- https://code.visualstudio.com/download
Bu linkten VS Code'u indirip kurabilirsiniz.

Eğer derse gelmeden kurmadıysanız ya da problem yaşadıysanız online editörler üstünden dersi takip edebilirsiniz:
- https://www.online-python.com/
---

### **2. Bölüm: Python’a Giriş **

#### **1. Python’u Tanıyalım **
Python’u bir dil olarak tanıdıktan sonra, bu dili nasıl kullanacağımızı öğrenelim. Python, hem küçük projeler hem de büyük çaplı sistemler için kullanılabilir. Web uygulamaları, veri analizleri, otomasyon görevleri gibi çeşitli alanlarda Python sıklıkla tercih edilir.

Python’un gücünü anlamak için basit bir "Merhaba Dünya" programı yazalım. Python’da bir program yazmak ve çalıştırmak oldukça basittir:

```python
print("Merhaba Dünya!")
```

Bu kod, ekrana **Merhaba Dünya!** yazdırır. Python'un syntax'ı (yazım kuralları) oldukça basit ve okunaklıdır.



#### **2. Basit Bir Python Programı Yazalım **
Python’da veri tiplerine geçmeden önce, birkaç basit program yazalım. İlk olarak, kullanıcıdan veri almayı öğrenelim. `input()` fonksiyonu ile kullanıcıdan giriş alabiliriz:

```python
isim = input("Adınızı girin: ")
print(f"Merhaba, {isim}!")
```

Bu program, kullanıcının girdiği ismi alır ve ekrana "Merhaba, [isim]!" yazar.

---

### **3. Bölüm: Python’da Veri Tipleri ve Temel İşlemler**

#### **1. Python Temel Veri Tipleri **
Python’da birkaç temel veri tipi vardır. Bunlar:

- **`int`** (Tam Sayı): Tamsayılar, örneğin `5`, `10`, `-3`.
- **`float`** (Ondalıklı Sayı): Ondalıklı sayılar, örneğin `3.14`, `0.5`, `-1.23`.
- **`str`** (String, Karakter Dizisi): Metin verileri, örneğin `"Python"`, `"Merhaba"`.
- **`bool`** (Boolean, Doğru/Yanlış): Mantıksal değerler, `True` veya `False`.

Örnek olarak bazı veri tiplerini inceleyelim:
```python
a = 5  # int
b = 3.14  # float
c = "Merhaba"  # str
d = True  # bool
```

Veri tipini öğrenmek için `type()` fonksiyonunu kullanabiliriz:
```python
print(type(a))  # int
print(type(b))  # float
print(type(c))  # str
print(type(d))  # bool
```

#### **2. Veri Tipi Dönüşümleri **
Python’da bir veri tipini diğerine dönüştürebiliriz. Örneğin, bir string’i integer’a çevirebiliriz:
```python
x = "10"
y = 5
print(int(x) + y)  # string -> int dönüşümü
```

Bu kodda, `"10"` string değeri `int()` fonksiyonu ile integer’a çevrilir ve ardından `y` ile toplanır.

#### **3. Matematiksel İşlemler **
Python’da temel matematiksel işlemler şunlardır:

- **Toplama**: `+`
- **Çıkarma**: `-`
- **Çarpma**: `*`
- **Bölme**: `/`
- **Üs Alma**: `**`
- **Mod Alma**: `%`

Örnek:
```python
a = 10
b = 3
print(a + b)  # toplama
print(a - b)  # çıkarma
print(a * b)  # çarpma
print(a / b)  # bölme
print(a ** b)  # üs alma
print(a % b)  # mod alma
```

---

### **4. Bölüm: Python’da String İşlemleri **

#### **1. String Birleştirme ve Dilimleme **
Stringler, metin verilerini temsil eder. Python’da string birleştirme ve dilimleme işlemleri oldukça basittir:

- **Birleştirme**: String’ler `+` operatörü ile birleştirilebilir:
  ```python
  isim = "Python"
  yil = 2024
  print(isim + " " + str(yil))  # Python 2024
  ```

- **Dilimleme**: String içindeki belirli karakterlere erişebiliriz:
  ```python
  kelime = "Python"
  print(kelime[0:3])  # "Pyt"
  ```

#### **2. String Metodları **
Python, string manipülasyonu için birçok metod sunar. En çok kullanılan string metodları şunlardır:

- **`upper()`**: Tüm karakterleri büyük harfe çevirir:
  ```python
  isim = "python"
  print(isim.upper())  # "PYTHON"
  ```

- **`lower()`**: Tüm karakterleri küçük harfe çevirir:
  ```python
  isim = "PYTHON"
  print(isim.lower())  # "python"
  ```

- **`strip()`**: Başında ve sonunda bulunan boşlukları siler:
  ```python
  isim = "  Python  "
  print(isim.strip())  # "Python"
  ```

- **`replace()`**: Sectiginiz harfi istediginiz harf ile degismenizi saglar:
  ```python
  isim = "  Python  "
  print(isim.replace('o','a'))  # "Pythan"

---

### **5. Bölüm: Uygulama**

#### **1. Uygulama Örnekleri **
Öğrenciler öğrendiklerini uygulayarak pekiştirirler:

1. Kullanıcıdan iki sayı alın ve bu sayılar üzerinde toplama, çıkarma

, çarpma ve bölme işlemleri yapın:
   ```python
   x = int(input("Birinci sayıyı girin: "))
   y = int(input("İkinci sayıyı girin: "))
   print("Toplam:", x + y)
   print("Fark:", x - y)
   print("Çarpım:", x * y)
   print("Bölüm:", x / y)
   ```

2. Girilen bir string üzerinde `upper()`, `lower()`, `strip()` gibi metodları kullanarak string’i manipüle edin.

---
```python
    isim = input("İsminiz nedir? ")
    yas = input("Yaşınız nedir? ")
    print(f"Merhaba {isim}, {yas} yaşındasınız.")
    ```
    
