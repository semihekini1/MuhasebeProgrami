import customtkinter as ctk
from tkinter import ttk
from datetime import datetime

from database import (
    carileri_getir,
    urunleri_getir,
    satis_ekle,
    satis_detay_ekle,
    stok_dus,
    cari_borc_artir
)


class SatisApp(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.pack(
            fill="both",
            expand=True
        )

        self.sepet = []


        ctk.CTkLabel(
            self,
            text="🧾 SATIŞ YÖNETİMİ",
            font=("Arial",26,"bold")
        ).pack(pady=20)



        ust = ctk.CTkFrame(self)

        ust.pack(pady=10)



        # CARİ

        ctk.CTkLabel(
            ust,
            text="Cari"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )


        self.cari_box = ctk.CTkComboBox(
            ust,
            width=250
        )

        self.cari_box.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )



        # ÜRÜN

        ctk.CTkLabel(
            ust,
            text="Ürün"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )


        self.urun_box = ctk.CTkComboBox(
            ust,
            width=250
        )

        self.urun_box.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )



        self.miktar = ctk.CTkEntry(
            ust,
            placeholder_text="Miktar"
        )

        self.miktar.grid(
            row=2,
            column=0,
            padx=5,
            pady=5
        )


        self.fiyat = ctk.CTkEntry(
            ust,
            placeholder_text="Fiyat"
        )

        self.fiyat.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )



        ctk.CTkButton(
            ust,
            text="Sepete Ekle",
            command=self.sepete_ekle
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=10
        )



        # TABLO

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


        for kolon in [
            "urun",
            "miktar",
            "fiyat",
            "tutar"
        ]:

            self.tablo.heading(
                kolon,
                text=kolon.upper()
            )


        self.tablo.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )



        self.toplam = ctk.CTkLabel(
            self,
            text="Toplam: 0 TL",
            font=("Arial",20,"bold")
        )

        self.toplam.pack()



        ctk.CTkButton(
            self,
            text="💾 Satışı Kaydet",
            command=self.kaydet
        ).pack(
            pady=15
        )


        self.verileri_yukle()



    def verileri_yukle(self):

        cari_liste = []

        for cari in carileri_getir():

            cari_liste.append(
                f"{cari[0]}-{cari[2]}"
            )


        self.cari_box.configure(
            values=cari_liste
        )



        urun_liste = []

        for urun in urunleri_getir():

            urun_liste.append(
                f"{urun[0]}-{urun[3]}"
            )


        self.urun_box.configure(
            values=urun_liste
        )




    def sepete_ekle(self):

        urun = self.urun_box.get()

        if not urun:
            return


        miktar = float(
            self.miktar.get() or 0
        )


        fiyat = float(
            self.fiyat.get() or 0
        )


        tutar = miktar * fiyat


        self.sepet.append({

            "urun": urun,

            "miktar": miktar,

            "fiyat": fiyat,

            "tutar": tutar

        })


        self.tablo.insert(

            "",

            "end",

            values=(

                urun,

                miktar,

                fiyat,

                tutar

            )

        )


        self.toplam_guncelle()




    def toplam_guncelle(self):

        toplam = 0


        for urun in self.sepet:

            toplam += urun["tutar"]


        self.toplam.configure(

            text=f"Toplam: {toplam} TL"

        )




    def kaydet(self):

        cari = self.cari_box.get()


        if not cari:

            return


        cari_id = int(
            cari.split("-")[0]
        )


        toplam = sum(

            x["tutar"]

            for x in self.sepet

        )


        satis_id = satis_ekle(

            cari_id,

            datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            ),

            toplam

        )


        for urun in self.sepet:


            urun_id = int(
                urun["urun"].split("-")[0]
            )


            satis_detay_ekle(

                satis_id,

                urun_id,

                urun["miktar"],

                urun["fiyat"],

                urun["tutar"]

            )


            stok_dus(

                urun_id,

                urun["miktar"]

            )



        cari_borc_artir(

            cari_id,

            toplam

        )



        self.sepet.clear()



        for satir in self.tablo.get_children():

            self.tablo.delete(satir)



        self.toplam_guncelle()