def Calc_totalReg2004(arq_2004):
    linha_cont = 0
    reg1_cont = 0
    reg2_cont = 0
    reg3_cont = 0
    reg4_cont = 0
    reg5_cont = 0
    quant_tReg2004 = dict()

    dados2004 = open(arq_2004, 'r', encoding='ISO-8859-1')
    l = dados2004.readlines()

    dados2004.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_tReg2004[linha_cont] = int(linha_dados[5])

    escreve2004 = open('Imprime_dados/Total/quantitativo_candidatos_totalreg_2004.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_tReg2004[cont_linha] == 1:
            reg1_cont += 1

        if quant_tReg2004[cont_linha] == 2:
            reg2_cont += 1

        if quant_tReg2004[cont_linha] == 3:
            reg3_cont += 1

        if quant_tReg2004[cont_linha] == 4:
            reg4_cont += 1

        if quant_tReg2004[cont_linha] == 5:
            reg5_cont += 1



    escreve2004.write('2004 - Total de Pessoas do Norte: ')
    escreve2004.write(str(reg1_cont))
    escreve2004.write('\n2004 - Total de Pessoas do Nordeste: ')
    escreve2004.write(str(reg2_cont))
    escreve2004.write('\n2004 - Total de Pessoas do Sudeste: ')
    escreve2004.write(str(reg3_cont))
    escreve2004.write('\n2004 - Total de Pessoas do Sul: ')
    escreve2004.write(str(reg4_cont))
    escreve2004.write('\n2004 - Total de Pessoas do Centro-Oeste: ')
    escreve2004.write(str(reg5_cont))

