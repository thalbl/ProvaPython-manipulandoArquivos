/*************************************************************************
 MEC/INEP/DAES (Diretoria de Avaliação da Educação Superior)             
 Coordenação Geral de Controle de Qualidade da Educação Superior         	
--------------------------------------------------------------------------
Programa:                                                              
	input_enade.sas (Pasta "INPUTS")                 	  
--------------------------------------------------------------------------
Descrição: 															  
	Programa para Leitura dos Microdados do enade 2005            
                                                                         
**************************************************************************
 Obs: Para executar este programa é necessário salvar o arquivo          
 "microdados_enade_2005.csv" (Pasta "DADOS") no diretório "C:\" do computador.	      
															 			  
*************************************************************************/

proc import datafile="C:\microdados_enade_2005.csv"
    out=enade_2005
	dbms=dlm
    replace;
	delimiter=";";
run;


