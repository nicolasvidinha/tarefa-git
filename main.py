total_vendas = 0
total_bruto = 0
total_descontos = 0
total_liquido = 0

while True:
    print("\n=== SISTEMA DE VENDAS ===")
    print("1 - Registrar venda")
    print("2 - Ver resumo parcial")
    print("3 - Encerrar sistema")

    opcao = input("\n Escolha uma opção: ")

    if opcao == "1":
        produto = input("Nome do produto: ")
        valor_unitario = float(input("Valor unitário: "))
        quantidade = int(input("Quantidade: "))

        valor_bruto = valor_unitario * quantidade

        print(f"Nome do produto: {produto}")
        print(f"Valor unitário: R$ {valor_unitario:.2f}")
        print(f"Quantidade: {quantidade}")

        print(f"Valor bruto da venda: R$ {valor_bruto:.2f}")

        percentual_desc = 0
        if valor_bruto < 100:
            percentual_desc = 0
        elif 100 > valor_bruto < 499.99:
            percentual_desc = 5
        elif 500 > valor_bruto < 999.99:
            percentual_desc = 10
        else:
            percentual_desc = 15

        valor_desconto = (percentual_desc / 100) * valor_bruto
        valor_final = valor_bruto - valor_desconto

        print(f"Desconto aplicado: {percentual_desc}%")  
        print(f"Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"Valor final da venda: R$ {valor_final:.2f}")

        total_vendas += 1
        total_bruto += valor_bruto
        total_descontos += valor_desconto
        total_liquido += valor_final
    
   














