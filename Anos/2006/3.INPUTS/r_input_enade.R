##################################################################################
#  MEC/INEP/DAES (Diretoria de Avaliação da Educação Superior)                   # 
#  Coordenação Geral de Controle de Qualidade da Educação Superior               # 	
#--------------------------------------------------------------------------------#
#  Programa:                                                                     #
#  r_input_enade.R (Pasta "INPUTS")                 	                         #
#--------------------------------------------------------------------------------#
#  Descrição: 															                                     #
#  Programa para Leitura dos Microdados do enade 2006                            #
#                                                                                #
#********************************************************************************#
#  Obs: Para executar este programa é necessário salvar o arquivo                #
# "microdados_enade_2006.csv" (Pasta "DADOS") no diretório "C:\" do computador.	 #     
#                                                                                #  
#********************************************************************************#

#microdados_enade <- read.table("C:/Users/sidney.arruda/Documents/microdados_enade_2006.csv",header=T,sep=";");
#Utilizando a função read.table retornou o resultado de registros a menos, sendo assim utilizei a função read.csv
microdados_enade <- read.csv("C:/Users/sidney.arruda/Documents/microdados_enade_2006.csv",header=T,sep=";");

