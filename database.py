import sqlite3


DB = "database/muhasebe.db"


# =========================
# VERİTABANI
# =========================

def veritabani_olustur():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kullanicilar(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        kullanici_adi TEXT UNIQUE,

        sifre TEXT

    )
    """)


    cursor.execute("""
    INSERT OR IGNORE INTO kullanicilar
    (kullanici_adi,sifre)

    VALUES

    ('admin','1234')

    """)


    conn.commit()
    conn.close()



# =========================
# LOGIN
# =========================

def giris_kontrol(kullanici, sifre):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    SELECT *

    FROM kullanicilar

    WHERE kullanici_adi=?
    AND sifre=?

    """,
    (
        kullanici,
        sifre
    ))


    sonuc = cursor.fetchone()


    conn.close()


    return sonuc



# =========================
# ÜRÜN TABLOSU
# =========================

def urun_tablosu_olustur():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS urunler(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        urun_kodu TEXT UNIQUE,

        barkod TEXT,

        urun_adi TEXT,

        kategori TEXT,

        birim TEXT,

        alis REAL,

        satis REAL,

        kdv INTEGER,

        stok REAL,

        kritik_stok REAL

    )
    """)


    conn.commit()

    conn.close()



# =========================
# ÜRÜN EKLE
# =========================

def urun_ekle(urun):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    INSERT INTO urunler

    (

    urun_kodu,
    barkod,
    urun_adi,
    kategori,
    birim,
    alis,
    satis,
    kdv,
    stok,
    kritik_stok

    )

    VALUES (?,?,?,?,?,?,?,?,?,?)

    """,
    (

    urun.urun_kodu,
    urun.barkod,
    urun.urun_adi,
    urun.kategori,
    urun.birim,
    urun.alis,
    urun.satis,
    urun.kdv,
    urun.stok,
    urun.kritik_stok

    ))


    conn.commit()

    conn.close()



# =========================
# ÜRÜN LİSTE
# =========================

def urunleri_getir():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    SELECT *

    FROM urunler

    ORDER BY id DESC

    """)


    veriler = cursor.fetchall()


    conn.close()


    return veriler



# =========================
# ÜRÜN SİL
# =========================

def urun_sil(id):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute(
        """
        DELETE FROM urunler

        WHERE id=?
        """,
        (id,)
    )


    conn.commit()

    conn.close()



# =========================
# ÜRÜN GÜNCELLE
# =========================

def urun_guncelle_v2(urun):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    UPDATE urunler SET

    urun_kodu=?,

    barkod=?,

    urun_adi=?,

    kategori=?,

    alis=?,

    satis=?,

    kdv=?,

    stok=?,

    kritik_stok=?


    WHERE id=?

    """,
    (

    urun.urun_kodu,
    urun.barkod,
    urun.urun_adi,
    urun.kategori,
    urun.alis,
    urun.satis,
    urun.kdv,
    urun.stok,
    urun.kritik_stok,
    urun.id

    ))


    conn.commit()

    conn.close()



# =========================
# CARİ TABLOSU
# =========================

def cari_tablosu_olustur():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cariler(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        cari_kodu TEXT UNIQUE,

        firma_adi TEXT,

        yetkili TEXT,

        telefon TEXT,

        email TEXT,

        adres TEXT,

        vergi_no TEXT,

        borc REAL DEFAULT 0,

        alacak REAL DEFAULT 0

    )
    """)


    conn.commit()

    conn.close()



# =========================
# CARİ EKLE
# =========================

def cari_ekle(cari):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    INSERT INTO cariler

    (

    cari_kodu,

    firma_adi,

    yetkili,

    telefon,

    email,

    adres,

    vergi_no,

    borc,

    alacak

    )

    VALUES (?,?,?,?,?,?,?,?,?)

    """,
    (

    cari.cari_kodu,

    cari.firma_adi,

    cari.yetkili,

    cari.telefon,

    cari.email,

    cari.adres,

    cari.vergi_no,

    cari.borc,

    cari.alacak

    ))


    conn.commit()

    conn.close()



# =========================
# CARİ LİSTE
# =========================

def carileri_getir():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    SELECT *

    FROM cariler

    ORDER BY id DESC

    """)


    veriler = cursor.fetchall()


    conn.close()


    return veriler



# =========================
# CARİ SİL
# =========================

def cari_sil(id):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute(
        """
        DELETE FROM cariler

        WHERE id=?
        """,
        (id,)
    )


    conn.commit()

    conn.close()
    # =========================
# SATIŞ TABLOLARI
# =========================

def satis_tablosu_olustur():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS satislar(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        cari_id INTEGER,

        tarih TEXT,

        toplam REAL

    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS satis_detaylari(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        satis_id INTEGER,

        urun_id INTEGER,

        miktar REAL,

        fiyat REAL,

        tutar REAL

    )
    """)


    conn.commit()

    conn.close()



# =========================
# SATIŞ EKLE
# =========================

def satis_ekle(cari_id, tarih, toplam):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    INSERT INTO satislar

    (
        cari_id,
        tarih,
        toplam
    )

    VALUES (?,?,?)

    """,
    (
        cari_id,
        tarih,
        toplam
    ))


    satis_id = cursor.lastrowid


    conn.commit()

    conn.close()


    return satis_id



# =========================
# SATIŞ DETAY EKLE
# =========================

def satis_detay_ekle(
        satis_id,
        urun_id,
        miktar,
        fiyat,
        tutar
):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    INSERT INTO satis_detaylari

    (
        satis_id,
        urun_id,
        miktar,
        fiyat,
        tutar
    )

    VALUES (?,?,?,?,?)

    """,
    (
        satis_id,
        urun_id,
        miktar,
        fiyat,
        tutar
    ))


    conn.commit()

    conn.close()



# =========================
# SATIŞ LİSTELE
# =========================

def satislari_getir():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    SELECT *

    FROM satislar

    ORDER BY id DESC

    """)


    veriler = cursor.fetchall()


    conn.close()


    return veriler
    # =========================
# STOK DÜŞÜRME
# =========================

def stok_dus(urun_id, miktar):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    UPDATE urunler

    SET stok = stok - ?

    WHERE id = ?

    """,
    (
        miktar,
        urun_id
    ))


    conn.commit()

    conn.close()



# =========================
# CARİ BORÇ ARTIRMA
# =========================

def cari_borc_artir(cari_id, tutar):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    UPDATE cariler

    SET borc = borc + ?

    WHERE id = ?

    """,
    (
        tutar,
        cari_id
    ))


    conn.commit()

    conn.close()
    # =========================
# SATIŞ GEÇMİŞİ
# =========================

def satis_gecmisi_getir():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    SELECT

        satislar.id,
        satislar.tarih,
        cariler.firma_adi,
        satislar.toplam

    FROM satislar

    LEFT JOIN cariler

    ON satislar.cari_id = cariler.id

    ORDER BY satislar.id DESC

    """)


    veriler = cursor.fetchall()


    conn.close()


    return veriler
    # =========================
# SATIŞ DETAY GETİR
# =========================

def satis_detaylarini_getir(satis_id):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    SELECT

        urunler.urun_adi,

        satis_detaylari.miktar,

        satis_detaylari.fiyat,

        satis_detaylari.tutar


    FROM satis_detaylari


    LEFT JOIN urunler


    ON satis_detaylari.urun_id = urunler.id


    WHERE satis_detaylari.satis_id = ?


    """,
    (
        satis_id,
    ))


    veriler = cursor.fetchall()


    conn.close()


    return veriler
    # =========================
# KASA TABLOSU
# =========================

def kasa_tablosu_olustur():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kasa_hareketleri(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        tarih TEXT,

        aciklama TEXT,

        tur TEXT,

        tutar REAL

    )
    """)


    conn.commit()

    conn.close()





# =========================
# KASA EKLE
# =========================

def kasa_ekle(tarih, aciklama, tur, tutar):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    INSERT INTO kasa_hareketleri

    (
        tarih,
        aciklama,
        tur,
        tutar
    )

    VALUES (?,?,?,?)

    """,
    (
        tarih,
        aciklama,
        tur,
        tutar
    ))


    conn.commit()

    conn.close()





# =========================
# KASA LİSTE
# =========================

def kasa_getir():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    SELECT *

    FROM kasa_hareketleri

    ORDER BY id DESC

    """)


    veriler = cursor.fetchall()


    conn.close()


    return veriler





# =========================
# KASA BAKİYE
# =========================

def kasa_bakiye():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    SELECT

    SUM(

        CASE

        WHEN tur='Giriş'

        THEN tutar

        ELSE 0

        END

    ),

    SUM(

        CASE

        WHEN tur='Çıkış'

        THEN tutar

        ELSE 0

        END

    )


    FROM kasa_hareketleri

    """)


    sonuc = cursor.fetchone()


    conn.close()


    giris = sonuc[0] or 0

    cikis = sonuc[1] or 0


    return giris - cikis
    # =========================
# ALIŞ TABLOSU
# =========================

def alis_tablosu_olustur():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alislar(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        cari_id INTEGER,

        tarih TEXT,

        toplam REAL

    )
    """)



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alis_detaylari(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        alis_id INTEGER,

        urun_id INTEGER,

        miktar REAL,

        fiyat REAL,

        tutar REAL

    )
    """)



    conn.commit()

    conn.close()





# =========================
# ALIŞ EKLE
# =========================

def alis_ekle(cari_id, tarih, toplam):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    INSERT INTO alislar

    (
        cari_id,
        tarih,
        toplam
    )

    VALUES (?,?,?)

    """,
    (
        cari_id,
        tarih,
        toplam
    ))


    alis_id = cursor.lastrowid


    conn.commit()

    conn.close()


    return alis_id





# =========================
# ALIŞ DETAY EKLE
# =========================

def alis_detay_ekle(
        alis_id,
        urun_id,
        miktar,
        fiyat,
        tutar
):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    INSERT INTO alis_detaylari

    (
        alis_id,
        urun_id,
        miktar,
        fiyat,
        tutar
    )

    VALUES (?,?,?,?,?)

    """,
    (
        alis_id,
        urun_id,
        miktar,
        fiyat,
        tutar
    ))


    conn.commit()

    conn.close()





# =========================
# STOK ARTIR
# =========================

def stok_artir(urun_id, miktar):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    UPDATE urunler

    SET stok = stok + ?

    WHERE id = ?

    """,
    (
        miktar,
        urun_id
    ))


    conn.commit()

    conn.close()





# =========================
# CARİ ALACAK ARTIR
# =========================

def cari_alacak_artir(cari_id, tutar):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""
    UPDATE cariler

    SET alacak = alacak + ?

    WHERE id = ?

    """,
    (
        tutar,
        cari_id
    ))


    conn.commit()

    conn.close()
    # =========================
# DASHBOARD RAPORLARI
# =========================

import sqlite3

DB = "database/muhasebe.db"


def toplam_satis():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT IFNULL(SUM(toplam),0)
    FROM satislar
    """)

    toplam = cursor.fetchone()[0]

    conn.close()

    return toplam


def toplam_alis():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT IFNULL(SUM(toplam),0)
    FROM alislar
    """)

    toplam = cursor.fetchone()[0]

    conn.close()

    return toplam


def toplam_urun():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM urunler
    """)

    adet = cursor.fetchone()[0]

    conn.close()

    return adet


def toplam_cari():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM cariler
    """)

    adet = cursor.fetchone()[0]

    conn.close()

    return adet


def kritik_stok_sayisi():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM urunler
    WHERE stok <= kritik_stok
    """)

    adet = cursor.fetchone()[0]

    conn.close()

    return adet


def kasa_bakiyesi():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT IFNULL(SUM(giris-cikis),0)
    FROM kasa
    """)

    bakiye = cursor.fetchone()[0]

    conn.close()

    return bakiye


def son_5_satis():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT

        satislar.tarih,
        cariler.firma_adi,
        satislar.toplam

    FROM satislar

    LEFT JOIN cariler

    ON satislar.cari_id = cariler.id

    ORDER BY satislar.id DESC

    LIMIT 5
    """)

    veriler = cursor.fetchall()

    conn.close()

    return veriler