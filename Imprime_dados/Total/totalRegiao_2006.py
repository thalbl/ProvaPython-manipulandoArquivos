def Calc_totalReg2006(arq_2006):
    linha_cont = 0
    reg1_cont = 0
    reg2_cont = 0
    reg3_cont = 0
    reg4_cont = 0
    reg5_cont = 0
    quant_tReg2006 = dict()

    dados2006 = open(arq_2006, 'r', encoding='ISO-8859-1')
    l = dados2006.readlines()

    dados2006.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_tReg2006[linha_cont] = int(linha_dados[6])

    escreve2006 = open('Imprime_dados/Total/quantitativo_candidatos_totalreg_2006.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_tReg2006[cont_linha] == 1:
            reg1_cont += 1

        if quant_tReg2006[cont_linha] == 2:
            reg2_cont += 1

        if quant_tReg2006[cont_linha] == 3:
            reg3_cont += 1

        if quant_tReg2006[cont_linha] == 4:
            reg4_cont += 1

        if quant_tReg2006[cont_linha] == 5:
            reg5_cont += 1



    escreve2006.write('2006 - Total de Pessoas do Norte: ')
    escreve2006.write(str(reg1_cont))
    escreve2006.write('\n2006 - Total de Pessoas do Nordeste: ')
    escreve2006.write(str(reg2_cont))
    escreve2006.write('\n2006 - Total de Pessoas do Sudeste: ')
    escreve2006.write(str(reg3_cont))
    escreve2006.write('\n2006 - Total de Pessoas do Sul: ')
    escreve2006.write(str(reg4_cont))
    escreve2006.write('\n2006 - Total de Pessoas do Centro-Oeste: ')
    escreve2006.write(str(reg5_cont))

