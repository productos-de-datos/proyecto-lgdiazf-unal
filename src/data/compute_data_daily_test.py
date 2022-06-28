from operator import imod
import os
import pandas as pd
import compute_daily_prices

cwd=os.getcwd()



class TestIngrestData:

    def test_ingest_data(self):
        compute_daily_prices.compute_daily_prices()
        path = os.path.join(cwd, 'data_lake/cleansed/precios-horarios.csv')
        assert os.path.exists(path) is True





