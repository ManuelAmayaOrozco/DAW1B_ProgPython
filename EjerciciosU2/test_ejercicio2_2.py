import pytest
from src.ejercicio2_2 import password

@pytest.mark.parametrize(
  "input_n1, expected",
    [
      ("holakase", "La contraseña introducida coincide con la contraseña guardada."),
      ("contraseña", "La contraseña introducida no coincide con la contraseña guardada."),
      ("waswas", "La contraseña introducida coincide con la contraseña guardada.")
    ] 
)
def test_password_params(input_n1, expected):
    assert password(input_n1) == expected