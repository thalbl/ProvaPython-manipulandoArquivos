from Funcoes.Idade.Idade2004 import Calc_idade2004
from Funcoes.Idade.Idade2005 import Calc_idade2005
from Funcoes.Idade.Idade2006 import Calc_idade2006
from Funcoes.Idade.Idade2007 import Calc_idade2007
from Funcoes.Idade.Idade2008 import Calc_idade2008
from Funcoes.Sexo.Sexo2004 import Calc_sexo2004
from Funcoes.Sexo.Sexo2005 import Calc_sexo2005
from Funcoes.Sexo.Sexo2006 import Calc_sexo2006
from Funcoes.Sexo.Sexo2007 import Calc_sexo2007
from Funcoes.Sexo.Sexo2008 import Calc_sexo2008
from Funcoes.Total.totalRegiao_2004 import Calc_totalReg2004
from Funcoes.Total.totalRegiao_2005 import Calc_totalReg2005
from Funcoes.Total.totalRegiao_2006 import Calc_totalReg2006
from Funcoes.Total.totalRegiao_2007 import Calc_totalReg2007
from Funcoes.Total.totalRegiao_2008 import Calc_totalReg2008
from Funcoes.Total2.totalP_2004 import Calc_totalP2004
from Funcoes.Total2.totalP_2005 import Calc_totalP2005
from Funcoes.Total2.totalP_2006 import Calc_totalP2006
from Funcoes.Total2.totalP_2007 import Calc_totalP2007
from Funcoes.Total2.totalP_2008 import Calc_totalP2008
from Funcoes.TotalMun.totalMun_2004 import Calc_totalMun2004
from Funcoes.TotalMun.totalMun_2005 import Calc_totalMun2005
from Funcoes.TotalMun.totalMun_2006 import Calc_totalMun2006
from Funcoes.TotalMun.totalMun_2007 import Calc_totalMun2007
from Funcoes.TotalMun.totalMun_2008 import Calc_totalMun2008

print('Gerando arquivo 2004: ')

arq_2004 = 'Anos/2004/2.DADOS/microdados_enade_2004.csv'
arq_2005 = 'Anos/2005/2.DADOS/microdados_enade_2005.csv'
arq_2006 = 'Anos/2006/2.DADOS/microdados_enade_2006.csv'
arq_2007 = 'Anos/2007/2.DADOS/microdados_enade_2007.csv'
arq_2008 = 'Anos/2008/2.DADOS/microdados_enade_2008.csv'

Calc_idade2004(arq_2004)
Calc_sexo2004(arq_2004)
Calc_totalReg2004(arq_2004)
Calc_totalP2004(arq_2004)
Calc_totalMun2004(arq_2004)

print('Gerando arquivo 2005: ')

Calc_idade2005(arq_2005)
Calc_sexo2005(arq_2005)
Calc_totalReg2005(arq_2005)
Calc_totalP2005(arq_2005)
Calc_totalMun2005(arq_2005)


print('Gerando arquivo 2006: ')

Calc_idade2006(arq_2006)
Calc_sexo2006(arq_2006)
Calc_totalReg2006(arq_2006)
Calc_totalP2006(arq_2006)
Calc_totalMun2006(arq_2006)

print('Gerando arquivo 2007: ')

Calc_idade2007(arq_2007)
Calc_sexo2007(arq_2007)
Calc_totalReg2007(arq_2007)
Calc_totalP2007(arq_2007)
Calc_totalMun2007(arq_2007)

print('Gerando arquivo 2008: ')

Calc_idade2008(arq_2008)
Calc_sexo2008(arq_2008)
Calc_totalReg2008(arq_2008)
Calc_totalP2008(arq_2008)
Calc_totalMun2008(arq_2008)

print('GERAÇÃO DE ARQUIVOS CONCLUIDA, VERIFICAR PASTA IMPRIME_DADOS.')
