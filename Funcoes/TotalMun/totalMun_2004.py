def Calc_totalMun2004(arq_2004):
    linha_cont = 0
    mun1_lista = []
    quant_tMun2004 = dict()
    quant_tMun2004_2 = dict()

    dados2004 = open(arq_2004, 'r', encoding='ISO-8859-1')
    l = dados2004.readlines()

    dados2004.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        linha_dados2 = l[linha_cont].split(";")
        quant_tMun2004[linha_cont] = int(linha_dados[6])
        quant_tMun2004_2[linha_cont] = str(linha_dados2[11])

    escreve2004 = open('Imprime_dados/TotalMun/quantitativo_candidatos_totalmun_2004.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):
        if quant_tMun2004_2[cont_linha] not in mun1_lista:
            if quant_tMun2004[cont_linha] == 33:
                print(quant_tMun2004_2[cont_linha])
                mun1_lista.append(quant_tMun2004_2[cont_linha])
    escreve2004.write('2004 - MUNICÍPIOS DO RIO: ')
    escreve2004.write(str(mun1_lista))
