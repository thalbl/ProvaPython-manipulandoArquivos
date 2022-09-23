def Calc_totalP2008(arq_2008):
    linha_cont = 0
    ano = 2008
    part_cont = 0
    quant_part2008 = dict()

    dados2008 = open(arq_2008, 'r', encoding='ISO-8859-1')
    l = dados2008.readlines()

    dados2008.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_part2008[linha_cont] = int(linha_dados[0])

    escreve2008 = open('Imprime_dados/Total2/quantitativo_candidatos_totalPart_2008.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_part2008[cont_linha] == 2008:
            part_cont += 1

    escreve2008.write('2008 - Total de Participantes: ')
    escreve2008.write(str(ano))
    escreve2008.write(", ")
    escreve2008.write(str(part_cont))

