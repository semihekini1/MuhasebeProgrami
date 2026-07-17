import customtkinter as ctk
from tkinter import ttk

from models.urun import Urun
from database import (
    urun_ekle,
    urunleri_getir,
    urun_sil,
    urun_guncelle_v2
)


class StokApp(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.pack(fill="both", expand=True)

        self.secili_id = None


        ctk.CTkLabel(
            self,
            text="📦 STOK YÖNETİMİ v2.1",
            font=("Arial",26,"bold")
        ).pack(pady=15)



        # Arama

        self.arama = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Ürün ara..."
        )

        self.arama.pack(pady=5)


        ctk.CTkButton(
            self,
            text="🔍 Ara",
            command=self.listele
        ).pack()



        # Form

        form = ctk.CTkFrame(self)

        form.pack(pady=10)


        self.kod = self.alan(form,"Ürün Kodu",0,0)
        self.barkod = self.alan(form,"Barkod",0,1)

        self.ad = self.alan(form,"Ürün Adı",1,0)
        self.kategori = self.alan(form,"Kategori",1,1)

        self.alis = self.alan(form,"Alış",2,0)
        self.satis = self.alan(form,"Satış",2,1)

        self.kdv = self.alan(form,"KDV %",3,0)
        self.stok = self.alan(form,"Stok",3,1)

        self.kritik = self.alan(
            form,
            "Kritik Stok",
            4,
            0
        )



        # Butonlar

        buton = ctk.CTkFrame(self)

        buton.pack(pady=10)


        ctk.CTkButton(
            buton,
            text="➕ Kaydet",
            command=self.kaydet
        ).grid(row=0,column=0,padx=5)


        ctk.CTkButton(
            buton,
            text="✏ Güncelle",
            command=self.guncelle
        ).grid(row=0,column=1,padx=5)


        ctk.CTkButton(
            buton,
            text="🗑 Sil",
            command=self.sil
        ).grid(row=0,column=2,padx=5)


        ctk.CTkButton(
            buton,
            text="🧹 Temizle",
            command=self.temizle
        ).grid(row=0,column=3,padx=5)



        # Tablo

        self.tablo = ttk.Treeview(
            self,
            columns=(
                "id",
                "kod",
                "urun",
                "stok",
                "durum"
            ),
            show="headings"
        )


        for kolon,baslik in {

            "id":"ID",
            "kod":"Kod",
            "urun":"Ürün",
            "stok":"Stok",
            "durum":"Durum"

        }.items():

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


        self.tablo.bind(
            "<ButtonRelease-1>",
            self.sec
        )


        self.listele()



    def alan(self,parent,yazi,row,col):

        alan = ctk.CTkEntry(
            parent,
            placeholder_text=yazi
        )

        alan.grid(
            row=row,
            column=col,
            padx=5,
            pady=5
        )

        return alan



    def kaydet(self):

        urun = Urun(

            urun_kodu=self.kod.get(),
            barkod=self.barkod.get(),
            urun_adi=self.ad.get(),
            kategori=self.kategori.get(),
            alis=float(self.alis.get() or 0),
            satis=float(self.satis.get() or 0),
            kdv=int(self.kdv.get() or 20),
            stok=float(self.stok.get() or 0),
            kritik_stok=float(self.kritik.get() or 5)

        )


        urun_ekle(urun)

        self.listele()

        self.temizle()



    def listele(self):

        for item in self.tablo.get_children():

            self.tablo.delete(item)



        arama = self.arama.get().lower()


        toplam = 0


        for urun in urunleri_getir():

            if arama and arama not in str(urun[3]).lower():

                continue


            durum = "Normal"


            if urun[9] <= urun[10]:

                durum = "⚠ Kritik"


            self.tablo.insert(
                "",
                "end",
                values=(
                    urun[0],
                    urun[1],
                    urun[3],
                    urun[9],
                    durum
                )
            )


            toplam += 1



    def sec(self,event):

        secilen = self.tablo.selection()


        if secilen:

            veri = self.tablo.item(secilen)

            self.secili_id = veri["values"][0]



    def guncelle(self):

        if not self.secili_id:

            return


        urun = Urun(

            id=self.secili_id,

            urun_kodu=self.kod.get(),
            barkod=self.barkod.get(),
            urun_adi=self.ad.get(),
            kategori=self.kategori.get(),
            alis=float(self.alis.get() or 0),
            satis=float(self.satis.get() or 0),
            kdv=int(self.kdv.get() or 20),
            stok=float(self.stok.get() or 0),
            kritik_stok=float(self.kritik.get() or 5)

        )


        urun_guncelle_v2(urun)

        self.listele()



    def sil(self):

        if self.secili_id:

            urun_sil(self.secili_id)

            self.listele()

            self.temizle()



    def temizle(self):

        self.secili_id=None

        for alan in [

            self.kod,
            self.barkod,
            self.ad,
            self.kategori,
            self.alis,
            self.satis,
            self.kdv,
            self.stok,
            self.kritik

        ]:

            alan.delete(0,"end")