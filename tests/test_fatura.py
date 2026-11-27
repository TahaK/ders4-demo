import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import pytest
from fatura import ara_toplam, indirim_uygula, toplam


def test_ara_toplam():
    assert ara_toplam([(2, 50), (1, 30)]) == 130


def test_indirimsiz_toplam():
    assert toplam([(1, 100)]) == 120.0


def test_yuzde_on_indirim():
    assert toplam([(1, 100)], indirim_yuzde=10) == 108.0


def test_gecersiz_indirim():
    with pytest.raises(ValueError):
        indirim_uygula(100, 150)
