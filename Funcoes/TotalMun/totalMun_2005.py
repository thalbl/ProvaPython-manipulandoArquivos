def Calc_totalMun2005(arq_2005):
    linha_cont = 0
    mun1_lista = []
    quant_tMun2005 = dict()
    quant_tMun2005_2 = dict()

    dados2005 = open(arq_2005, 'r', encoding='ISO-8859-1')
    l = dados2005.readlines()

    dados2005.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        linha_dados2 = l[linha_cont].split(";")
        quant_tMun2005[linha_cont] = int(linha_dados[6])
        quant_tMun2005_2[linha_cont] = str(linha_dados2[11])

    escreve2005 = open('Imprime_dados/TotalMun/quantitativo_candidatos_totalmun_2005.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):
        if quant_tMun2005_2[cont_linha] not in mun1_lista:
            if quant_tMun2005[cont_linha] == 33:
                mun1_lista.append(quant_tMun2005_2[cont_linha])
    escreve2005.write('2005 - MUNICÍPIOS DO RIO: ')
    escreve2005.write(str(mun1_lista))
