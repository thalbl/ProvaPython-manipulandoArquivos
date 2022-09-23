def Calc_sexo2005(arq_2005):
    linha_cont = 0
    sexom_cont = 0
    sexof_cont = 0
    quant_sexo2005 = dict()

    dados2005 = open(arq_2005, 'r', encoding='ISO-8859-1')
    l = dados2005.readlines()

    dados2005.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_sexo2005[linha_cont] = int(linha_dados[10])

    escreve2005 = open('Imprime_dados/Sexo/quantitativo_candidatos_sexo_2005.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_sexo2005[cont_linha] == 1:
            sexom_cont += 1

        if quant_sexo2005[cont_linha] == 2:
            sexof_cont += 1



    escreve2005.write('2005 - Pessoas do Sexo Masculino: ')
    escreve2005.write(str(sexom_cont))
    escreve2005.write('\n2005 - Pessoas do Sexo Feminino: ')
    escreve2005.write(str(sexof_cont))