def Calc_idade2007(arq_2007):
    linha_cont = 0
    idade_cont = 0
    quant_idade2007 = dict()

    dados2007 = open(arq_2007, 'r', encoding='ISO-8859-1')
    l = dados2007.readlines()

    dados2007.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_idade2007[linha_cont] = int(linha_dados[9])

    escreve2007 = open('Imprime_dados/Idade/quantitativo_candidatos_40_2007.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_idade2007[cont_linha] > 40:
            idade_cont += 1

    escreve2007.write('2007 - Pessoas acima dos 40 anos: ')
    escreve2007.write(str(idade_cont))
