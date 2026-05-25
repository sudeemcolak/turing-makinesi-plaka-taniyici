class TuringMakinesi:
    def __init__(self, giris_metni):
        # Bandın sonuna boşluk (blank) sembolü eklenir.
        # Turing Makinesi mantığında girdi bittikten sonra boşluk sembolü gelir.
        self.bant = list(giris_metni) + ['_']
        self.kafa = 0
        self.durum = 'q0'
        self.kabul_durumu = 'q7'  
        self.red_durumu = 'RED'

        # Geçiş tablosu: q0-q6 arası durum geçişleri
        self.gecis_tablosu = {
            'q0': {'N': 'q1'},   # 1. Rakam okundu -> q1
            'q1': {'N': 'q2'},   # 2. Rakam okundu -> q2
            'q2': {'L': 'q3'},   # 1. Harf okundu   -> q3
            'q3': {'L': 'q4'},   # 2. Harf okundu   -> q4
            'q4': {'N': 'q5'},   # 3. Rakam okundu -> q5
            'q5': {'N': 'q6'},   # 4. Rakam okundu -> q6
            'q6': {'N': 'q7'},   # 5. Rakam okundu -> q7 (Kabul adımı öncesi)
            'q7': {'_': 'KABUL'}  # q7'de boşluk okunursa işlem başarıyla biter
        }

    def sembol_tipini_bul(self, karakter):
        # Rakam kontrolü (0-9)
        if karakter.isdigit():
            return 'N'
        # "küçük harf kabul edilmez" kuralı için isupper() ve isalpha() birlikte elenir
        elif karakter.isalpha() and karakter.isupper() and karakter.isascii():
            return 'L'
        # Boşluk sembolü
        elif karakter == '_':
            return '_'
        else:
            return '?' # Tanımsız karakter tipi

    def banti_yazdir(self):
        bant_metni = ''.join(self.bant)
        kafa_gosterimi = [' '] * len(self.bant)
        if self.kafa < len(kafa_gosterimi):
            kafa_gosterimi[self.kafa] = '^'
        print(f"Bant           : {bant_metni}")
        print(f"Kafa Konumu    : {''.join(kafa_gosterimi)}")

    def adim_calistir(self):
        mevcut_sembol = self.bant[self.kafa]
        sembol_tipi = self.sembol_tipini_bul(mevcut_sembol)

        print("\n" + "-"*40)
        print(f"Mevcut Durum   : {self.durum}")
        print(f"Okunan Sembol  : '{mevcut_sembol}' (Tip: {sembol_tipi})")
        self.banti_yazdir()

        # Geçiş kontrolü
        if self.durum in self.gecis_tablosu and sembol_tipi in self.gecis_tablosu[self.durum]:
            yeni_durum = self.gecis_tablosu[self.durum][sembol_tipi]
            
            if yeni_durum == 'KABUL':
                self.durum = self.kabul_durumu  # q7'de kalıp döngüyü bitirme 
                print("Kafa Hareketi  : - (Durdu)")
                return True 

            print(f"Kafa Hareketi  : R (Sağa) -> Yeni Durum: {yeni_durum}")
            self.durum = yeni_durum
            self.kafa += 1
        else:
            print(f"HATA: {self.durum} durumunda '{mevcut_sembol}' sembolü için geçiş yok!")
            self.durum = self.red_durumu

    def calistir(self):
        print("\n" + "="*15 + " TURING MAKİNESİ SİMÜLASYONU BAŞLADI " + "="*15)
        
        # q7'de boşluk kontrolü yapılana veya RED durumuna düşene kadar çalışır
        while self.durum != self.red_durumu:
            # Eğer q7 durumundaysak ve bantta boşluk varsa kabul edip bitiriyoruz
            if self.durum == self.kabul_durumu and self.bant[self.kafa] == '_':
                self.adim_calistir()
                break
            
            if self.durum == self.kabul_durumu and self.bant[self.kafa] != '_':
                # q7'ye ulaşıldı ama fazladan karakter var durumu
                print(f"\nHATA: Format sonrasında fazladan karakter algılandı: '{self.bant[self.kafa]}'")
                self.durum = self.red_durumu
                break
                
            self.adim_calistir()

        print("\n---------------------------------")

        # Sonuç
        if self.durum == self.kabul_durumu:
            print("SONUC : KABUL")

        else:
            print("SONUC : RED")

# Kullanıcıdan plaka bilgisi alınır
plaka = input("Plaka giriniz (NNLLNNN): ")

# Turing Makinesi oluşturulur
tm = TuringMakinesi(plaka)

# Makine çalıştırılır
tm.calistir()
