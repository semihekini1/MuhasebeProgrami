import customtkinter as ctk
from tkinter import ttk

from database import (
    satis_gecmisi_getir,
    satis_detaylarini_getir
)



class SatisGecmisiApp(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)


        self.pack(
            fill="both",
            expand=True
        )


        ctk.CTkLabel(
            self,
            text="📋 SATIŞ GEÇMİŞİ",
            font=("Arial",26,"bold")
        ).pack(
            pady=15
        )


        # SATIŞ LİSTESİ

        self.satis_tablo = ttk.Treeview(

            self,

            columns=(

                "id",
                "tarih",
                "cari",
                "toplam"

            ),

            show="headings"

        )


        for kolon, baslik in [

            ("id","No"),

            ("tarih","Tarih"),

            ("cari","Cari"),

            ("toplam","Toplam")

        ]:

            self.satis_tablo.heading(

                kolon,

                text=baslik

            )


            self.satis_tablo.column(

                kolon,

                width=150

            )


        self.satis_tablo.pack(

            fill="x",

            padx=20,

            pady=10

        )


        self.satis_tablo.bind(

            "<<TreeviewSelect>>",

            self.detay_getir

        )



        ctk.CTkLabel(

            self,

            text="SATIŞ DETAYI",

            font=("Arial",20,"bold")

        ).pack(

            pady=10

        )



        # DETAY TABLOSU


        self.detay_tablo = ttk.Treeview(

            self,

            columns=(

                "urun",

                "miktar",

                "fiyat",

                "tutar"

            ),

            show="headings"

        )


        for kolon, baslik in [

            ("urun","Ürün"),

            ("miktar","Miktar"),

            ("fiyat","Fiyat"),

            ("tutar","Tutar")

        ]:


            self.detay_tablo.heading(

                kolon,

                text=baslik

            )


            self.detay_tablo.column(

                kolon,

                width=150

            )



        self.detay_tablo.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=10

        )


        self.yukle()




    def yukle(self):


        for satir in self.satis_tablo.get_children():

            self.satis_tablo.delete(satir)



        satislar = satis_gecmisi_getir()



        for satis in satislar:


            self.satis_tablo.insert(

                "",

                "end",

                values=satis

            )





    def detay_getir(self,event):


        secili = self.satis_tablo.selection()



        if not secili:

            return



        secilen = self.satis_tablo.item(

            secili[0]

        )


        satis_id = secilen["values"][0]



        for satir in self.detay_tablo.get_children():

            self.detay_tablo.delete(satir)



        detaylar = satis_detaylarini_getir(

            satis_id

        )



        for detay in detaylar:


            self.detay_tablo.insert(

                "",

                "end",

                values=detay

            )