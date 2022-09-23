/*************************************************************************
 MEC/INEP/DAES (Diretoria de Avaliação da Educação Superior)             
 Coordenação Geral de Controle de Qualidade da Educação Superior         	
--------------------------------------------------------------------------
Programa:                                                              
	sas_input_enade.sas (Pasta "INPUTS")                 	  
--------------------------------------------------------------------------
Descrição: 															  
	Programa para Leitura dos Microdados do enade 2006            
                                                                         
**************************************************************************
 Obs: Para executar este programa é necessário salvar o arquivo          
 "microdados_enade_2006.csv" (Pasta "DADOS") no diretório "C:\" do computador.	      
															 			  
*************************************************************************/

proc import datafile="C:\Users\sidney.arruda\Documents\microdados_enade_2006.csv"
    	out=enade_2006
	dbms=dlm
    	replace;
	delimiter=";";
run;


