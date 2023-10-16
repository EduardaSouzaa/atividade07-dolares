# Digite um valor e veja quantos dolares voce poderá comprar: R$
real = float(input("Digite o Valor em real"))
dolar = float(input("Digite a cotação do dia"))
conv = real / dolar
print(f"""
seu valor em R$ {real}
cotação atual em $ {dolar}
valor de convensão $ {conv}
""")