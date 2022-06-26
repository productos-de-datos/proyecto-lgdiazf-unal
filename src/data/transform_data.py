

import pandas as pd
import os

cwd=os.getcwd()



path_landing = os.path.join(cwd, 'data_lake/landing/') 
path_raw = os.path.join(cwd, 'data_lake/raw/') 
list_files = os.listdir(path_landing)





def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """

    for file in list_files:
        nombre = file.split(".")[0] 
        try :
            df_energia = pd.read_excel(path_landing + file,engine='openpyxl')
        except :
            df_energia = pd.read_excel(path_landing + file )
        df_energia_filtrado = df_energia.dropna(thresh=24)
        if list(df_energia_filtrado.columns.values)[0].upper() != "FECHA":
            df_energia_filtrado.to_csv(path_raw + nombre + '.csv',index=False,header=False)
        else :
            df_energia_filtrado.to_csv(path_raw + nombre + '.csv',index=False,header=True)
      
        

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
