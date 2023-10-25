import pytest
from src.ejercicio2_7 import renta

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (10, "Tu tipo impositivo es del 5%."),
      (35000, "Tu tipo impositivo es del 30%."),
      (66666, "Tu tipo impositivo es del 45%.")
    ] 
)
def test_renta_params(input_n1, expected):
    assert renta(input_n1) == expected