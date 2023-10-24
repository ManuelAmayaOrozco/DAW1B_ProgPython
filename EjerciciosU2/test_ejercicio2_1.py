import pytest
from ejercicio2_1 import edad

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (12, "No eres mayor de edad."),
      (23, "Eres mayor de edad."),
      (30, "Eres mayor de edad.")
    ] 
)
def test_edad_params(input_n1, expected):
    assert edad(input_n1) == expected