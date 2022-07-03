
import sys
import time
import luigi

sys.path.append("src/data")


import ingest_data
import transform_data
import clean_data
import compute_daily_prices
import compute_monthly_prices
    

class IngestData(luigi.Task):

    def output(self):
        return luigi.LocalTarget('ingest.log')

    def run(self):
        with self.output().open('w') as f:
            ingest_data.ingest_data()
            #ingest_data.ingest_data()
            
            

            f.write('ingest data')
        
class TransformData(luigi.Task):

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      transform_data.transform_data()



    def requires(self):
        return IngestData()

    def output(self):
        return luigi.LocalTarget('transform.log')

    def run(self):
        pass
        
        #with self.input().open('r') as i:
        #     f = self.output().open('w')
        #     b = transform_data.transform_data()
        #     time.sleep(30)
        #     f.write(str(b))   
        #     f.close()         

class CleanData(luigi.Task):

    def requires(self):
        return [IngestData(),TransformData()]

    def output(self):
        return luigi.LocalTarget('clean.log')

    def run(self):
        with self.output().open('w') as f:
            
            clean_data.clean_data()
            f.write('clean data')

class ComputeDailyPrices(luigi.Task):


    def requires(self):
        return [IngestData(),TransformData(),CleanData()]

    def output(self):
        return luigi.LocalTarget('compute_daily.log')

    def run(self):
         with self.output().open('w') as f:
            
            compute_daily_prices.compute_daily_prices()
            f.write('compute Daily')

class ComputeMounthlyPrices(luigi.Task):


    def requires(self):
        return [ComputeDailyPrices()]

    def output(self):
        return luigi.LocalTarget('compute_mounthly.log')

    def run(self):
         with self.output().open('w') as f:
            
            compute_monthly_prices.compute_monthly_prices()
            f.write('compute mounthly')

"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""


    # raise NotImplementedError("Implementar esta función")
    #luigi.build([IngestData(),TransformData(),CleanData(),ComputeDailyPrices(),ComputeMounthlyPrices()], local_scheduler=True)
    

if __name__ == "__main__":
    import doctest

    #luigi.build([IngestData(),TransformData(),CleanData(),ComputeDailyPrices(),ComputeMounthlyPrices()])
    #luigi.build([IngestData(),TransformData(),CleanData(),ComputeDailyPrices(),ComputeMounthlyPrices()])

    luigi.run(["TransformData"])

    doctest.testmod()
