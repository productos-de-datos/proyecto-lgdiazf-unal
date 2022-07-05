import luigi
import sys
import os
import pandas as pd

sys.path.append("src/data")

import ingest_data
import transform_data
import clean_data
import compute_daily_prices
import compute_monthly_prices


url_path_raw = 'https://raw.githubusercontent.com/jdvelasq/datalabs/master/datasets/precio_bolsa_nacional/xls/'
cwd=os.getcwd()

class TaskA(luigi.Task):

  def output(self):
    return luigi.LocalTarget('TaskA.output')

  def run(self):
    lista = ingest_data.get_file_list()
    with self.output().open('w') as f :
      for archivo in lista:
        url = url_path_raw  + str(archivo["path"])
        path = os.path.join(cwd,"data_lake/landing/" + str(archivo['path']))
        ingest_data.guardar_data(url,path)
        f.write(path+"\n")



class TaskB(luigi.Task):

    def output(self):
        return luigi.LocalTarget("TaskB.output")

    def requires(self):
        return TaskA()

    def run(self):
      path_raw = os.path.join(cwd, 'data_lake/raw/') 
      with self.input().open("r") as i:
        lineas = i.readlines()
        with self.output().open("w") as f:
          for linea in lineas:
            path = str(linea).replace("\n","").split("/")[-1]
            df_energia = transform_data.load_df(path)
            df_esquema = transform_data.set_esquema(df_energia)
            df_transformado = transform_data.transform_df(df_esquema)
            # df = transform_data.get_df(path)
            path_csv = transform_data.guardar_df(path,path_raw,df_transformado)
            f.write(path_csv+"\n")



class TaskC(luigi.Task):

  def arreglar_lista(self,linea):
    return linea.replace("\n","")

  def requires(self):
    return TaskB()

  def output(self):
    return luigi.LocalTarget('TaskC.output')

  def run(self):
    with self.input().open("r") as i:
      lineas = i.readlines()
      lista_archivos = list(lineas)
      lista_archivos = list(map(self.arreglar_lista,lista_archivos))
      df_completo = clean_data.get_df_completo(lista_archivos)
      df_formateado = clean_data.formatear_df(df_completo)
      path = os.path.join(cwd,"data_lake/cleansed/" + "precios-horarios.csv" )
      clean_data.guardar_df(path,df_formateado)
      with self.output().open("w") as f:
        f.write(path)
        
class TaskD(luigi.Task):

  def requires(self):
    return TaskC()

  def output(self):
    return luigi.LocalTarget('TaskD.output')

  def run(self):
    with self.input().open("r") as i:
      path_data = str(i.read())
      df_datos = pd.read_csv(path_data)
      df_promedio_diario = compute_daily_prices.get_datos(df_datos) 
      path_salida = os.path.join(cwd, 'data_lake/business/precios-diarios.csv')
      compute_daily_prices.guardar_df(path_salida,df_promedio_diario)
      with self.output().open("w") as f:
        f.write(path_salida)        

class TaskE(luigi.Task):

  def requires(self):
    return [TaskC(),TaskD()]

  def output(self):
    return luigi.LocalTarget('TaskE.output')

  def run(self):
    with self.input()[0].open("r") as i:
      path_data = str(i.read())
      df_datos = pd.read_csv(path_data)
      df_formateado =  compute_monthly_prices.format_df(df_datos)
      path_datos_computados = os.path.join(cwd, 'data_lake/business/precios-mensuales.csv')
      compute_monthly_prices.guardar_df(df_formateado,path_datos_computados)
      with self.output().open("w") as f:
        f.write(path_datos_computados)  


def correr_pipeline():
  luigi.run(["TaskE"],local_scheduler=True)


if __name__ == "__main__":
    import doctest
    luigi.run(["TaskE"],local_scheduler=True)

    #luigi.build([IngestData(),TransformData(),CleanData(),ComputeDailyPrices(),ComputeMounthlyPrices()])
    #luigi.build([IngestData(),TransformData(),CleanData(),ComputeDailyPrices(),ComputeMounthlyPrices()])

    