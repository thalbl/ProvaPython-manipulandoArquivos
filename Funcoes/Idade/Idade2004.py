def Calc_idade2004(arq_2004):
    linha_cont = 0
    idade_cont = 0
    quant_idade2004 = dict()

    dados2004 = open(arq_2004, 'r', encoding='ISO-8859-1')
    l = dados2004.readlines()

    dados2004.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_idade2004[linha_cont] = int(linha_dados[9])

    escreve2004 = open('Imprime_dados/Idade/quantitativo_candidatos_40_2004.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_idade2004[cont_linha] > 40:
            idade_cont += 1

    escreve2004.write('2004 - Pessoas acima dos 40 anos: ')
    escreve2004.write(str(idade_cont))

