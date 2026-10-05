from desconto import calcular_desconto


def test_compra_abaixo_100_comum():
    assert calcular_desconto(50, "COMUM") == 0


def test_compra_igual_100_comum():
    assert calcular_desconto(100, "COMUM") == 10


def test_compra_entre_100_e_500_comum():
    assert calcular_desconto(300, "COMUM") == 30


def test_compra_igual_500_comum():
    assert calcular_desconto(500, "COMUM") == 100


def test_compra_abaixo_100_vip():
    assert calcular_desconto(50, "VIP") == 2.50


def test_compra_300_vip():
    assert calcular_desconto(300, "VIP") == 45


def test_compra_500_vip():
    assert calcular_desconto(500, "VIP") == 125


def test_vip_minusculo():
    assert calcular_desconto(300, "vip") == 45


def test_vip_letras_variadas():
    assert calcular_desconto(300, "Vip") == 45


def test_teto_desconto_vip():
    assert calcular_desconto(1000, "VIP") == 200


def test_teto_desconto_comum():
    assert calcular_desconto(2000, "COMUM") == 200