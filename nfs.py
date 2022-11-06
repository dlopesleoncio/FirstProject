import os
import csv
import xml.etree.ElementTree as ET
import sdatabase as sd

data = []

header = ['fornecedor','produto','nota fiscal']
def obter_nome(arquivo):
	tree = ET.parse(arquivo)
	root = tree.getroot()
	nome = []
	prod = []
	idd = []
	
	for child in root.iter():
		if child.tag == "{http://www.portalfiscal.inf.br/nfe}xNome":
			nome.append(child.text)
		if child.tag =="{http://www.portalfiscal.inf.br/nfe}xProd":
			prod.append(child.text)
		if child.tag == "{http://www.portalfiscal.inf.br/nfe}infNFe":
			idd.append(child.attrib)

	data.append([nome[0],prod[0],idd[0]])
	sd.database(nome[0],prod[0],str(idd[0]))

#diretorio onde está o os arquivos xml
cwd = os.getcwd()
dirnfs = "NFS/042021"

diretorio = cwd + dirnfs
def obter_arquivos_xml(diretorio):
    ret = []
    for arq in os.listdir( diretorio ):
        if arq.endswith(".xml"):
            ret.append( os.path.join( diretorio, arq ) )
    return ret
ret = obter_arquivos_xml(diretorio)

for arquivo in ret:
	obter_nome(arquivo)

with open('database.csv','w',newline='') as f:
	writer = csv.writer(f)
	writer.writerow(header)

	writer.writerows(data)

sd.inserdata()