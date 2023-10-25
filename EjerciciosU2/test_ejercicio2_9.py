import pytest
from src.ejercicio2_9 import precio

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (3, "Entrada gratis."),
      (8, "Tiene que pagar 5€."),
      (24, "Tiene que pagar 10€.")
    ] 
)
def test_precio_params(input_n1, expected):
    assert precio(input_n1) == expected