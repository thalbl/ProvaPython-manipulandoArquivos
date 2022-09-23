def Calc_totalReg2005(arq_2005):
    linha_cont = 0
    reg1_cont = 0
    reg2_cont = 0
    reg3_cont = 0
    reg4_cont = 0
    reg5_cont = 0
    quant_tReg2005 = dict()

    dados2005 = open(arq_2005, 'r', encoding='ISO-8859-1')
    l = dados2005.readlines()

    dados2005.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_tReg2005[linha_cont] = int(linha_dados[5])

    escreve2005 = open('Imprime_dados/Total/quantitativo_candidatos_totalreg_2005.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_tReg2005[cont_linha] == 1:
            reg1_cont += 1

        if quant_tReg2005[cont_linha] == 2:
            reg2_cont += 1

        if quant_tReg2005[cont_linha] == 3:
            reg3_cont += 1

        if quant_tReg2005[cont_linha] == 4:
            reg4_cont += 1

        if quant_tReg2005[cont_linha] == 5:
            reg5_cont += 1



    escreve2005.write('2005 - Total de Pessoas do Norte: ')
    escreve2005.write(str(reg1_cont))
    escreve2005.write('\n2005 - Total de Pessoas do Nordeste: ')
    escreve2005.write(str(reg2_cont))
    escreve2005.write('\n2005 - Total de Pessoas do Sudeste: ')
    escreve2005.write(str(reg3_cont))
    escreve2005.write('\n2005 - Total de Pessoas do Sul: ')
    escreve2005.write(str(reg4_cont))
    escreve2005.write('\n2005 - Total de Pessoas do Centro-Oeste: ')
    escreve2005.write(str(reg5_cont))

