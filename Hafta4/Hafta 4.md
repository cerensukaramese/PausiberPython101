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
def topla(a=1, b=2):
    return a + b

print(topla(b=4, a=5))  # Çıktı: 9
```

Eğer bir fonksiyon parametreleri için varsayılan değerler belirlenmişse, argümanları atlamanız mümkün olur. Örneğin:

```python
print(topla())  # Çıktı: 3
```

Bu durumda `a` ve `b` varsayılan olarak 1 ve 2 değerlerini alır.

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

### DRY (Don’t Repeat Yourself)

Tekrarlayan kodlardan kaçınmak için aynı kod parçasını bir fonksiyon içine almanız önerilir. Böylece, tek bir yerde değişiklik yaparak tüm kodunuzu güncel tutabilirsiniz. Bu, kodunuzu daha okunabilir ve bakımı daha kolay hale getirir.