import clean_data
import os


path_archivo = "data_lake/cleansed/precios-horarios.csv"

class TestIngrestData:

    def test_ingest_data(self):
        clean_data.clean_data()
        assert os.path.exists(path_archivo) is True





