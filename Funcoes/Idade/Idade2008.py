def Calc_idade2008(arq_2008):
    linha_cont = 0
    idade_cont = 0
    quant_idade2008 = dict()

    dados2008 = open(arq_2008, 'r', encoding='ISO-8859-1')
    l = dados2008.readlines()

    dados2008.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_idade2008[linha_cont] = int(linha_dados[10])

    escreve2008 = open('Imprime_dados/Idade/quantitativo_candidatos_40_2008.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_idade2008[cont_linha] > 40:
            idade_cont += 1

    escreve2008.write('2008 - Pessoas acima dos 40 anos: ')
    escreve2008.write(str(idade_cont))
