import pytest
from ejercicio2_10 import pizzatime

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      ("V", "Su pizza vegetariana lleva: Mozzarella, Tomate, {ing}."),
      ("N", "Su pizza lleva: Mozzarella, Tomate, {ing}."),
      ("N", "Su pizza lleva: Mozzarella, Tomate, {ing}.")
    ] 
)
def test_pizzatime_params(input_n1, expected):
    assert pizzatime(input_n1) == expected