import ingest_data
import os
import esquema_data as esquema
import pandas as pd

cwd=os.getcwd()



class TestIngrestData:


    def test_guardar_data(self):

        os.system("rm -rf .tmp")
        os.system("mkdir .tmp")
        url_archivo = "https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/1995.xlsx"
        path_archivo = os.path.join(cwd,".tmp/file.xlsx")
        ingest_data.guardar_data(url_archivo,path_archivo)
        assert os.path.exists(path_archivo) is True
        os.system("rm -rf .tmp")



    # def test_ingest_data(self):
    #     ingest_data.ingest_data()
    #     for path_archivos in esquema.get_esquema():
    #         assert os.path.exists(path_archivos) is True

    # def test_cargar_pandas(self):
    #     #ingest_data.ingest_data()
    #     try:
    #         path = os.path.join(cwd, esquema.get_esquema()[0])
    #         df = pd.read_excel(path,engine='openpyxl')
    #         print(df)
    #     except:
    #         assert False





