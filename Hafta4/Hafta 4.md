### Fonksiyon Nedir?

Fonksiyonlar, belirli bir görevi yerine getirmek için yazdığınız kod bloklarıdır. Parametre alabilir, geri dönüş değeri verebilirler ve kodunuzu daha düzenli hale getirirler. Fonksiyonlar `def` anahtar kelimesiyle başlar, bir isimle tanımlanır ve ardından iki nokta (`:`) ile devam eder. Örneğin:

```python
def bir_fonksiyon():
    print("Bir fonksiyon oluşturdunuz!")
```

Bu fonksiyon, sadece bir metin yazdırır. Bir fonksiyonu çağırmak için, fonksiyonun ismini ve ardından parantezleri kullanırız:

```python
bir_fonksiyon()
# Çıktı: Bir fonksiyon oluşturdunuz!
```

#### Boş Fonksiyon (Stub)

Bazen kodun yapısını oluştururken bir fonksiyonun içeriğini henüz doldurmak istemeyebilirsiniz. Bu durumda `pass` ifadesini kullanarak "boş" bir fonksiyon tanımlayabilirsiniz:

```python
def bos_fonksiyon():
    pass
```

`pass`, Python'a burada hiçbir şey yapmamasını söyleyen bir komuttur.

---
### Argümanlar

Fonksiyonlara bilgi geçmek için argümanlar kullanılır. Argümanlar, fonksiyon isminin ardından parantez içinde belirtilir:

```python
def my_function(isim):
    print(isim)

my_function("Emil")
my_function("Tobias")
my_function("Linus")
```

---
### Argüman Sayısı

Fonksiyonlar, varsayılan olarak doğru sayıda argümanla çağrılmalıdır:

```python
def my_function(isim, yas):
    print(isim + " " + yas)

my_function("Ahmet", "25")
```
---


### Fonksiyonlara Parametre Geçmek

Fonksiyonlara parametre göndererek onlara dışarıdan veri sağlayabiliriz. Mesela iki sayıyı toplayan bir fonksiyon yazalım:

```python
def topla(a, b):
    return a + b

print(topla(1, 2))  # Çıktı: 3
```

Fonksiyonlar her zaman bir değer döndürür; eğer bir değer dönmezse `None` döndürürler. Bu örnekte `a + b` sonucunu döndürmesini belirttik.

---

### Anahtar Kelime Argümanları (Keyword Arguments)

Fonksiyonları çağırırken argümanları isimlendirerek sırayı değiştirebilirsiniz:

```python
def topla(a, b):
    return a + b

print(topla(b=4, a=5))  # Çıktı: 9
```

Eğer bir fonksiyon parametreleri için varsayılan değerler belirlenmişse, argümanları atlamanız mümkün olur. Örneğin:

```python
print(topla())  # Çıktı: 3
```

Bu durumda `a` ve `b` varsayılan olarak 1 ve 2 değerlerini alır.

---
#### Parametre ve Argüman Farkı

Bir fonksiyonun tanımında yer alan değişkenlere **parametre**, fonksiyon çağrıldığında geçirilen değerlere ise **argüman** denir.

---

### *args ve **kwargs

Fonksiyonların değişken sayıda parametre alabilmesi için `*args` ve `**kwargs` kullanılır:

```python
def bircok_parametre(*args, **kwargs):
    print(args)
    print(kwargs)

bircok_parametre(1, 2, 3, isim="Ali", meslek="Yazılımcı")
# Çıktı:
# (1, 2, 3)
# {'isim': 'Ali', 'meslek': 'Yazılımcı'}
```

Bu örnekte `args` bir demet (`tuple`), `kwargs` ise bir sözlük (`dictionary`) olarak kullanılır.

---
Python’da, fonksiyon parametrelerinin **sadece konum** ya da **sadece anahtar kelime** ile çağrılmasını sağlamak için ` / ` ve ` * ` sembolleri kullanılır. Bu özellikler, fonksiyonlara girilen argümanların nasıl ve hangi sırayla verilmesi gerektiğini daha net bir şekilde belirtmeye yarar.

#### 1. Sadece Konumla Girilen Argümanlar (Positional-Only Arguments)

Bir fonksiyonun **sadece konumla** girilen argümanlar almasını istiyorsanız, parametrelerin sonuna `/` sembolünü ekleyebilirsiniz. Bu durumda, `/`'dan önce tanımlanan parametreler **yalnızca konum** yoluyla verilebilir ve anahtar kelime ile verilirse hata alırsınız.

**Örnek:**

```python
def my_function(x, /):
    print(x)

my_function(3)       # Bu geçerli, çünkü argüman konumla giriliyor.
my_function(x=3)     # Bu geçersiz ve hata verir, çünkü x yalnızca konumla girilmeliydi.
```

##### Neden Kullanılır?
Sadece konumla girilen argümanlar, bir fonksiyonun belirli bir sırayla çağrılmasını garanti eder ve fonksiyonun çağrılırken `x=...` gibi anahtar kelimelerle verilmesini istemediğiniz durumlarda faydalıdır.

#### 2. Sadece Anahtar Kelimeyle Girilen Argümanlar (Keyword-Only Arguments)

Bir fonksiyonun bazı parametrelerinin **yalnızca anahtar kelimeyle** belirtilmesini istiyorsanız, parametre listesinin başına `*` sembolü ekleyebilirsiniz. `*`'den sonraki parametreler **yalnızca anahtar kelimeyle** girilebilir; yani, doğrudan konumla girilirse hata alınır.

**Örnek:**

```python
def my_function(*, x):
    print(x)

my_function(x=3)     # Bu geçerli, çünkü x anahtar kelimeyle belirtilmiş.
my_function(3)       # Bu geçersiz ve hata verir, çünkü x anahtar kelime olarak verilmeliydi.
```

##### Neden Kullanılır?
Anahtar kelimeyle girilen argümanlar, kodun daha anlaşılır olmasını sağlar. Ayrıca, belirli bir parametrenin yanlış sırayla verilme riskini azaltır, çünkü her parametre anahtar kelimeyle tanımlandığı için hangi değerin hangi parametreye ait olduğu açıkça bellidir.

#### Özet:
- `/` sembolü: `parametre /` biçiminde kullanılır ve **yalnızca konum** ile girilen parametreleri belirtir.
- `*` sembolü: `*, parametre` biçiminde kullanılır ve **yalnızca anahtar kelimeyle** girilen parametreleri belirtir. 

Bu özellikler özellikle çok sayıda parametre içeren veya dikkatli çağrılması gereken fonksiyonlarda faydalıdır.

---
### Değer Döndürmek

Bir fonksiyonun sonuç olarak bir değer döndürmesi için `return` ifadesi kullanılır:
```python
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

```
---
### Rekürsiyon (Recursion)

Bir fonksiyonun kendisini çağırmasına **rekürsiyon** denir:

```python
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Rekürsiyon Örneği:")
tri_recursion(6)

```
Rekürsiyon, dikkatli yazılmadığında sonsuz döngüye girme riski taşır.

---
### Değişkenlerin Kapsamı ve Global Değişkenler

Python'da değişkenlerin hangi alanlarda geçerli olduğunu belirleyen bir kapsam (scope) kavramı vardır. Fonksiyon içinde tanımlanan değişkenler yalnızca o fonksiyon içinde geçerlidir. Ancak `global` anahtar kelimesi kullanılarak değişkenler global hale getirilebilir:

```python
def fonksiyon_a():
    global a
    a = 1
    b = 2
    return a + b

def fonksiyon_b():
    c = 3
    return a + c

print(fonksiyon_a())  # Çıktı: 3
print(fonksiyon_b())  # Çıktı: 4
```

Global değişkenler genellikle önerilmez, çünkü başka bir fonksiyonda kazara değiştirilebilirler.

---

### Lambda Fonksiyonları
Lambda fonksiyonları, Python'da **tek satırlık, küçük** ve **anonim fonksiyonlar** oluşturmak için kullanılır.

Lambda fonksiyonlarının genel yapısı şöyledir:

```python
lambda argüman1, argüman2, ... : ifade
```

- `argüman1, argüman2, ...` → Lambda fonksiyonuna girilen parametreler.
- `ifade` → Fonksiyonun geri döndüreceği sonuç, burada yalnızca **tek bir ifade** olabilir.

### Örnekler

1. **Basit Toplama İşlemi**

    ```python
    toplama = lambda x, y: x + y
    print(toplama(3, 5))  # Çıktı: 8
    ```

    - Burada `toplama` isimli bir lambda fonksiyonu tanımlandı. Bu fonksiyon, `x` ve `y` parametrelerini alır ve bunların toplamını döner.

2. **Karesini Alma**

    ```python
    karesi = lambda x: x ** 2
    print(karesi(4))  # Çıktı: 16
    ```

    - `karesi` fonksiyonu bir sayıyı alır ve karesini döner.

3. **Koşullu İfade Kullanımı**

    ```python
    çift_mi = lambda x: "Çift" if x % 2 == 0 else "Tek"
    print(çift_mi(5))  # Çıktı: Tek
    print(çift_mi(4))  # Çıktı: Çift
    ```

    - Bu örnekte `x` sayısının çift olup olmadığını kontrol eden bir lambda fonksiyonu oluşturulmuştur.

4. **Liste Elemanlarını Sıralamak**

    Lambda fonksiyonları, `sorted()` gibi fonksiyonlarda `key` parametresi ile de kullanılabilir.

    ```python
    sayılar = [(1, 2), (4, 1), (5, -1), (3, 3)]
    sıralı = sorted(sayılar, key=lambda x: x[1])
    print(sıralı)  # Çıktı: [(5, -1), (4, 1), (1, 2), (3, 3)]
    ```

    - Burada `sorted()` fonksiyonuna `key` olarak verilen lambda, her tuple'ın ikinci elemanına göre sıralama yapılmasını sağlıyor.

5. **Harita (map) Fonksiyonu ile Kullanım**

    `map()` fonksiyonu, bir liste gibi veri yapılarının her elemanına belirli bir işlevi uygulamak için kullanılır.

    ```python
    sayılar = [1, 2, 3, 4]
    kareler = list(map(lambda x: x ** 2, sayılar))
    print(kareler)  # Çıktı: [1, 4, 9, 16]
    ```

    - Bu örnekte, `map()` fonksiyonu ile her sayının karesi alınmıştır.


---
### DRY (Don’t Repeat Yourself)

Tekrarlayan kodlardan kaçınmak için aynı kod parçasını bir fonksiyon içine almanız önerilir. Böylece, tek bir yerde değişiklik yaparak tüm kodunuzu güncel tutabilirsiniz. Bu, kodunuzu daha okunabilir ve bakımı daha kolay hale getirir.

---
## Uygulamalar:

### Taş Kağıt Makas Oyunu:

```python
import random
import time

hamleler = ["taş", "kağıt", "makas"]
bilgisayar_hamlesi = random.choice(hamleler)

  
kullanici_hamlesi = input("Hamleni seç (taş, kağıt, makas): ").lower()
while kullanici_hamlesi not in ["taş", "kağıt", "makas"]:
	kullanici_hamlesi = input("Lütfen geçerli bir hamle girin (taş, kağıt ya da makas): ").lower()
 
print("Bilgisayar hamlesi:\n 3 ")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print(f"Bilgisayarın hamlesi: {bilgisayar_hamlesi}")

if kullanici_hamlesi == bilgisayar_hamlesi:
	print("Berabere!")
elif (kullanici_hamlesi == "taş" and bilgisayar_hamlesi == "makas") or \
(kullanici_hamlesi == "kağıt" and bilgisayar_hamlesi == "taş") or \
(kullanici_hamlesi == "makas" and bilgisayar_hamlesi == "kağıt"):
	print("Kazandın!")
elif (kullanici_hamlesi == bilgisayar_hamlesi):
	print("Kaybettin!")

```

### Fibonacci Sayısı:

```python
def fibonacci(n):
    fib_sequence = [0, 1]

    for i in range(2, n):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)
    return fib_sequence[:n]  

n = int(input("Kaç Fibonacci sayısı görmek istersiniz? "))

if n <= 0:
    print("Lütfen pozitif bir sayı girin.")
else:
    print("Fibonacci dizisi:", fibonacci(n))


```
