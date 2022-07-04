
import os
import create_data_lake as create_data_lake
import esquema_data_lake as esquema

class TestCreateDataLake:

    def test_crear_data_lake(self):
        os.system("rm -rf data_lake")

        create_data_lake.create_data_lake()
        for path_carpeta in esquema.esquema:
            assert os.path.exists(path_carpeta) is True

        os.system("rm -rf data_lake")