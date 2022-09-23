def Calc_sexo2006(arq_2006):
    linha_cont = 0
    sexom_cont = 0
    sexof_cont = 0
    quant_sexo2006 = dict()

    dados2006 = open(arq_2006, 'r', encoding='ISO-8859-1')
    l = dados2006.readlines()

    dados2006.close()

    for linha_cont in range(1, len(l)):
        linha_dados = l[linha_cont].split(";")
        quant_sexo2006[linha_cont] = int(linha_dados[11])

    escreve2006 = open('Imprime_dados/Sexo/quantitativo_candidatos_sexo_2006.csv', 'w', encoding='ISO-8859-1')
    for cont_linha in range(1, len(l)):

        if quant_sexo2006[cont_linha] == 1:
            sexom_cont += 1

        if quant_sexo2006[cont_linha] == 2:
            sexof_cont += 1



    escreve2006.write('2006 - Pessoas do Sexo Masculino: ')
    escreve2006.write(str(sexom_cont))
    escreve2006.write('\n2006 - Pessoas do Sexo Feminino: ')
    escreve2006.write(str(sexof_cont))