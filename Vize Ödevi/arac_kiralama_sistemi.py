class Arac:
    def __init__(self, arac_id, marka, model):
        self.arac_id = arac_id  # Bu satırı düzelttik
        self.marka = marka
        self.model = model
        self.kiralama_durumu = False

    def arac_durumu_guncelle(self, durum):
        self.kiralama_durumu = durum


class Musteri:
    def __init__(self, ad, soyad, musterıID, telefon_numarasi):
        self.ad = ad
        self.soyad = soyad
        self.musterıID = musterıID
        self.telefon_numarasi = telefon_numarasi


class Kiralama:
    def __init__(self):
        self.kiralamalar = []

    def kiralama_yap(self, musteri, arac):
        if arac.kiralama_durumu:
            print(f"Araç {arac.marka} {arac.model} zaten başka bir müşteri tarafından kiralanmış.")
        else:
            arac.arac_durumu_guncelle(True)
            self.kiralamalar.append({"musteri": musteri, "arac": arac})
            print(f"{musteri.ad} {musteri.soyad} adlı müşteri {arac.marka} {arac.model} aracını kiraladı.")

    def kiralama_iptal_et(self, musteri, arac):
        for kiralama in self.kiralamalar:
            if kiralama["musteri"] == musteri and kiralama["arac"] == arac:
                arac.arac_durumu_guncelle(False)
                self.kiralamalar.remove(kiralama)
                print(f"{musteri.ad} {musteri.soyad} adlı müşterinin {arac.marka} {arac.model} araç kiralaması iptal edildi.")
                return
        print("Kayıtlarda böyle bir kira yok.")


araclar = [
    Arac("A1", "Volkswagen", "Jetta"),
    Arac("B2", "Renault", "Megan"),
    Arac("C3", "Ford", "Mustang"),
    Arac("D4", "Toyota", "Land Cruiser")
]

musteriler = [
    Musteri("Samet", "Efe", "1A", "05344657890"),
    Musteri("Faruk", "Citak", "2B", "05897561234"),
    Musteri("Enes", "Ayyıldız", "3C", "05439876540"),
    Musteri("Arda", "Arslan", "4D", "05457456785")
]

kiralama_sistemi = Kiralama()


def araclari_listele():
    print("\nMevcut Araçlar:")
    for arac in araclar:
        durum = "Kiralandı" if arac.kiralama_durumu else "Müsait"
        print(f"ID: {arac.arac_id} | Marka: {arac.marka} | Model: {arac.model} | Durum: {durum}")  # arac_id'yi doğru yazdık


def musterileri_listele():
    print("\nMevcut Müşteriler:")
    for musteri in musteriler:
        print(f"ID: {musteri.musterıID} | Ad: {musteri.ad} | Soyad: {musteri.soyad} | Telefon: {musteri.telefon_numarasi}")


def arayuz():
    while True:
        print("\n=== Araç Kiralama Sistemi ===")
        print("1. Araçları Listele")
        print("2. Müşterileri Listele")
        print("3. Araç Kirala")
        print("4. Kiralama İptal Et")
        print("5. Çıkış Yap")

        secim = input("Seçiminizi yapın (1-5): ")

        if secim == "1":
            araclari_listele()

        elif secim == "2":
            musterileri_listele()

        elif secim == "3":
            musterileri_listele()
            musteri_id = input("Kiralamak isteyen müşterinin ID'sini girin: ")
            araclari_listele()
            arac_id = input("Kiralanacak aracın ID'sini girin: ")

            musteri = next((m for m in musteriler if m.musterıID == musteri_id), None)
            arac = next((a for a in araclar if a.arac_id == arac_id), None)

            if musteri and arac:
                kiralama_sistemi.kiralama_yap(musteri, arac)
            else:
                print("Geçersiz müşteri veya araç seçimi.")

        elif secim == "4":
            musterileri_listele()
            musteri_id = input("Kiralamayı iptal edecek müşterinin ID'sini girin: ")
            araclari_listele()
            arac_id = input("İptal edilecek aracın ID'sini girin: ")

            musteri = next((m for m in musteriler if m.musterıID == musteri_id), None)
            arac = next((a for a in araclar if a.arac_id == arac_id), None)

            if musteri and arac:
                kiralama_sistemi.kiralama_iptal_et(musteri, arac)
            else:
                print("Geçersiz müşteri veya araç seçimi.")

        elif secim == "5":
            print("Bizi tercih ettiğiniz için teşekkür ederiz.")
            break

        else:
            print("Lütfen konsoldaki numaralardan birini tuşlayın.")


arayuz()
