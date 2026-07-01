print("=== Lá no charuri ===")
print(" " * 4, "Lanchonete" )

nome_cliente = input( "Por favor, digite o seu nome: ")
print(f"Olá, {nome_cliente}")

print("=== NOSSO CARDÁPIO === ")
print("1. Hambúrguer Matador - R$ 39.59")
print("2. Bolinha de queijo - R$ 31.30")
print("3. Pastel de Palmito - R$ 39.59")

# Recebendo dados do pedido
print("\n Faça o seu pedido")
qtd_hamburguer = int(input("Quantos hamburgures você deseja? "))
qtd_bol_queijo = int(input("Quantas bolinhas você deseja? "))
qtd_pastel_palmito = int(input("Quantos pasteis você deseja? "))

# Fechando a conta
total_hamburguer = qtd_hamburguer * 39.59 
total_bolinha_queijo = qtd_bol_queijo * 1.30
total_pastel_palmito = qtd_pastel_palmito * 15.59

valor_total = total_hamburguer + total_bolinha_queijo + total_pastel_palmito
# Exibindo o cupom fiscal
print("\n" + "="+30)
print(" " * 8 + "CUPOM FISCAL" + " " * 8)
print("=" * 30)
print(f"Cliente: {nome_cliente}")
print(f"Hmaburguer Matador: {total_hamburguer}")
print(f"Bolinha de queijo: {total_bolinha_queijo}")
print(f"Pastel Palmito : {total_pastel_palmito}")
print(f"Total do pedido: {valor_total}")
