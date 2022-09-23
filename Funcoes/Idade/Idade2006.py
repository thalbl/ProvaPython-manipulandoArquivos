def Calc_idade2006(arq_2006):
    linha_cont = 0
    idade_cont = 0
    quant_idade2006 = dict()

    dados2006 = open(arq_2006, 'r', encoding='ISO-8859-1')
    l = dados2006.readlines()

    dados2006.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_idade2006[linha_cont] = int(linha_dados[10])

    escreve2006 = open('Imprime_dados/Idade/quantitativo_candidatos_40_2006.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_idade2006[cont_linha] > 40:
            idade_cont += 1

    escreve2006.write('2006 - Pessoas acima dos 40 anos: ')
    escreve2006.write(str(idade_cont))
