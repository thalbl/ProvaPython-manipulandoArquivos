##################################################################################
#  MEC/INEP/DAES (Diretoria de AvaliaÃ§Ã£o da EducaÃ§Ã£o Superior)                   # 
#  CoordenaÃ§Ã£o Geral de Controle de Qualidade da EducaÃ§Ã£o Superior               # 	
#--------------------------------------------------------------------------------#
#  Programa:                                                                     #
#  input_enade.R (Pasta "INPUTS")                 	                         #
#--------------------------------------------------------------------------------#
#  DescriÃ§Ã£o: 															                                     #
#  Programa para Leitura dos Microdados do enade 2008                            #
#                                                                                #
#********************************************************************************#
#  Obs: Para executar este programa Ã© necessÃ¡rio salvar o arquivo                #
# "microdados_enade_2008.csv" (Pasta "DADOS") no diretÃ³rio "C:\" do computador.	 #     
#                                                                                #  
#********************************************************************************#

microdados_enade <- read.csv("C:/microdados_enade_2008.csv",header=T,sep=";");

