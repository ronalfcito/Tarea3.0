import app

def test_suma():
    assert app.suma(2, 3) == 5

def test_resta():
    assert app.resta(10, 4) == 6

def test_multiplicacion():
    assert app.multiplicacion(3, 7) == 21

def test_division():
    assert app.division(8, 2) == 4

def test_division_por_cero():
    assert app.division(5, 0) == "Error: división por cero"
