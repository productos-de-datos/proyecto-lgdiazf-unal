

import pandas as pd
import os

cwd=os.getcwd()



path_landing = os.path.join(cwd, 'data_lake/landing/') 
path_raw = os.path.join(cwd, 'data_lake/raw/') 
list_files = os.listdir(path_landing)


def set_columnas(col):
    try :
        return str(int(col))
    except:
        return str(col)


def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """

    for file in list_files:
        # nombre = file.split(".")[0] 
        # try :
        #     df_energia = pd.read_excel(path_landing + file,engine='openpyxl')
        # except :
        #     df_energia = pd.read_excel(path_landing + file )
        # df_energia_filtrado = df_energia.dropna(thresh=23)

        # if list(df_energia_filtrado.columns.values)[0].upper() != "FECHA":
        #     df_arreglo = df_energia_filtrado.copy()
        #     header = df_arreglo.iloc[0].apply(set_columnas)
        #     df_energia_filtrado = df_arreglo.rename(columns = header)
        #     df_energia_filtrado = df_energia_filtrado.iloc[1: , :]

        # esquema = ["Fecha"] + [str(int(hora)) for hora in range(24)]
        # df_energia_filtrado = df_energia_filtrado[esquema]

        # df_energia_filtrado.index = df_energia_filtrado[list(df_energia_filtrado.columns.values)[0]]

        # df_energia_filtrado = df_energia_filtrado.drop_duplicates( subset = list(df_energia_filtrado.columns.values)[0], keep='first',inplace=False)

        # df_transformado = transformar_df(df_energia_filtrado)

        df_transformado = get_df(file)
        guardar_df(file,path_raw,df_transformado)
        # nombre = file.split(".")[0] 
        # df_transformado.to_csv(path_raw + nombre + '.csv',index=False,header=True)



    return True
        



        
        # if list(df_energia_filtrado.columns.values)[0].upper() != "FECHA":
        #     df_energia_filtrado.to_csv(path_raw + nombre + '.csv',index=False,header=False)
        # else :
        #     df_energia_filtrado.to_csv(path_raw + nombre + '.csv',index=False,header=True)
      
        

    #raise NotImplementedError("Implementar esta función")

def guardar_df(file,path_raw,df):
    nombre = file.split(".")[0] 
    path = path_raw + nombre + '.csv'
    df.to_csv(path,index=False,header=True)
    return path


def get_df(file):
    try :
        df_energia = pd.read_excel(path_landing + file,engine='openpyxl')
    except :
        df_energia = pd.read_excel(path_landing + file )
    df_energia_filtrado = df_energia.dropna(thresh=23)

    if list(df_energia_filtrado.columns.values)[0].upper() != "FECHA":
        df_arreglo = df_energia_filtrado.copy()
        header = df_arreglo.iloc[0].apply(set_columnas)
        df_energia_filtrado = df_arreglo.rename(columns = header)
        df_energia_filtrado = df_energia_filtrado.iloc[1: , :]

    esquema = ["Fecha"] + [str(int(hora)) for hora in range(24)]
    df_energia_filtrado = df_energia_filtrado[esquema]

    df_energia_filtrado.index = df_energia_filtrado[list(df_energia_filtrado.columns.values)[0]]

    df_energia_filtrado = df_energia_filtrado.drop_duplicates( subset = list(df_energia_filtrado.columns.values)[0], keep='first',inplace=False)

    df_transformado = transformar_df(df_energia_filtrado)
    return df_transformado



def transformar_df(df):
    df_inicial = df.copy()
   
    df_transpuesta = df_inicial.T
    df_transpuesta = df_transpuesta.iloc[1:,:]
    arreglo_fechas = list(df_transpuesta.columns)

    arreglo_df = []

    for fecha in arreglo_fechas:

        serie_fecha = { "precio" : df_transpuesta[fecha] }

        df_fecha = pd.DataFrame(serie_fecha)
        df_fecha["fecha"] = fecha

        arreglo_df.append(df_fecha)

    df_completo = pd.concat(arreglo_df,sort=False)
    df_completo['hora'] = df_completo.index
    df_completo = df_completo[['fecha','hora','precio']]

    df_completo['hora'] = df_completo.apply(lambda row : set_hora(row['hora']),axis=1)

    return df_completo

def set_hora(hora):
    if int(hora) < 10:
        return "H0" + str(int(hora)) 
    else:
        return "H" + str(int(hora))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
