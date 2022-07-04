

import pandas as pd
import os

cwd=os.getcwd()

path_landing = os.path.join(cwd, 'data_lake/landing/') 
path_raw = os.path.join(cwd, 'data_lake/raw/') 
#list_files = os.listdir(path_landing)


def set_columnas(col):
    """
    Funcion qur pasa un numero a texto
    >>> set_columnas(10)
    '10'
    """
    try :
        return str(int(col))
    except:
        return str(col)

def guardar_df(file,path_raw,df):
    """
    Funcion para guardar el df como csv
    """
    nombre = file.split(".")[0] 
    path = path_raw + nombre + '.csv'
    df.to_csv(path,index=False,header=True)
    return path

def set_hora(hora):
    """
    Funcion que formatea la hora como H00
    >>> set_hora(15)
    'H15'
    """
    if int(hora) < 10:
        return "H0" + str(int(hora)) 
    else:
        return "H" + str(int(hora))

def set_esquema(df,horas=24):
    """
    Funcion que transforma los data a un esquema desterminado
    por el numero de horas que se quiere ver
    >>> import pandas as pd
    >>> data = {'Fecha':[1],'0':[2],'1':[3],'otro':[2]}
    >>> df = pd.DataFrame(data=data)
    >>> set_esquema(df,2)
       Fecha  0  1
    0      1  2  3
    """
    esquema = ["Fecha"] + [str(int(hora)) for hora in range(horas)]
    df_energia_filtrado = df[esquema]

    return df_energia_filtrado

def load_df(file):
    """
    Funcion para leer archivo de excel
    """
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

    return df_energia_filtrado


def transform_df(df,horas=24):
    """
    Funcion que transforma el df 
    >>> import pandas as pd
    >>> data = {'Fecha':[1,2],'0':[2,2],'1':[3,3],'2':[5,1]}
    >>> df = pd.DataFrame(data=data)
    >>> transform_df(df,3)
       fecha hora  precio
    0      1  H00       2
    1      2  H00       2
    2      1  H01       3
    3      2  H01       3
    4      1  H02       5
    5      2  H02       1
    """
    df_transformado = pd.melt(df,id_vars=['Fecha'],value_vars=[str(fecha) for fecha in range(horas)])
    df_transformado = df_transformado.rename(columns={"Fecha" : "fecha" , "variable":"hora","value":"precio"})
    df_transformado['hora'] = df_transformado.apply(lambda row : set_hora(row['hora']),axis=1)

    return df_transformado

    

    # esquema = ["Fecha"] + [str(int(hora)) for hora in range(24)]
    # df_energia_filtrado = df_energia_filtrado[esquema]

    # df_energia_filtrado.index = df_energia_filtrado[list(df_energia_filtrado.columns.values)[0]]

    # df_energia_filtrado = df_energia_filtrado.drop_duplicates( subset = list(df_energia_filtrado.columns.values)[0], keep='first',inplace=False)

    # df_transformado = transformar_df(df_energia_filtrado)
    # return df_transformado

# def transformar_df(df):
#     df_inicial = df.copy()
   
#     df_transpuesta = df_inicial.T
#     df_transpuesta = df_transpuesta.iloc[1:,:]
#     arreglo_fechas = list(df_transpuesta.columns)

#     arreglo_df = []

#     for fecha in arreglo_fechas:

#         serie_fecha = { "precio" : df_transpuesta[fecha] }

#         df_fecha = pd.DataFrame(serie_fecha)
#         df_fecha["fecha"] = fecha

#         arreglo_df.append(df_fecha)

#     df_completo = pd.concat(arreglo_df,sort=False)
#     df_completo['hora'] = df_completo.index
#     df_completo = df_completo[['fecha','hora','precio']]

#     df_completo['hora'] = df_completo.apply(lambda row : set_hora(row['hora']),axis=1)

#     return df_completo

def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """

    try :

        list_files = os.listdir(path_landing)
        for file in list_files:
            df_energia = load_df(file)
            df_esquema = set_esquema(df_energia)
            df_transformado = transform_df(df_esquema)
            guardar_df(file,path_raw,df_transformado)
    except :
        raise Exception("error al transformar los datos")





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

#        df_transformado = get_df(file)
#       guardar_df(file,path_raw,df_transformado)
        # nombre = file.split(".")[0] 
        # df_transformado.to_csv(path_raw + nombre + '.csv',index=False,header=True)
        
        # if list(df_energia_filtrado.columns.values)[0].upper() != "FECHA":
        #     df_energia_filtrado.to_csv(path_raw + nombre + '.csv',index=False,header=False)
        # else :
        #     df_energia_filtrado.to_csv(path_raw + nombre + '.csv',index=False,header=True)
      
        

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    transform_data()
