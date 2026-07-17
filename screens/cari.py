import customtkinter as ctk
from tkinter import ttk

from database import (
    cari_ekle,
    carileri_getir,
    cari_sil
)


class CariApp(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.pack(
            fill="both",
            expand=True
        )

        self.secili_id = None


        ctk.CTkLabel(
            self,
            text="👥 CARİ HESAP YÖNETİMİ",
            font=("Arial",26,"bold")
        ).pack(pady=15)



        # Arama

        self.arama = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Cari ara..."
        )

        self.arama.pack(pady=5)



        ctk.CTkButton(
            self,
            text="🔍 Ara",
            command=self.listele
        ).pack()



        # Form

        form = ctk.CTkFrame(self)

        form.pack(pady=15)



        self.kod = self.alan(
            form,
            "Cari Kodu",
            0,
            0
        )


        self.firma = self.alan(
            form,
            "Firma Adı",
            0,
            1
        )


        self.yetkili = self.alan(
            form,
            "Yetkili",
            1,
            0
        )


        self.telefon = self.alan(
            form,
            "Telefon",
            1,
            1
        )


        self.email = self.alan(
            form,
            "E-Mail",
            2,
            0
        )


        self.vergi = self.alan(
            form,
            "Vergi No",
            2,
            1
        )


        self.borc = self.alan(
            form,
            "Borç",
            3,
            0
        )


        self.alacak = self.alan(
            form,
            "Alacak",
            3,
            1
        )



        # Butonlar

        buton = ctk.CTkFrame(self)

        buton.pack(pady=10)



        ctk.CTkButton(
            buton,
            text="➕ Kaydet",
            command=self.kaydet
        ).grid(
            row=0,
            column=0,
            padx=5
        )


        ctk.CTkButton(
            buton,
            text="🗑 Sil",
            command=self.sil
        ).grid(
            row=0,
            column=1,
            padx=5
        )


        ctk.CTkButton(
            buton,
            text="🧹 Temizle",
            command=self.temizle
        ).grid(
            row=0,
            column=2,
            padx=5
        )



        # Tablo

        self.tablo = ttk.Treeview(
            self,
            columns=(
                "id",
                "kod",
                "firma",
                "telefon",
                "borc",
                "alacak",
                "durum"
            ),
            show="headings"
        )



        basliklar = {

            "id":"ID",
            "kod":"Kod",
            "firma":"Firma",
            "telefon":"Telefon",
            "borc":"Borç",
            "alacak":"Alacak",
            "durum":"Durum"

        }



        for kolon,baslik in basliklar.items():

            self.tablo.heading(
                kolon,
                text=baslik
            )

            self.tablo.column(
                kolon,
                width=100
            )



        self.tablo.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )


        self.tablo.bind(
            "<ButtonRelease-1>",
            self.sec
        )


        self.listele()



    def alan(self,parent,text,row,col):

        e = ctk.CTkEntry(
            parent,
            placeholder_text=text
        )


        e.grid(
            row=row,
            column=col,
            padx=5,
            pady=5
        )


        return e




    def kaydet(self):


        class Cari:
            pass



        cari = Cari()


        cari.cari_kodu = self.kod.get()

        cari.firma_adi = self.firma.get()

        cari.yetkili = self.yetkili.get()

        cari.telefon = self.telefon.get()

        cari.email = self.email.get()

        cari.adres = ""

        cari.vergi_no = self.vergi.get()

        cari.borc = float(
            self.borc.get() or 0
        )

        cari.alacak = float(
            self.alacak.get() or 0
        )



        cari_ekle(cari)


        self.listele()

        self.temizle()




    def listele(self):


        for item in self.tablo.get_children():

            self.tablo.delete(item)



        arama = self.arama.get().lower()



        for cari in carileri_getir():


            if arama:

                if arama not in cari[2].lower():

                    continue



            durum = "Borçlu"


            if cari[9] > cari[8]:

                durum = "Alacaklı"


            elif cari[9] == cari[8]:

                durum = "Dengeli"



            self.tablo.insert(

                "",

                "end",

                values=(

                    cari[0],

                    cari[1],

                    cari[2],

                    cari[4],

                    cari[8],

                    cari[9],

                    durum

                )

            )




    def sec(self,event):

        secilen = self.tablo.selection()


        if secilen:

            veri = self.tablo.item(secilen)


            self.secili_id = veri["values"][0]




    def sil(self):


        if self.secili_id:


            cari_sil(
                self.secili_id
            )


            self.listele()


            self.temizle()




    def temizle(self):


        self.secili_id = None


        for alan in [

            self.kod,
            self.firma,
            self.yetkili,
            self.telefon,
            self.email,
            self.vergi,
            self.borc,
            self.alacak

        ]:

            alan.delete(
                0,
                "end"
            )