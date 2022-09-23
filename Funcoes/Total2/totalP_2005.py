def Calc_totalP2005(arq_2005):
    linha_cont = 0
    ano = 2005
    part_cont = 0
    quant_part2005 = dict()

    dados2005 = open(arq_2005, 'r', encoding='ISO-8859-1')
    l = dados2005.readlines()

    dados2005.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_part2005[linha_cont] = int(linha_dados[0])

    escreve2005 = open('Imprime_dados/Total2/quantitativo_candidatos_totalPart_2005.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_part2005[cont_linha] == 2005:
            part_cont += 1

    escreve2005.write('2005 - Total de Participantes: ')
    escreve2005.write(str(ano))
    escreve2005.write(", ")
    escreve2005.write(str(part_cont))

