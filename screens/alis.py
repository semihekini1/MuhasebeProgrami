import customtkinter as ctk
from tkinter import ttk
from datetime import datetime

from database import (
    carileri_getir,
    urunleri_getir,
    alis_ekle,
    alis_detay_ekle,
    stok_artir,
    cari_alacak_artir
)



class AlisApp(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)


        self.pack(
            fill="both",
            expand=True
        )


        self.sepet = []



        ctk.CTkLabel(
            self,
            text="📥 ALIŞ",
            font=("Arial",26,"bold")
        ).pack(
            pady=15
        )



        self.cari_box = ctk.CTkComboBox(
            self,
            width=250
        )

        self.cari_box.pack(
            pady=5
        )



        self.urun_box = ctk.CTkComboBox(
            self,
            width=250
        )

        self.urun_box.pack(
            pady=5
        )



        self.miktar = ctk.CTkEntry(
            self,
            placeholder_text="Miktar"
        )

        self.miktar.pack(
            pady=5
        )



        self.fiyat = ctk.CTkEntry(
            self,
            placeholder_text="Alış Fiyatı"
        )

        self.fiyat.pack(
            pady=5
        )



        ctk.CTkButton(
            self,
            text="Sepete Ekle",
            command=self.sepete_ekle
        ).pack(
            pady=10
        )



        self.tablo = ttk.Treeview(
            self,
            columns=(
                "urun",
                "miktar",
                "fiyat",
                "tutar"
            ),
            show="headings"
        )


        for kolon,baslik in [

            ("urun","Ürün"),

            ("miktar","Miktar"),

            ("fiyat","Fiyat"),

            ("tutar","Tutar")

        ]:

            self.tablo.heading(
                kolon,
                text=baslik
            )


        self.tablo.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )



        self.toplam = ctk.CTkLabel(
            self,
            text="Toplam: 0 TL",
            font=("Arial",20,"bold")
        )

        self.toplam.pack(
            pady=10
        )



        ctk.CTkButton(
            self,
            text="ALIŞI KAYDET",
            command=self.kaydet
        ).pack(
            pady=10
        )


        self.cari_listesi = carileri_getir()

        self.urun_listesi = urunleri_getir()


        self.cari_box.configure(
            values=[
                f"{x[0]} - {x[2]}"
                for x in self.cari_listesi
            ]
        )


        self.urun_box.configure(
            values=[
                f"{x[0]} - {x[3]}"
                for x in self.urun_listesi
            ]
        )




    def sepete_ekle(self):

        urun = self.urun_box.get()

        miktar = float(
            self.miktar.get()
        )

        fiyat = float(
            self.fiyat.get()
        )


        urun_id = int(
            urun.split("-")[0]
        )


        urun_adi = urun.split("-")[1]


        tutar = miktar * fiyat


        self.sepet.append(
            (
                urun_id,
                miktar,
                fiyat,
                tutar,
                urun_adi
            )
        )


        self.tablo.insert(
            "",
            "end",
            values=(
                urun_adi,
                miktar,
                fiyat,
                tutar
            )
        )


        self.hesapla()




    def hesapla(self):

        toplam = sum(
            x[3]
            for x in self.sepet
        )


        self.toplam.configure(
            text=f"Toplam: {toplam} TL"
        )





    def kaydet(self):

        cari = self.cari_box.get()

        cari_id = int(
            cari.split("-")[0]
        )


        toplam = sum(
            x[3]
            for x in self.sepet
        )


        tarih = datetime.now().strftime(
            "%Y-%m-%d"
        )


        alis_id = alis_ekle(
            cari_id,
            tarih,
            toplam
        )


        for urun in self.sepet:


            stok_artir(
                urun[0],
                urun[1]
            )


            alis_detay_ekle(
                alis_id,
                urun[0],
                urun[1],
                urun[2],
                urun[3]
            )


        cari_alacak_artir(
            cari_id,
            toplam
        )


        self.sepet.clear()

        self.tablo.delete(
            *self.tablo.get_children()
        )


        self.hesapla()