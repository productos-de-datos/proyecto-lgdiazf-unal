"""
Modulo para test de la funcion create
datalake
"""
import os
import  create_data_lake
import esquema_data_lake as esquema



def test_crear_data_lake():
    """
    asegura la creacion del datalake
    """
    os.system("rm -rf data_lake")

    create_data_lake.create_data_lake()
    for path_carpeta in esquema.esquema:
        assert os.path.exists(path_carpeta) is True

    os.system("rm -rf data_lake")
