from dataclasses import dataclass

@dataclass
class Urun:
    id: int | None = None
    urun_kodu: str = ""
    barkod: str = ""
    urun_adi: str = ""
    kategori: str = ""
    birim: str = ""
    alis: float = 0.0
    satis: float = 0.0
    kdv: int = 20
    stok: float = 0.0
    kritik_stok: float = 0.0