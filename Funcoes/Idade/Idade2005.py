def Calc_idade2005(arq_2005):
    linha_cont = 0
    idade_cont = 0
    quant_idade2005 = dict()

    dados2005 = open(arq_2005, 'r', encoding='ISO-8859-1')
    l = dados2005.readlines()

    dados2005.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_idade2005[linha_cont] = int(linha_dados[9])

    escreve2005 = open('Imprime_dados/Idade/quantitativo_candidatos_40_2005.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_idade2005[cont_linha] > 40:
            idade_cont += 1

    escreve2005.write('2005 - Pessoas acima dos 40 anos: ')
    escreve2005.write(str(idade_cont))
