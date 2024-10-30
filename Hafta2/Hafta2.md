
# Koleksiyon Veri Tipleri

Python'da dört temel koleksiyon veri tipi bulunmaktadır: **Listeler**, **Tuple'lar**, **Set'ler** ve **Dictionary'ler**. Bu veri yapıları, birden fazla öğeyi saklamaya olanak tanır ve farklı kullanım senaryolarına göre seçilir.

## Listeler

Listeler, Python'da diğer dillerdeki dizilere benzeyen, sıralı ve değiştirilebilir veri yapılarıdır. Aynı liste içinde farklı veri tipleri saklanabilir.

### Liste Tanımlamak

```python
my_list = []
my_list = list()  # Boş liste
my_list = [1, 2, 3, 4]  # Elemanları olan bir liste
```

### Liste Özellikleri ve Metotları

1. **Liste içinde farklı veri tipleri olabilir**: 

```python
my_list = [1, "Python", 3.14, True]
```

2. **Liste içinde liste** oluşturulabilir:

```python
nested_list = [[1, 2], [3, 4], [5, 6]]
```

3. **Liste elemanlarına ulaşma** ve **listeyi dilimleme**:

```python
my_list = [10, 20, 30, 40]
print(my_list[0])    # 10
print(my_list[-1])   # 40
print(my_list[1:3])  # [20, 30]
```

4. **Listeye eleman eklemek** ve **silmek**:

```python
my_list.append(50)  # Listenin sonuna eleman ekler
my_list.remove(20)  # Belirli bir elemanı siler
```

5. **Liste metodları**:
   - **sort()**: Listeyi sıralar.
   - **reverse()**: Listeyi ters çevirir.
   - **pop()**: Belirtilen indisteki elemanı siler.
   - **count()**: Bir elemanın listede kaç kez geçtiğini sayar.

Örnek:

Extend metodunu kullanarak iki listeyi birbirine karabiliriz:

```python
combo_list = [1,2]
one_list = [4, 5]
combo_list.extend(one_list)
print(combo_list)
#[1, 2, 4, 5]
```

Daha kolay bir yolu:

```python
 my_list = [1, 2, 3]
 my_list2 = ["a", "b", "c"]
 combo_list = my_list + my_list2
 print(combo_list)
 #[1, 2, 3, 'a', 'b', 'c']
```

Liste içerisindeki elemanları sıralayabileceğimiz bir metot olan sort()'u inceleyelim:
```python
 alpha_list = [34, 23, 67, 100, 88, 2]
 alpha_list.sort()
 print(alpha_list)
 #[2, 23, 34, 67, 88, 100]
```

Sort() metodu varsayılan olarak elemanları artan sırada sıralar.
Bir örnek daha:
```python
alpha_list = [34, 23, 67, 100, 88, 2]
sorted_list = alpha_list.sort()
print(sorted_list)
#None
```

Bu örnekte, sıralanmış listeyi bir değişkene atamaya çalışıyoruz. Ancak, sort() metodu bir listeyi yerinde sıralar, yani listeyi olduğu yerde değiştirir. Eğer sıralamanın sonucunu başka bir değişkene atamaya çalışırsanız, None (başka dillerdeki Null'a benzer) değeri alırsınız. Bu nedenle, bir listeyi sıralamak istediğinizde, listenin yerinde sıralandığını ve sonucunu başka bir değişkene atayamayacağınızı unutmamanız gerekir.

Bir listeyi sıralayıp başka bir değişkene atamak için sorted() metodunu kullanabiliriz:

```python
sorted_list = sorted(alpha_list)
print(sorted_list)


```python
my_list = [10, 20, 30, 40]
my_list.append(50)
print(my_list)  # [10, 20, 30, 40, 50]

my_list.pop() 
print(my_list)  # [10, 20, 30, 40]
```

6. **Listeyi ters çevirme**:

```python
reversed_list = my_list[::-1]  # Listeyi ters döndürür
```

7. **split() Metodu**:

```python
text = "Python dilinde programlama"
word_list = text.split()
print(word_list)  # ['Python', 'dilinde', 'programlama']
```

## Setler

Set'ler, tekrarsız ve sırasız elemanlardan oluşan koleksiyonlardır. Setler, veri tiplerinin tekrarlamasını önler.

### Set Tanımlamak

```python
my_set = {1, 2, 3, 4, 4, 5}  # 4 tekrarlı olduğu için teke indirilir
print(my_set)  # {1, 2, 3, 4, 5}
```

### Set Metotları

- **add()**: Set'e eleman ekler.
- **remove()**: Set'ten eleman siler.
- **union()**: İki seti birleştirir.
- **intersection()**: İki setin ortak elemanlarını döndürür.

Örnek:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))         # {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # {3}
```

## Tuple'lar

Tuple'lar, listeler gibi sıralıdır, ancak **değiştirilemez** (immutable) veri yapılarıdır.

### Tuple Tanımlamak

```python
my_tuple = (1, 2, 3)
print(my_tuple[0])  # 1
```

### Tuple Metotları

- **count()**: Belirli bir elemanın kaç kez geçtiğini döndürür.
- **index()**: Belirli bir elemanın indeksini döndürür.

Tuple’lar liste gibi dilimlenebilir fakat eleman ekleme, çıkarma işlemi yapılamaz.

## Dictionary'ler

Dictionary'ler, anahtar-değer çiftlerinden oluşan veri yapılarıdır. Anahtarlar benzersizdir ve her anahtar bir değerle ilişkilidir.

### Dictionary Tanımlamak

```python
my_dict = {"isim": "Ahmet", "yaş": 25}
print(my_dict["isim"])  # 'Ahmet'
```

 Şimdi de bir anahtarın sözlükte olup olmadığını nasıl kontrol edeceğimize bakalım:

```python
"isim" in my_dict
#True
"adres" in my_dict
#False
```

Eğer anahtar sözlükte varsa, Python **True** döner. Aksi takdirde, **False** döner. Bir sözlüğün tüm anahtarlarını listelemek isterseniz, bunu şu şekilde yapabilirsiniz:

```python
my_dict.keys()
```
### Dictionary Metotları

- **keys()**: Tüm anahtarları döndürür.
- **values()**: Tüm değerleri döndürür.
- **items()**: Anahtar-değer çiftlerini döndürür.
- **get()**: Anahtarın değerini döndürür.

Örnek:

```python
my_dict = {"isim": "Ali", "yaş": 30}
print(my_dict.get("isim"))  # 'Ali'
```

Özet:
- **List**: Sıralı, değiştirilebilir, tekrar eden elemanlara izin verir.
- **Tuple**: Sıralı, değiştirilemez, tekrar eden elemanlara izin verir.
- **Set**: Sırasız, değiştirilebilir, tekrar eden elemanlara izin vermez.
- **Dictionary**: Sırasız, anahtar-değer çiftlerinden oluşur, anahtarlar benzersizdir.
---

# Mantıksal ve Atama Operatörleri

Python'da atama ve karşılaştırma işlemleri için kullanılan operatörler:

## Atama Operatörleri

- **=**: Değer atar.
- **+=**: Bir değeri ekleyerek atar (ör. `a += 5` ifadesi, `a = a + 5` ile aynıdır).
- **-=**: Bir değeri çıkararak atar (ör. `a -= 5` ifadesi, `a = a - 5` ile aynıdır).
- ***=**: Bir değerle çarparak atar (ör. `a *= 5` ifadesi, `a = a * 5` ile aynıdır).
- **/=**: Bir değere bölerek atar (ör. `a /= 5` ifadesi, `a = a / 5` ile aynıdır).
- **%=**: Modülüs değerini atar (ör. `a %= 5` ifadesi, `a = a % 5` ile aynıdır).
-  *=:  Üs alarak atar (ör. `a **= 2`  ifadesi, `a = a ** 2` ile aynıdır).
- **//=**: Taban bölme sonucu atar (ör. `a //= 3` ifadesi, `a = a // 3` ile aynıdır).

## Karşılaştırma Operatörleri

- == :Eşit mi?
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

Else, önceden belirttiğimiz tüm koşullar gerçekleşmediyse diğer durumunu ifadeyi yazarak belirtilir. Bu ifadeden sonra koşul yazılmaz.

````python
a=100
b=200
if b > a :
  print("b, a'dan büyüktür.")
else:
  print("a, b'den büyük ya da eşittir.")
  
`````
Yukarıdaki örnekte ilk koşul doğru değil elif koşulu da doğru değil bu yüzden else koşuluna gidiyoruz ve "a'nın b'den büyük olduğunu" yazdırıyoruz.
### Elif (Else If)

Birden fazla koşul kontrol etmek istiyorsak, **`elif`** anahtar kelimesini kullanabiliriz. İlk koşul sağlanmazsa, `elif` ile kontrol edilen koşul denenir.

```python
a=100
b=100
if b > a: #bu koşulu kontrol eder doğru olmadığı için diğer koşula geçer.
  print("b, a'dan büyüktür.")
elif a == b: #bu koşulu doğru sağlar.
  print("a, b'ye eşittir.")
else: #diğer durumlar 
   print("a, b'den büyüktür.")
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
