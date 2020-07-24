print("O que você deseja fazer?")
print("1 - Simular investimento em Fundos Imobiliários.")

opcaoSelecionada = input("Digite a opção desejada: ")

if opcaoSelecionada == "1":
    valorDisponivelInicialmente = float(input("Quanto você pretende investir inicialmnte? "))
    valorAportes = float(input("Qual o valor dos aportes mensais? "))
    quantidadeMeses = int(input("Para quantos mêses você pretende fazer a simulação? "))
    valorCota = float(input("Qual o preço atual da cota que você pretende comprar? "))
    rendimentoMesCota = float(input("Quanto cada cota rende por mês? "))

    valorFinal = valorAportes + valorDisponivelInicialmente + ((valorDisponivelInicialmente/valorCota)*rendimentoMesCota)

    for i in range (quantidadeMeses-1):
        valorDisponivel = valorFinal
        valorFinal = valorAportes + valorDisponivel + ((valorDisponivel/valorCota)*rendimentoMesCota)
    
    rendimentoLiquido = valorFinal - (valorDisponivelInicialmente + (valorAportes * quantidadeMeses))
    print("O seu saldo final será: R$%.2f. O rendimento líquido foi de: R$%.2f" %(valorFinal, rendimentoLiquido))
