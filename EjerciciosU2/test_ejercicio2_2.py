import pytest
from ejercicio2_2 import password

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
      ("holakase", "HOLAKASE", "La contraseña introducida coincide con la contraseña guardada."),
      ("contraseña", "Contraseya", "La contraseña introducida no coincide con la contraseña guardada."),
      ("waswas", "WaSwAs", "La contraseña introducida coincide con la contraseña guardada.")
    ] 
)
def test_password_params(input_n1, expected):
    assert password(input_n1) == expected