def Calc_totalMun2006(arq_2006):
    linha_cont = 0
    mun1_lista = []
    quant_tMun2006 = dict()
    quant_tMun2006_2 = dict()

    dados2006 = open(arq_2006, 'r', encoding='ISO-8859-1')
    l = dados2006.readlines()

    dados2006.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        linha_dados2 = l[linha_cont].split(";")
        quant_tMun2006[linha_cont] = int(linha_dados[7])
        quant_tMun2006_2[linha_cont] = str(linha_dados2[12])

    escreve2006 = open('Imprime_dados/TotalMun/quantitativo_candidatos_totalmun_2006.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):
        if quant_tMun2006_2[cont_linha] not in mun1_lista:
            if quant_tMun2006[cont_linha] == 33:
                print(quant_tMun2006_2[cont_linha])
                mun1_lista.append(quant_tMun2006_2[cont_linha])
    escreve2006.write('2006 - MUNICÍPIOS DO RIO: ')
    escreve2006.write(str(mun1_lista))
