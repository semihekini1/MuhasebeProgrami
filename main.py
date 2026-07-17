import customtkinter as ctk

from database import (
    veritabani_olustur,
    urun_tablosu_olustur,
    cari_tablosu_olustur,
    satis_tablosu_olustur,
    kasa_tablosu_olustur,
    alis_tablosu_olustur
)
from screens.login import LoginApp

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

veritabani_olustur()
urun_tablosu_olustur()
cari_tablosu_olustur()
kasa_tablosu_olustur()
satis_tablosu_olustur()
alis_tablosu_olustur()
app = LoginApp()
app.mainloop()