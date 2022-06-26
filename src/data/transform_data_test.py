import transform_data
import os
import esquema_data_csv as esquema


class TestTransformData:
    def test_data_lake(self):
        transform_data.transform_data()
        for path_carpeta in esquema.esquema:
            assert os.path.exists(path_carpeta) is True