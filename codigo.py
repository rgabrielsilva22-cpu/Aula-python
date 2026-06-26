compra_1 = 50
compra_2 = 150
compra_3 = 300
nome_cliente = input("Qual o nome do cliente: ")
valor_compra = float(input("qual o valor de compra: "))
if valor_compra > 100:
    desconto = valor_compra * 0.10
else:
    desconto = 0
valor_final = valor_compra - desconto
print("\nCliente: ", nome_cliente)
print("Desconto: R$", desconto)
print("Valor final: R$", valor_final)
repetir = input("\nDeseja realizar outro atendimento? (S/N):").upper
print("programa encerrado.")
