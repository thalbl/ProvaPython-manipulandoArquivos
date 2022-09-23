def Calc_totalP2006(arq_2006):
    linha_cont = 0
    ano = 2006
    part_cont = 0
    quant_part2006 = dict()

    dados2006 = open(arq_2006, 'r', encoding='ISO-8859-1')
    l = dados2006.readlines()

    dados2006.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_part2006[linha_cont] = int(linha_dados[0])

    escreve2006 = open('Imprime_dados/Total2/quantitativo_candidatos_totalPart_2006.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_part2006[cont_linha] == 2006:
            part_cont += 1

    escreve2006.write('2006 - Total de Participantes: ')
    escreve2006.write(str(ano))
    escreve2006.write(", ")
    escreve2006.write(str(part_cont))

