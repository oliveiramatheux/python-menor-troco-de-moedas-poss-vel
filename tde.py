um_real = int(input("Digite a quantidade de moedas de um real disponivel: "))
cinquenta_cent = int(input("Digite a quantidade de moedas de cinquenta centavos disponivel: "))
vintecinco_cent = int(input("Digite a quantidade de moedas de vinte e cinco centavos disponivel: "))
dez_cent = int(input("Digite a quantidade de moedas de dez centavos disponivel: "))
cinco_cent = int(input("Digite a quantidade de moedas de cinco centavos disponivel: "))
valor_gasto = float(input("Digite o valor gasto pelo cliente: "))
valor_pago = float(input("Digite o valor pago pelo cliente: "))

estoque = um_real + (cinquenta_cent * 0.50) + (vintecinco_cent * 0.25) + (dez_cent * 0.10) + (cinco_cent * 0.05)
troco = (valor_pago - valor_gasto)
cont1 = 0
cont50 = 0
cont25 = 0
cont10 = 0
cont5 = 0

if estoque >= troco:
    if valor_pago > valor_gasto:
        print("Quantidade do estoque de moedas:", estoque, "Valor do troco:", round(troco, 2))
        if troco >= 1 and um_real > 0:
            while troco >= 1:
                troco = troco - 1
                estoque = estoque - 1
                um_real = um_real - 1
                cont1 = cont1 + 1
        if troco >= 0.50 and cinquenta_cent > 0:
            while troco >= 0.50:
                troco = troco - 0.50
                estoque = estoque - 0.50
                cinquenta_cent = cinquenta_cent - 1
                cont50 = cont50 + 1
        if troco >= 0.25 and vintecinco_cent > 0:
            while troco >= 0.25:
                troco = troco - 0.25
                estoque = estoque - 0.25
                vintecinco_cent = vintecinco_cent - 1
                cont25 = cont25 + 1
        if troco >= 0.10 and dez_cent > 0:
            while troco >= 0.10:
                troco = troco - 0.10
                estoque = estoque - 0.10
                dez_cent = dez_cent - 1
                cont10 = cont10 + 1
        if troco >= 0.05 and cinco_cent > 0:
            while troco >= 0.05:
                troco = troco - 0.05
                estoque = estoque - 0.05
                cinco_cent = cinco_cent - 1
                cont5 = cont5 + 1
        print("O cliente receberá", cont1, "moedas de 1 real,", cont50, "moedas de 50 centavos,",
        cont25, "moedas de 25 centavos,", cont10, "moedas de 10 centavos e", cont5, "moedas de 5 centavos")
        print("Novo estoque:", round(estoque, 2))
    else:
        print("Não é necessário troco ou o cliente não deu dinheiro suficiente para pagar!")
else:
    print("Não há troco disponível para pagar esta quantia!")