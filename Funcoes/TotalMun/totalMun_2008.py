def Calc_totalMun2008(arq_2008):
    linha_cont = 0
    mun1_lista = []
    quant_tMun2008 = dict()
    quant_tMun2008_2 = dict()

    dados2008 = open(arq_2008, 'r', encoding='ISO-8859-1')
    l = dados2008.readlines()

    dados2008.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        linha_dados2 = l[linha_cont].split(";")
        quant_tMun2008[linha_cont] = int(linha_dados[7])
        quant_tMun2008_2[linha_cont] = str(linha_dados2[8])

    escreve2008 = open('Imprime_dados/TotalMun/quantitativo_candidatos_totalmun_2008.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):
        if quant_tMun2008_2[cont_linha] not in mun1_lista:
            if quant_tMun2008[cont_linha] == 33:
                print(quant_tMun2008_2[cont_linha])
                mun1_lista.append(quant_tMun2008_2[cont_linha])
    escreve2008.write('2008 - MUNICÍPIOS DO RIO: ')
    escreve2008.write(str(mun1_lista))
