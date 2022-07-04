import clean_data
import os
import create_data_lake
import ingest_data
import transform_data 

path_archivo = "data_lake/cleansed/precios-horarios.csv"

class TestCleanData:

    def test_clean_data(self):

        os.system("rm -rf data_lake")
        create_data_lake.create_data_lake()
        ingest_data.ingest_data()
        transform_data.transform_data()
        clean_data.clean_data()
        assert os.path.exists(path_archivo) is True
        os.system("rm -rf data_lake")





