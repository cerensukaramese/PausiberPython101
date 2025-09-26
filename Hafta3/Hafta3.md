
# Mantıksal ve Atama Operatörleri

Python'da atama ve karşılaştırma işlemleri için kullanılan operatörler:

## Atama Operatörleri

- **=**: Değer atar.

## Karşılaştırma Operatörleri

- **==**: Eşit mi?
- **!=**: Eşit değil mi?
- **<**: Küçük mü?
- **>**: Büyük mü?
- **<=**: Küçük veya eşit mi?
- **>=**: Büyük veya eşit mi?

## Mantıksal Operatörler

- **and**: Her iki koşul doğruysa `True` döner.
- **or**: En az bir koşul doğruysa `True` döner.
- **not**: Koşulun tersini döner.

---
# Koşullu İfadeler (If - Else)

Python'da koşullu ifadeler, bir programın belirli bir durumda farklı davranışlar sergilemesine olanak tanır. Bu yapı, karar vermek ve birden fazla alternatif arasında seçim yapmak için kullanılır.

## If - Else Yapısı

**`if`** anahtar kelimesi bir koşulu kontrol eder. Koşul doğruysa (`True`), ilgili blok çalıştırılır. Eğer yanlışsa (`False`), **`else`** bloğuna geçilir (varsa).

### Temel Kullanım

```python
a=100
b=200
if b > a :
  print("b, a'dan büyüktür")
```

Yukarıdaki kodda, `x > 5` koşulu doğru olduğundan ekrana "x 5'ten büyüktür." mesajı yazdırılır. `else` kısmı koşul sağlanmazsa çalışır.

Else, önceden belirttiğimiz tüm koşullar gerçekleşmediyse diğer durumu nu ifadeyi yazarak belirtilir. Bu ifadeden sonra koşul yazılmaz.

````python
a=100
b=200
if b > a :
  print("b, a'dan büyüktür")
elif a == b:
  print("a, b'ye eşittir")
else:
  print("a, b'den büyüktür")
  
`````
Yukarıdaki örnekte ilk koşul doğru değil elif koşulu da doğru değil bu yüzden else koşuluna gidiyoruz ve "a'nın b'den büyük olduğunu" yazdırıyoruz.
### Elif (Else If)

Birden fazla koşul kontrol etmek istiyorsak, **`elif`** anahtar kelimesini kullanabiliriz. İlk koşul sağlanmazsa, `elif` ile kontrol edilen koşul denenir.

```python
a=100
b=100
if b > a: #bu koşulu kontrol eder doğru olmadığı için diğer koşula geçer.
  print("b, a'dan büyüktür")
elif a == b: #bu koşulu doğru sağlar.
  print("a, b'ye eşittir")
```

Bu yapıda, program sırayla koşulları dener ve ilk doğru koşulun bloğunu çalıştırır. Eğer hiçbir koşul doğru değilse, `else` bloğuna geçer.

### Mantıksal Operatörlerle If Kullanımı

Birden fazla koşulu aynı anda kontrol etmek için **`and`** ve **`or`** operatörleri kullanılabilir.

```python
a = 10
b = 20
if a > 5 and b > 15:
    print("Her iki koşul da doğru.")
```

Bu örnekte, hem `a > 5` hem de `b > 15` koşulu sağlandığında ekrana "Her iki koşul da doğru." yazdırılır. **`and`** operatörü her iki koşulun da doğru olmasını gerektirir.

**`or`** operatörü ise en az bir koşul doğruysa çalışır:

```python
a = 10
b = 5
if a > 5 or b > 10:
    print("Koşullardan biri doğru.")
```

Bu örnekte, sadece `a > 5` doğru olduğu için, "Koşullardan biri doğru." mesajı ekrana yazdırılır.

### İç İçe If Kullanımı

**İç içe if yapıları**, bir koşulun doğru olduğu durumlarda yeni koşullar eklememize olanak tanır.

```python
x = 25
if x > 10:
    print("x 10'dan büyük")
    if x > 20:
        print("x 20'den de büyük")
    else:
        print("ama x 20'den küçük")
```

Bu yapı, bir koşul doğru olduğunda başka bir koşulun da kontrol edilmesini sağlar. Yukarıdaki örnekte, `x 10'dan büyük` koşulu sağlandığında, ayrıca `x 20'den büyük mü` kontrol edilir.

### Pass ile Boş If Yapısı

Bazen, bir `if` bloğunda henüz kod yazmamış olabiliriz. Python’da bu durumlarda **`pass`** anahtar kelimesi kullanılarak geçici olarak blok boş bırakılabilir.

```python
x = 10
if x > 5:
    pass  # Geçici olarak bloğu boş bırakır, hata vermez.
```

---

# Döngüler

Döngüler, bir işlemi tekrar tekrar gerçekleştirmek için kullanılır. Python’da iki ana döngü türü vardır: **while döngüsü** ve **for döngüsü**.

## While Döngüsü

**While** döngüsü, bir koşul doğru olduğu sürece çalışmaya devam eder. Döngünün koşulu doğru (`True`) oldukça, döngüdeki ifadeler tekrar tekrar çalışır.

### While Döngüsü Temel Kullanımı

```python
i = 0
while i < 5:
    print(i)
    i += 1  # i değerini her seferinde 1 artırır
```

Bu örnekte, `i` değişkeni 5’ten küçük olduğu sürece döngü devam eder. Her döngüde `i` değeri 1 artırılır ve ekrana yazdırılır. Döngü, `i` 5'e eşit olduğunda sona erer.

### Sonsuz Döngü

Eğer döngü koşulu her zaman doğru olursa, döngü sonsuza kadar çalışır. Bu tür döngülere **sonsuz döngü** denir.

```python
while True:
    print("Bu döngü sonsuz olarak çalışır.")
```

Bu tür bir döngüyü durdurmak için `break` anahtar kelimesi kullanılabilir. Örneğin, bir koşul sağlandığında döngüyü sonlandırmak için:

```python
i = 0
while True:
    print(i)
    if i == 5:
        break  # i 5 olduğunda döngü sonlanır
    i += 1
```

### While ile Artış

Bir döngüde genellikle bir sayaç veya indeks kullanılır. Bu sayaç, döngünün her adımında artırılarak döngünün belirli bir noktada sonlanmasını sağlar.

```python
i = 0
while i < 10:
    print("i'nin değeri:", i)
    i += 2  # Her adımda i'yi 2 artırır
```

## For Döngüsü

**For** döngüsü, bir koleksiyonun (liste, dizi, string, vb.) elemanları üzerinde tekrarlı bir işlem yapar. Her iterasyonda koleksiyonun bir elemanını alır ve ilgili blokta kullanır.

### For Döngüsü Temel Kullanımı

```python
isimler = ["Ahmet", "Mehmet", "Ali"]
for isim in isimler:
    print(isim)
```

Bu döngü, `isimler` listesindeki her bir öğeyi sırayla alır ve ekrana yazdırır.

### Range() ile For Döngüsü

**`range()`** fonksiyonu, belirli bir aralıktaki sayılar üzerinde döngü oluşturmak için kullanılır.

```python
for i in range(5):
    print(i)
```

Bu örnekte, `range(5)` ifadesi 0'dan 4'e kadar olan sayıları üretir ve döngü bu sayılar üzerinde çalışır.

### For ile Liste ve String Üzerinde Döngü

For döngüsü, sadece sayılar üzerinde değil, listeler ve string'ler üzerinde de çalışabilir.

```python
kelime = "Python"
for harf in kelime:
    print(harf)
```

Bu döngü, `kelime` string'inin her bir harfi üzerinde çalışır ve sırayla her harfi ekrana yazdırır.

### İç İçe For Döngüsü

For döngüleri de iç içe kullanılabilir. İç içe for döngüleri genellikle iki boyutlu listeler (matrisler) gibi yapıların elemanlarını işlemek için kullanılır.

```python
matris = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for satir in matris:
    for eleman in satir:
        print(eleman, end=" ")
    print()  # Her satırı yeni satıra yazdırır
```

Bu kod, 3x3 boyutunda bir matrisin her elemanını sırayla ekrana yazdırır.

### Break ve Continue

**`break`** anahtar kelimesi döngüyü sonlandırırken, **`continue`** döngünün o adımını atlayıp bir sonraki adıma geçer.

- **Break**: Döngüyü anında sonlandırır.
- **Continue**: Döngünün o iterasyonunu atlar.

```python
for i in range(10):
    if i == 5:
        break  # i 5 olduğunda döngü sona erer
    print(i)

for i in range(10):
    if i == 5:
        continue  # i 5 olduğunda bu iterasyonu atlar
    print(i)
```

### For Döngüsünde Else Yapısı

Döngülerdeki else ifadesi yalnızca döngü başarıyla tamamlanırsa çalışır. Else ifadesinin asıl kullanımı, öğeleri aramak içindir:

```python
my_list = [1, 2, 3, 4, 5]

for i in my_list:
    if i == 3:
        print("Öğe bulundu!")
        break
    print(i)
else:
    print("Öğe bulunamadı!")
```

Bu kodda, `i` 3'e eşit olduğunda döngüden çıkmak için `break` kullanıyoruz. Bu, else ifadesinin atlanmasına neden olur. Denemek isterseniz, döngüde olmayan bir değeri arayarak koşulu değiştirebilirsiniz; bu, else ifadesinin çalışmasına yol açar.