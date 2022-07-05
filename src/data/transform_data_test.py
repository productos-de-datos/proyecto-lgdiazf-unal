import transform_data
import os
import esquema_data_csv as esquema
import create_data_lake
import ingest_data


class TestTransformData:
    def test_transform_data(self):
        os.system("rm -rf data_lake")
        create_data_lake.create_data_lake()
        ingest_data.ingest_data()
        transform_data.transform_data()
        for path_carpeta in esquema.esquema:
            assert os.path.exists(path_carpeta) is True
        os.system("rm -rf data_lake")
