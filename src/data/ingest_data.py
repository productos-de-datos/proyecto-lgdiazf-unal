import json
import re
import requests
import os
from pathlib import Path

"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""

url_path_raw = "https://raw.githubusercontent.com/jdvelasq/datalabs/master/datasets/precio_bolsa_nacional/xls/"
url_tree_repo = "https://api.github.com/repos/jdvelasq/datalabs/git/trees/master"
cwd = os.getcwd()


def get_tree_sha(files, folder):
    """ "
    funcion que retorna la url de la subcarpeta *folder* dentro del arreglo de diccionarios *files*
    >>> files = [{ 'path' : 'folder1' , 'url' : 'https://1.com' },{ 'path' : 'folder2' , 'url' : 'https://2.com' }]
    >>> get_tree_sha(files,"folder1")
    'https://1.com'
    """
    url = [file["url"] for file in files if file["path"] == folder][0]
    return str(url)


def guardar_data(url, path):
    """
    Funcion que descarga el archivo desde la *url* y guarda el contenido en
    el *path*
    """
    response = requests.get(url, allow_redirects=True)
    filename = Path(path)
    filename.write_bytes(response.content)


def get_file_list():
    """
    funcion que retorna arreglo con diccionarios de los archivos que se
    van a descargar del repo
    >>> get_file_list()[0]['path']
    '1995.xlsx'
    """

    folders = ["datasets", "precio_bolsa_nacional", "xls"]

    root_folder_tree = requests.get(url_tree_repo)

    folder_tree = root_folder_tree

    for folder in folders:

        f = get_tree_sha(folder_tree.json()["tree"], folder)
        folder_tree = requests.get(f)

    return folder_tree.json()["tree"]


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    try:
        for archivo in get_file_list():
            url = url_path_raw + str(archivo["path"])
            path = os.path.join(cwd, "data_lake/landing/" + str(archivo["path"]))
            guardar_data(url, path)
    except:
        return False


if __name__ == "__main__":
    import doctest

    ingest_data()
    doctest.testmod()
