from operator import imod
import os
import pandas as pd
import compute_monthly_prices

cwd=os.getcwd()



class TestIngrestData:

    def test_ingest_data(self):
        compute_monthly_prices.compute_monthly_prices()
        path = os.path.join(cwd, 'data_lake/business/precios-mensuales.csv')
        assert os.path.exists(path) is True





