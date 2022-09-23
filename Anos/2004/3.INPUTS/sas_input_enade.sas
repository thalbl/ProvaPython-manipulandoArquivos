/*************************************************************************
 MEC/INEP/DAES (Diretoria de Avalia��o da Educa��o Superior)             
 Coordena��o Geral de Controle de Qualidade da Educa��o Superior         	
--------------------------------------------------------------------------
Programa:                                                              
	input_enade.sas (Pasta "INPUTS")                 	  
--------------------------------------------------------------------------
Descri��o: 															  
	Programa para Leitura dos Microdados do enade 2004            
                                                                         
**************************************************************************
 Obs: Para executar este programa � necess�rio salvar o arquivo          
 "microdados_enade_2004.csv" (Pasta "DADOS") no diret�rio "C:\" do computador.	      
															 			  
*************************************************************************/

proc import datafile="C:\microdados_enade_2004.csv"
    out=enade_2004
	dbms=dlm
    replace;
	delimiter=";";
run;


