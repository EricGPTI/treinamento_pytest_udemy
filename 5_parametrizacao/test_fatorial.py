import pytest
from fatorial import fatorial

@pytest.mark.parametrize(
    "n, expected_fat",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720)
        ]
)

def test_fatorial(n, expected_fat):
    assert fatorial(n) == expected_fat


@pytest.mark.parametrize(
    "n, raise_expected",
    [
        (-1, ValueError),
        ('a', ValueError)
    ]
            
)
def test_fatorial_raise(n, raise_expected):
    with pytest.raises(raise_expected):
        fatorial(n)





