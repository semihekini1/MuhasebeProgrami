import customtkinter as ctk
from tkinter import ttk
from datetime import datetime

from database import (
    kasa_ekle,
    kasa_getir,
    kasa_bakiye
)



class KasaApp(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)


        self.pack(
            fill="both",
            expand=True
        )


        ctk.CTkLabel(

            self,

            text="💰 KASA",

            font=("Arial",26,"bold")

        ).pack(
            pady=20
        )



        form = ctk.CTkFrame(self)

        form.pack(
            pady=10
        )



        ctk.CTkLabel(

            form,

            text="Tür"

        ).grid(

            row=0,

            column=0,

            padx=5,

            pady=5

        )



        self.tur = ctk.CTkComboBox(

            form,

            values=[

                "Giriş",

                "Çıkış"

            ]

        )


        self.tur.grid(

            row=0,

            column=1,

            padx=5,

            pady=5

        )


        self.tur.set(
            "Giriş"
        )



        ctk.CTkLabel(

            form,

            text="Açıklama"

        ).grid(

            row=1,

            column=0,

            padx=5,

            pady=5

        )



        self.aciklama = ctk.CTkEntry(

            form,

            width=250

        )


        self.aciklama.grid(

            row=1,

            column=1,

            padx=5,

            pady=5

        )




        ctk.CTkLabel(

            form,

            text="Tutar"

        ).grid(

            row=2,

            column=0,

            padx=5,

            pady=5

        )



        self.tutar = ctk.CTkEntry(

            form

        )


        self.tutar.grid(

            row=2,

            column=1,

            padx=5,

            pady=5

        )




        ctk.CTkButton(

            self,

            text="Kaydet",

            command=self.kaydet

        ).pack(

            pady=10

        )




        self.bakiye = ctk.CTkLabel(

            self,

            text="Bakiye: 0 TL",

            font=("Arial",20,"bold")

        )


        self.bakiye.pack(

            pady=10

        )




        self.tablo = ttk.Treeview(

            self,

            columns=(

                "id",

                "tarih",

                "aciklama",

                "tur",

                "tutar"

            ),

            show="headings"

        )



        for kolon,baslik in [

            ("id","No"),

            ("tarih","Tarih"),

            ("aciklama","Açıklama"),

            ("tur","Tür"),

            ("tutar","Tutar")

        ]:


            self.tablo.heading(

                kolon,

                text=baslik

            )


            self.tablo.column(

                kolon,

                width=130

            )



        self.tablo.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=20

        )


        self.yukle()




    def kaydet(self):


        tarih = datetime.now().strftime(

            "%Y-%m-%d %H:%M"

        )


        kasa_ekle(

            tarih,

            self.aciklama.get(),

            self.tur.get(),

            float(

                self.tutar.get() or 0

            )

        )


        self.aciklama.delete(

            0,

            "end"

        )


        self.tutar.delete(

            0,

            "end"

        )


        self.yukle()




    def yukle(self):


        for satir in self.tablo.get_children():

            self.tablo.delete(satir)



        for veri in kasa_getir():


            self.tablo.insert(

                "",

                "end",

                values=veri

            )



        self.bakiye.configure(

            text=f"Bakiye: {kasa_bakiye()} TL"

        )