import os

def obter_nome(arquivo):
	import xml.etree.ElementTree as ET
	tree = ET.parse(arquivo)
	root = tree.getroot()
	nome = []
	prod = []
	for child in root.iter():
		if child.tag == "{http://www.portalfiscal.inf.br/nfe}xNome":
			nome.append(child.text)
		if child.tag =="{http://www.portalfiscal.inf.br/nfe}xProd":
			prod.append(child.text)	
	print(nome[0], "\tProd: ",prod[0])
	


diretorio = "/home/solar/NFe08.2020/Entrada/674-I/082020/"
def obter_arquivos_xml(diretorio):
    ret = []
    for arq in os.listdir( diretorio ):
        if arq.endswith(".xml"):
            ret.append( os.path.join( diretorio, arq ) )
    return ret
ret = obter_arquivos_xml(diretorio)

for arquivo in ret:
	obter_nome(arquivo)
