/*************************************************************************
 MEC/INEP/DAES (Diretoria de Avalia��o da Educa��o Superior)             
 Coordena��o Geral de Controle de Qualidade da Educa��o Superior         	
--------------------------------------------------------------------------
Programa:                                                              
	sas_input_enade.sas (Pasta "INPUTS")                 	  
--------------------------------------------------------------------------
Descri��o: 															  
	Programa para Leitura dos Microdados do enade 2008            
                                                                         
**************************************************************************
 Obs: Para executar este programa � necess�rio salvar o arquivo          
 "microdados_enade_2008.csv" (Pasta "DADOS") no diret�rio "C:\" do computador.	      
															 			  
*************************************************************************/

proc import datafile="C:\microdados_enade_2008.csv"
     out=enade_2008
     dbms=dlm
     replace;
     delimiter=";";
run;
