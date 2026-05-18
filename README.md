# Turing Makinesi ile Araç Plaka Formatı Tanıyıcı

BİL312 Özdevinirler Kuramı Ödevi

Bu proje, Python programlama dili kullanılarak geliştirilmiş deterministik bir Turing Makinesi simülatörüdür. Program, araç plakalarının belirli bir formata uygun olup olmadığını kontrol etmektedir.

---

# Projenin Amacı

Bu çalışmanın amacı:

* Turing Makinesi mantığını simüle etmek
* Durum tabanlı doğrulama sistemi geliştirmek
* Karakter bazlı analiz gerçekleştirmek
* Belirli bir dil (format) tanımak
* Bant (Tape) yapısını modellemek
* Geçiş fonksiyonları ile kontrol sağlamak

olarak belirlenmiştir.

---

# Kullanılan Teknolojiler

* Python
* Tek Bantlı Turing Makinesi Modeli

---

# Programın Özellikleri

Program aşağıdaki işlemleri gerçekleştirmektedir:

* Kullanıcıdan plaka bilgisi alma
* Girdiyi bant yapısına yerleştirme
* Karakterleri soldan sağa okuma
* Her karakter için durum geçişi gerçekleştirme
* Büyük harf ve rakam kontrolü yapma
* Fazladan veya eksik karakterleri tespit etme
* Geçersiz girişlerde RED durumuna geçme
* Her adımda:

  * mevcut durum
  * okunan sembol
  * kafa hareketi
  * kafa pozisyonu
  * bant içeriği

bilgilerini ekrana yazdırma.

---

# Tanınan Dil

Program aşağıdaki formatı tanımaktadır:

```text
NNLLNNN
```

Burada:

* `N` → Rakam (0–9)
* `L` → Büyük Harf (A–Z)

---

# Geçerli Girdi Örnekleri

```text
55AB123
34TR456
06AA789
81ZX321
99KK999
```

---

# Geçersiz Girdi Örnekleri

```text
5AB123
555AB12
34A1234
AB34123
55ab123
```

---

# Bant Formatı

Program girdiyi aşağıdaki bant yapısına dönüştürmektedir:

```text
55AB123_
```

Burada:

* `_` → boşluk (blank) sembolünü temsil eder
* Bant sonunu belirtmek için kullanılmaktadır

---

# Kullanılan Durumlar

| Durum    | Açıklama                           |
| -------- | ---------------------------------- |
| q0       | İlk rakam kontrolü                 |
| q1       | İkinci rakam kontrolü              |
| q2       | İlk büyük harf kontrolü            |
| q3       | İkinci büyük harf kontrolü         |
| q4       | İlk son rakam kontrolü             |
| q5       | İkinci son rakam kontrolü          |
| q6       | Üçüncü son rakam kontrolü          |
| q7       | Giriş sonu kontrolü                |
| q_accept | Kabul durumu                       |
| q_reject | Hata / RED durumu                  |

---

# Çalışma Mantığı

Program aşağıdaki adımları takip etmektedir:

1. İlk karakterin rakam olup olmadığı kontrol edilir
2. İkinci karakterin rakam olup olmadığı kontrol edilir
3. Üçüncü karakterin büyük harf olup olmadığı kontrol edilir
4. Dördüncü karakterin büyük harf olup olmadığı kontrol edilir
5. Son üç karakterin rakam olup olmadığı kontrol edilir
6. Bant sonunda boşluk sembolü (`_`) kontrol edilir
7. Fazladan karakter varsa RED durumuna geçilir
8. Tüm kontroller başarılıysa makine kabul durumuna geçer

---

# Örnek Çalışma

## Girdi

```text
55AB123
```

## Bant

```text
55AB123_
```

## Çıktı

```text
SONUC : KABUL
```

---

# Geçersiz Örnek

## Girdi

```text
55ab123
```

## Çıktı

```text
HATA : Ucuncu karakter buyuk harf olmalidir.
SONUC : RED
```

---

# Çalıştırma

Python kurulu olduktan sonra terminal üzerinden aşağıdaki komut çalıştırılır:

```bash
python3 plaka_taniyici.py
```

---

