import os
import pandas as pd
import create_data_lake
import ingest_data
import transform_data
import clean_data
import compute_daily_prices

cwd=os.getcwd()



class TesComputeDaily:

    def test_compute_daily(self):
        os.system("rm -rf data_lake")
        create_data_lake.create_data_lake()
        ingest_data.ingest_data()
        transform_data.transform_data()
        clean_data.clean_data()
        compute_daily_prices.compute_daily_prices()
        path = os.path.join(cwd, 'data_lake/cleansed/precios-horarios.csv')
        assert os.path.exists(path) is True
        os.system("rm -rf data_lake")





