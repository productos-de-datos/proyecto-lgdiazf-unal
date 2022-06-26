"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""
import json
import requests
import os
cwd=os.getcwd()
from pathlib import Path


url_tree_repo = "https://api.github.com/repos/jdvelasq/datalabs/git/trees/master"



data_tree_repo : json  = requests.get(url_tree_repo).json()['tree']

def get_tree_sha(files:json,folder:str):
    path : str= ""
    for file in files:
        if file["path"] == folder:
            path = file["url"]
    return path

root = get_tree_sha(data_tree_repo,'datasets')
resp = requests.get(root)

subfolder = get_tree_sha(resp.json()['tree'],'precio_bolsa_nacional')
resp = requests.get(subfolder)

data_path =  get_tree_sha(resp.json()['tree'],'xls')
resp = requests.get(data_path)


def guardar_data(url:str,path:str):
  
  resp = requests.get(url, allow_redirects=True)
  filename = Path(path)
  filename.write_bytes(resp.content)
#   file = open(path, 'w')
#   file.write(resp.content)
#   file.close()



def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    for i in  resp.json()['tree']:
        url = 'https://raw.githubusercontent.com/jdvelasq/datalabs/master/datasets/precio_bolsa_nacional/xls/' + str(i["path"])
        path = os.path.join(cwd,"data_lake/landing/"+str(i['path']))
        guardar_data(url,path)
    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
