import ingest_data
import os
import esquema_data as esquema
import pandas as pd




class TestIngrestData:

    def test_ingest_data(self):
        ingest_data.ingest_data()
        for path_archivos in esquema.get_esquema():
            assert os.path.exists(path_archivos) is True

    def test_cargar_pandas(self):
        #ingest_data.ingest_data()
        try:
            pd.read_excel(esquema.get_esquema()[0])
        except:
            assert False





