def Calc_totalP2007(arq_2007):
    linha_cont = 0
    ano = 2007
    part_cont = 0
    quant_part2007 = dict()

    dados2007 = open(arq_2007, 'r', encoding='ISO-8859-1')
    l = dados2007.readlines()

    dados2007.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_part2007[linha_cont] = int(linha_dados[0])

    escreve2007 = open('Imprime_dados/Total2/quantitativo_candidatos_totalPart_2007.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_part2007[cont_linha] == 2007:
            part_cont += 1

    escreve2007.write('2007 - Total de Participantes: ')
    escreve2007.write(str(ano))
    escreve2007.write(", ")
    escreve2007.write(str(part_cont))
