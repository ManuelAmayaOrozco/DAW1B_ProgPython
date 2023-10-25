import pytest
from ejercicio2_8 import rendimiento

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (0.0, "Nivel inaceptable, recibirá una paga de {din}€."),
      (0.5, "Nivel aceptable, recibirá una paga de {din}€."),
      (0.8, "Nivel meritorio, recibirá una paga de {din}€.")
    ] 
)
def test_rendimiento_params(input_n1, expected):
    assert rendimiento(input_n1) == expected