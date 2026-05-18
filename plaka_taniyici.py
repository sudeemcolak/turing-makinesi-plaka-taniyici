
class TuringMakinesi:

    def __init__(self, giris_metni):

        # Bandın sonuna boşluk(blank) sembolü eklenir
        self.bant = list(giris_metni) + ['_'] # Turing Makinesi mantığında bant teorik olarak sonsuzdur ve girişin nerede bittiğini anlayabilmek için kullanılır.

        # Okuma/Yazma kafası başlangıç konumu
        self.kafa = 0

        # Durumlar
        self.durum = 'q0'
        self.kabul_durumu = 'q_accept'
        self.red_durumu = 'q_reject'

        # N -> Rakam
        # L -> Büyük Harf
        # _ -> Boşluk

        self.gecis_tablosu = {

            'q0': {'N': 'q1'},   # ilk rakam
            'q1': {'N': 'q2'},   # ikinci rakam

            'q2': {'L': 'q3'},   # ilk harf
            'q3': {'L': 'q4'},   # ikinci harf

            'q4': {'N': 'q5'},   # üçüncü karakter (rakam)
            'q5': {'N': 'q6'},   # dördüncü karakter (rakam)
            'q6': {'N': 'q7'},   # beşinci karakter (rakam)

            'q7': {'_': 'q_accept'}  # giriş sonu kontrolü
        }

    # Okunan karakterin tipini belirler
    def sembol_tipini_bul(self, karakter):

        # Rakam kontrolü
        if karakter.isdigit():
            return 'N'

        # Büyük harf kontrolü
        elif karakter.isalpha() and karakter.isupper():
            return 'L'

        # Boşluk sembolü
        elif karakter == '_':
            return '_'

        # Geçersiz karakter
        else:
            return '?'  # Tanımsız karakter tipi

    # Bant görüntüsünü yazdırır
    def banti_yazdir(self):

        bant_metni = ''.join(self.bant) # Bant içeriğini listeden stringe çevirir

        kafa_gosterimi = [' '] * len(self.bant)

        if self.kafa < len(kafa_gosterimi): #kafa bant sınırları içinde ise
            kafa_gosterimi[self.kafa] = '^' # Kafanın bulunduğu konumu göstermek için '^' sembolü kullanılır

        print("Bant :", bant_metni)
        print("       " + ''.join(kafa_gosterimi))

    # Bir adım çalıştırır
    def adim_calistir(self):

        mevcut_sembol = self.bant[self.kafa]

        # Sembol tipini öğren
        sembol_tipi = self.sembol_tipini_bul(mevcut_sembol)

        print("\n--------------------------------")
        print(f"Durum          : {self.durum}")
        print(f"Okunan Sembol  : {mevcut_sembol}")
        print(f"Kafa Pozisyonu : {self.kafa}")
        print("Kafa Hareketi  : R (Sağa)")

        self.banti_yazdir()

        # Geçiş tablosunda uygun geçiş var mı?
        if (self.durum in self.gecis_tablosu and
                sembol_tipi in self.gecis_tablosu[self.durum]):

            # Yeni duruma geç
            self.durum = self.gecis_tablosu[self.durum][sembol_tipi]

            # Kafayı sağa kaydır
            self.kafa += 1

        else:
            # Tanımsız geçiş -> RED
            self.durum = self.red_durumu

    # Makineyi çalıştırır
    def calistir(self):

        print("\n= TURING MAKINESI BASLATILDI =")

        # Kabul veya RED durumuna ulaşana kadar devam et
        while (self.durum != self.kabul_durumu and
               self.durum != self.red_durumu):

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