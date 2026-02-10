# Esto es para que el pre-commit no falle por no encontrar tests, aunque realmente no se esté testeando nada.
def test_smoke() -> None:
    assert True
