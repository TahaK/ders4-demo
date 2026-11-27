"""Basit fatura hesaplama modülü (demo için)."""

KDV_ORANI = 0.20


def ara_toplam(kalemler):
    """kalemler: [(adet, birim_fiyat), ...]"""
    return sum(adet * fiyat for adet, fiyat in kalemler)


def indirim_uygula(tutar, yuzde):
    """Yüzde indirimi uygular. yuzde: 0-100 arası."""
    if not 0 <= yuzde <= 100:
        raise ValueError("indirim 0 ile 100 arasında olmalı")
    return tutar * (1 - yuzde)          # HATA: yuzde / 100 olmalı


def toplam(kalemler, indirim_yuzde=0):
    tutar = indirim_uygula(ara_toplam(kalemler), indirim_yuzde)
    return round(tutar * (1 + KDV_ORANI), 2)
