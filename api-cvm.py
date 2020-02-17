
#group list - lista os grupos de dados
'http://dados.cvm.gov.br/api/3/action/group_list'
#resultado:
"cias-abertas", 
"fundos-de-investimento",
"fundos-estruturados",
"participantes-intermediarios"
#Pacotes de dados existentes
'http://dados.cvm.gov.br/api/action/package_list'
#resultado:
"cia_aberta-cad", 
"cia_aberta-doc-dfp-bpa", 
"cia_aberta-doc-dfp-bpp", 
"cia_aberta-doc-dfp-dfc_md", 
"cia_aberta-doc-dfp-dfc_mi", 
"cia_aberta-doc-dfp-dmpl", 
"cia_aberta-doc-dfp-dre", 
"cia_aberta-doc-dfp-dva", 
"cia_aberta-doc-fre", 
"cia_aberta-doc-itr",
"distrpubl", 
"emissores", 
"fi-cad", 
"fidc-doc-inf_mensal",
"fi-doc-balancete",
"fi-doc-cda", 
"fi-doc-compl", 
"fi-doc-eventual", 
"fi-doc-extrato", #Extrato semanal
"fi-doc-inf_diario", 
"fi-doc-lamina", 
"fi-doc-perfil_mensal", 
"fie-cad", 
"fie-medidas", 
"fip-doc-inf_trimestral", 
"intermediario-cad"
# Url para verificar pacotes de dados (quais arquivos estão disponíveis)
'http://dados.cvm.gov.br/api/3/action/package_show?id=fidc-doc-inf_mensal'
#url para download de arquivos, neste caso os arquivos do pacote:fi-doc-inf_diario
'http://dados.cvm.gov.br/dataset/fi-doc-inf_diario'
# Url para verificar pacotes de dados (quais arquivos estão disponíveis) para fi-doc-inf_diario
'http://dados.cvm.gov.br/api/3/action/package_show?id=fi-doc-inf_diario'
#tag_show ?????
'http://dados.cvm.gov.br/api/3/action/tag_show?id=bfbb0044-359b-4084-89ca-f6ce8ac8d5a3'
#group show
'http://dados.cvm.gov.br/api/3/action/group_show?id=bfbb0044-359b-4084-89ca-f6ce8ac8d5a3'
