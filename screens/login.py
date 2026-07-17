import customtkinter as ctk
from database import giris_kontrol
from screens.dashboard import Dashboard


class LoginApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Muhasebe ve Stok Takip Programı")
        self.geometry("500x450")
        self.resizable(False, False)

        baslik = ctk.CTkLabel(
            self,
            text="MUHASEBE & STOK TAKİP",
            font=("Arial", 24, "bold")
        )
        baslik.pack(pady=30)

        self.kullanici = ctk.CTkEntry(
            self,
            placeholder_text="Kullanıcı Adı",
            width=300,
            height=40
        )
        self.kullanici.pack(pady=10)

        self.sifre = ctk.CTkEntry(
            self,
            placeholder_text="Şifre",
            show="*",
            width=300,
            height=40
        )
        self.sifre.pack(pady=10)

        self.durum = ctk.CTkLabel(self, text="")
        self.durum.pack(pady=10)

        ctk.CTkButton(
            self,
            text="GİRİŞ YAP",
            width=300,
            height=40,
            command=self.giris_yap
        ).pack(pady=20)

    def giris_yap(self):

        sonuc = giris_kontrol(
            self.kullanici.get(),
            self.sifre.get()
        )

        if sonuc:
            self.withdraw()

            Dashboard()

        else:
            self.durum.configure(
                text="Kullanıcı adı veya şifre yanlış",
                text_color="red"
            )