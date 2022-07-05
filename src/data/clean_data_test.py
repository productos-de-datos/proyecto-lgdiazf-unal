"""
modulo para probar la funcion clean_data
"""
import os
from data import  clean_data
from data import create_data_lake
from data import ingest_data
from data import transform_data


PATH = "data_lake/cleansed/precios-horarios.csv"



def test_clean_data():
    """
    crear el datalake y realiza los pasos
    necesarios para poder ejecutar la funcion
    clean_data
    """
    os.system("rm -rf data_lake")
    create_data_lake.create_data_lake()
    ingest_data.ingest_data()
    transform_data.transform_data()
    clean_data.clean_data()
    assert os.path.exists(PATH) is True
    os.system("rm -rf data_lake")
