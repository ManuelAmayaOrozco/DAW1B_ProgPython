import pytest
from ejercicio2_6 import asiggrupo

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
      ("Claudia", 2, "Eres parte del grupo A."),
      ("Manuel", 1, "Eres parte del grupo B."),
      ("Norton", 1, "Eres parte del grupo A.")
    ] 
)
def test_asiggrupo_params(input_n1, input_n2, expected):
    assert asiggrupo(input_n1, input_n2) == expected