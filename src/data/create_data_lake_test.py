import create_data_lake
import os
import esquema_data_lake as esquema




class TestCreateDataLake:
    def test_data_lake(self):
        create_data_lake.create_data_lake()
        for path_carpeta in esquema.esquema:
            assert os.path.exists(path_carpeta) is True