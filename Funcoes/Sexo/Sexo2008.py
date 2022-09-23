def Calc_sexo2008(arq_2008):
    linha_cont = 0
    sexom_cont = 0
    sexof_cont = 0
    quant_sexo2008 = dict()

    dados2008 = open(arq_2008, 'r', encoding='ISO-8859-1')
    l = dados2008.readlines()

    dados2008.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_sexo2008[linha_cont] = int(linha_dados[11])

    escreve2008 = open('Imprime_dados/Sexo/quantitativo_candidatos_sexo_2008.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_sexo2008[cont_linha] == 1:
            sexom_cont += 1

        if quant_sexo2008[cont_linha] == 2:
            sexof_cont += 1



    escreve2008.write('2008 - Pessoas do Sexo Masculino: ')
    escreve2008.write(str(sexom_cont))
    escreve2008.write('\n2008 - Pessoas do Sexo Feminino: ')
    escreve2008.write(str(sexof_cont))