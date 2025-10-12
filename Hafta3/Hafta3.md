

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
