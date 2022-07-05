from operator import imod
import os

import create_data_lake
import ingest_data
import transform_data
import clean_data
import compute_monthly_prices

cwd = os.getcwd()



def test_compute_mounthly():
    os.system("rm -rf data_lake")
    create_data_lake.create_data_lake()
    ingest_data.ingest_data()
    transform_data.transform_data()
    clean_data.clean_data()
    compute_monthly_prices.compute_monthly_prices()
    path = os.path.join(cwd, "data_lake/business/precios-mensuales.csv")
    assert os.path.exists(path) is True
    os.system("rm -rf data_lake")
