import pytest
from src.ejercicio2_4 import paridad

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (4, "El número es par."),
      (7, "El número es impar."),
      (1, "El número es impar.")
    ] 
)
def test_paridad_params(input_n1, expected):
    assert paridad(input_n1) == expected