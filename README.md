## Testes Unitários

Os testes unitários foram escritos utilizando Python.

Foram criados cenários para validar:

- Compras abaixo de R$ 100,00 para clientes comuns.
- Compras exatamente de R$ 100,00.
- Compras entre R$ 100,00 e R$ 500,00.
- Compras exatamente de R$ 500,00.
- Clientes VIP com compras abaixo de R$ 100,00.
- Clientes VIP com valores intermediários.
- Clientes VIP com compras de R$ 500,00.
- Cliente VIP escrito como `VIP`.
- Cliente VIP escrito como `vip`.
- Cliente VIP escrito como `Vip`.
- Aplicação do teto máximo de R$ 200,00 para clientes VIP.
- Aplicação do teto máximo de R$ 200,00 para clientes comuns.

Os testes foram implementados com instruções `assert`, comparando o valor retornado pela função `calcular_desconto` com o resultado esperado de acordo com os critérios de aceite.

Exemplo:

```python
def test_compra_igual_100_comum():
    assert calcular_desconto(100, "COMUM") == 10