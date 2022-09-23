def Calc_sexo2004(arq_2004):
    linha_cont = 0
    sexom_cont = 0
    sexof_cont = 0
    quant_sexo2004 = dict()

    dados2004 = open(arq_2004, 'r', encoding='ISO-8859-1')
    l = dados2004.readlines()

    dados2004.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_sexo2004[linha_cont] = int(linha_dados[10])

    escreve2004 = open('Imprime_dados/Sexo/quantitativo_candidatos_sexo_2004.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_sexo2004[cont_linha] == 1:
            sexom_cont += 1

        if quant_sexo2004[cont_linha] == 2:
            sexof_cont += 1



    escreve2004.write('2004 - Pessoas do Sexo Masculino: ')
    escreve2004.write(str(sexom_cont))
    escreve2004.write('\n2004 - Pessoas do Sexo Feminino: ')
    escreve2004.write(str(sexof_cont))

