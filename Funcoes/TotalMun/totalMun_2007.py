def Calc_totalMun2007(arq_2007):
    linha_cont = 0
    mun1_lista = []
    quant_tMun2007 = dict()
    quant_tMun2007_2 = dict()

    dados2007 = open(arq_2007, 'r', encoding='ISO-8859-1')
    l = dados2007.readlines()

    dados2007.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        linha_dados2 = l[linha_cont].split(";")
        quant_tMun2007[linha_cont] = int(linha_dados[6])
        quant_tMun2007_2[linha_cont] = str(linha_dados2[11])

    escreve2007 = open('Imprime_dados/TotalMun/quantitativo_candidatos_totalmun_2007.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):
        if quant_tMun2007_2[cont_linha] not in mun1_lista:
            if quant_tMun2007[cont_linha] == 33:
                mun1_lista.append(quant_tMun2007_2[cont_linha])
    escreve2007.write('2007 - MUNICÍPIOS DO RIO: ')
    escreve2007.write(str(mun1_lista))
