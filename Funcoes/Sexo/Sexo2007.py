def Calc_sexo2007(arq_2007):
    linha_cont = 0
    sexom_cont = 0
    sexof_cont = 0
    quant_sexo2007 = dict()

    dados2007 = open(arq_2007, 'r', encoding='ISO-8859-1')
    l = dados2007.readlines()

    dados2007.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_sexo2007[linha_cont] = linha_dados[10]

    escreve2007 = open('Imprime_dados/Sexo/quantitativo_candidatos_sexo_2007.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_sexo2007[cont_linha] == '1':
            sexom_cont += 1

        if quant_sexo2007[cont_linha] == '2':
            sexof_cont += 1



    escreve2007.write('2007 - Pessoas do Sexo Masculino: ')
    escreve2007.write(str(sexom_cont))
    escreve2007.write('\n2007 - Pessoas do Sexo Feminino: ')
    escreve2007.write(str(sexof_cont))