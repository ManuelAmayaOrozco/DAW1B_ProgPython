import pytest
from ejercicio2_5 import tributar

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
      (18, 9000, "Usted tiene que tributar."),
      (20, 10, "Usted no tiene que tributar."),
      (25, 2000, "Usted tiene que tributar.")
    ] 
)
def test_tributar_params(input_n1, input_n2, expected):
    assert tributar(input_n1, input_n2) == expected