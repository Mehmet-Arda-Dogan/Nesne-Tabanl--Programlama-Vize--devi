class Kitap:
    def __init__(self, ad, yazar, kitapID):
        self.ad = ad
        self.yazar = yazar
        self.kitapID = kitapID
        self.durum = "Müsait" 

    def durum_guncelle(self, durum):
        self.durum = durum


class Üye:
    def __init__(self, ad, soyad, telefon_numarası, uye_id):
        self.ad = ad
        self.soyad = soyad
        self.telefon_numarası = telefon_numarası
        self.uye_id = uye_id  

    def uye_bilgisi(self):
        return f"Üye ID: {self.uye_id} | Ad: {self.ad} | Soyad: {self.soyad} | Telefon: {self.telefon_numarası}"


class Ödünç:
    def __init__(self):
        self.odunc_islemleri = [] 

    def odunc_al(self, uye, kitap):
        if kitap.durum == "Müsait":
            kitap.durum_guncelle("Ödünç Alındı")
            self.odunc_islemleri.append({"Üye": uye, "Kitap": kitap, "Durum": "Alındı"})
            print(f"{uye.ad} {uye.soyad} üyemiz {kitap.ad} isimli kitabı ödünç almıştır.")
        else:
            print(f"{kitap.ad} kitabımız başka bir üye tarafından ödünç alınmıştır.")

    def iade_et(self, uye, kitap):
        for odunc in self.odunc_islemleri:
            if odunc["Üye"] == uye and odunc["Kitap"] == kitap:
                kitap.durum_guncelle("Müsait")
                self.odunc_islemleri.remove(odunc)
                print(f"{uye.ad} {uye.soyad} isimli üyemiz {kitap.ad} kitabını iade etmiştir.")
                return
        print("Üyemizin böyle bir kaydı bulunmamaktadır.")


kitaplar = [
    Kitap("Denizler Altında Yirmi Bin Fersah", "Jules Verne", "A1"),
    Kitap("Zamanın Dışından Gelen Gölge", "H.P Lovecraft", "B2"),
    Kitap("Hayvan Çiftliği", "George Orwell", "C3"),
    Kitap("Kan Meridyeni", "Cormac McCarthy", "D4")
]

üyeler = [
    Üye("Samet", "Aktaş", "05395467887", "1A"),
    Üye("Duhan", "Şimşek", "05764645613", "1B"),
    Üye("Elif", "Şimşek", "05552340908", "3C"),
    Üye("Büşra", "Odabaş", "05359725671", "4D"),
]

# ---------------------------------------------------------
def kitaplari_listele():
    print("\nMevcut Kitaplar:")
    for kitap in kitaplar:
        print(f"ID: {kitap.kitapID} | Ad: {kitap.ad} | Yazar: {kitap.yazar} | Durum: {kitap.durum}")


def musterileri_listele():
    print("\nMevcut Üyeler:")
    for uye in üyeler:
        print(f"ID: {uye.uye_id} | Ad: {uye.ad} {uye.soyad} | Telefon: {uye.telefon_numarası}")


def main():
    odunc_sistemi = Ödünç()  

    while True:
        print("\n=== Kütüphane Yönetim Sistemi ===")
        print("1. Kitapları Listele")
        print("2. Üyeleri Listele")
        print("3. Kitap Ödünç Al")
        print("4. Kitap İade Et")
        print("5. Ödünç Bilgilerini Görüntüle")
        print("6. Çıkış")

        secim = input("Seçiminizi yapın (1-6): ")

        if secim == "1":
            kitaplari_listele()
        elif secim == "2":
            musterileri_listele()
        elif secim == "3":
            kitap_id = input("Ödünç alınacak kitabın ID'sini girin: ")
            uye_id = input("Üye ID'sini girin: ")

            kitap = next((k for k in kitaplar if k.kitapID == kitap_id), None)
            uye = next((u for u in üyeler if u.uye_id == uye_id), None)

            if kitap and uye:
                odunc_sistemi.odunc_al(uye, kitap)
            else:
                print("Kitap veya üye bulunamadı.")
        elif secim == "4":
            kitap_id = input("İade edilecek kitabın ID'sini girin: ")
            uye_id = input("Üye ID'sini girin: ")

            kitap = next((k for k in kitaplar if k.kitapID == kitap_id), None)
            uye = next((u for u in üyeler if u.uye_id == uye_id), None)

            if kitap and uye:
                odunc_sistemi.iade_et(uye, kitap)
            else:
                print("Kitap veya üye bulunamadı.")
        elif secim == "5":
            print("\nÖdünç İşlemleri:")
            for odunc in odunc_sistemi.odunc_islemleri:
                print(f"{odunc['Üye'].ad} {odunc['Üye'].soyad} - {odunc['Kitap'].ad} ({odunc['Durum']})")
        elif secim == "6":
            print("Bizi tercih ettiğiniz için teşekkürler.")
            break
        else:
            print("Lütfen konsoldaki numaralardan birini tuşlayın.")


if __name__ == "__main__":
    main()
