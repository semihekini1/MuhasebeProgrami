import customtkinter as ctk


from screens.stok import StokApp
from screens.cari import CariApp
from screens.satis import SatisApp
from screens.satis_gecmisi import SatisGecmisiApp
from screens.alis import AlisApp
from screens.kasa import KasaApp



class Dashboard(ctk.CTkToplevel):

    def __init__(self):

        super().__init__()


        self.title(
            "Muhasebe ve Stok Takip Programı"
        )


        self.geometry(
            "1200x700"
        )


        self.icerik = None



        # SOL MENÜ

        menu = ctk.CTkFrame(

            self,

            width=220

        )

        menu.pack(

            side="left",

            fill="y"

        )



        ctk.CTkLabel(

            menu,

            text="MENÜ",

            font=("Arial",22,"bold")

        ).pack(

            pady=20

        )



        butonlar = [

            ("🏠 Ana Sayfa", self.ana_sayfa),

            ("📦 Stok", self.stok_ac),

            ("👥 Cari", self.cari_ac),

            ("🧾 Satış", self.satis_ac),

            ("📋 Satış Geçmişi", self.satis_gecmisi_ac),

            ("📥 Alış", self.alis_ac),

            ("💰 Kasa", self.kasa_ac),

            ("📊 Raporlar", None),

            ("⚙ Ayarlar", None)

        ]



        for yazi, komut in butonlar:


            ctk.CTkButton(

                menu,

                text=yazi,

                width=180,

                command=komut

            ).pack(

                pady=5

            )




        # SAĞ PANEL


        self.sag = ctk.CTkFrame(

            self

        )


        self.sag.pack(

            side="left",

            fill="both",

            expand=True

        )



        self.baslangic = ctk.CTkLabel(

            self.sag,

            text="Hoş Geldiniz",

            font=("Arial",28,"bold")

        )


        self.baslangic.pack(

            pady=40

        )





    def ekran_temizle(self):


        if self.icerik:


            self.icerik.destroy()


        if self.baslangic:


            self.baslangic.destroy()




    def ana_sayfa(self):


        self.ekran_temizle()



    def stok_ac(self):


        self.ekran_temizle()


        self.icerik = StokApp(

            self.sag

        )




    def cari_ac(self):


        self.ekran_temizle()


        self.icerik = CariApp(

            self.sag

        )




    def satis_ac(self):


        self.ekran_temizle()


        self.icerik = SatisApp(

            self.sag

        )




    def satis_gecmisi_ac(self):


        self.ekran_temizle()


        self.icerik = SatisGecmisiApp(

            self.sag

        )




    def alis_ac(self):


        self.ekran_temizle()


        self.icerik = AlisApp(

            self.sag

        )




    def kasa_ac(self):


        self.ekran_temizle()


        self.icerik = KasaApp(

            self.sag

        )