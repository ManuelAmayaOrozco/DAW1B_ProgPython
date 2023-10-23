import pytest
from pruebaunitaria1 import mayor

def test_mayor():
    assert mayor(1, 2) == 2
    assert mayor(5, 3) == 5
    assert mayor(8, 8) == 0
    
@pytest.mark.parametrize(
  "input_n1, input_n2, expected",
  [
    (2, 3, 3),
    (5, 3, 5),
    (8, 8, 0)
  ]
 )
def test_mayor_params(input_n1, input_n2, expected):
    assert mayor(input_n1, input_n2) == expected