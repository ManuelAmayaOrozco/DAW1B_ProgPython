import pytest
from src.ejercicio2_3 import division

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
      (4, 2, "{input_n1} / {input_n2} = {expected}"),
      (4, 0, "Error, no se puede dividir por 0."),
      (6, 3, "{input_n1} / {input_n2} = {expected}")
    ] 
)
def test_division_params(input_n1, input_n2, expected):
    assert division(input_n1, input_n2) == expected