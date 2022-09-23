def Calc_totalP2004(arq_2004):
    linha_cont = 0
    ano = '2004'
    part_cont = 0
    quant_part2004 = dict()

    dados2004 = open(arq_2004, 'r', encoding='ISO-8859-1')
    l = dados2004.readlines()

    dados2004.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_part2004[linha_cont] = int(linha_dados[0])

    escreve2004 = open('Imprime_dados/Total2/quantitativo_candidatos_totalPart_2004.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_part2004[cont_linha] == 2004:
            part_cont += 1

    escreve2004.write('2004 - Total de Participantes: ')
    escreve2004.write(str(ano))
    escreve2004.write(", ")
    escreve2004.write(str(part_cont))

