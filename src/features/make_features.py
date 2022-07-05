import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

cwd = os.getcwd()

path_datos = os.path.join(cwd,"data_lake/business/precios-diarios.csv")
path_salida = os.path.join(cwd,"data_lake/business/features/precios_diarios.csv")
# coding=utf-8
def make_features():
    """Prepara datos para pronóstico.
    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """

    df = pd.read_csv(path_datos)
    # df =  df.iloc[13: , :]

    # df_variables_explicativas = get_df_variables_explicativas(df,p=13)

    # df_completo = df.join(df_variables_explicativas)

    # df_completo.to_csv(path_salida,index=False,header=True)

    data = get_precios(df)
    observed_scaled, X = get_precio_transformado(data)

    df1 = pd.DataFrame(X)
    df2 = pd.DataFrame(observed_scaled).rename(columns={0:"precio_transformado"})
    df3 =  df.iloc[13: , :]["fecha"]
    df3.index = [ i  for i in range(df3.shape[0]) ]


    df_completo = df1.join(df2).join(df3)
    df_completo.to_csv(path_salida,index=False,header=True)

    #print(pd.DataFrame(observed_scaled))
    #print(df.shape)







    
    #raise NotImplementedError("Implementar esta función")



def get_precios(df):
    return list(df["precio"])


def get_precio_transformado(data,P=13):
    # crea el transformador
    scaler = MinMaxScaler()

    # escala la serie
    data_scaled = scaler.fit_transform(np.array(data).reshape(-1, 1))

    # z es un array de listas como efecto
    # del escalamiento
    data_scaled = [u[0] for u in data_scaled]

    X = []
    for t in range(P - 1, len(data) - 1):
        X.append([data_scaled[t - n] for n in range(P)])

    observed_scaled = data_scaled[P:]

    return (observed_scaled,X)


def get_df_variables_explicativas(df,p=13):
    df_variables_explicativas = df.apply(lambda row : get_data(row.name,df,p),axis=1)
    df_variables_explicativas = df_variables_explicativas.to_frame()

    df_variables_explicativas = df_variables_explicativas.rename(columns={0 : "variables"})

    return df_variables_explicativas


def get_data(index,df,p):

    inicio = index - p
    final = inicio + p

    return list(df.iloc[inicio:final]["precio"])

if __name__ == "__main__":
    import doctest
    make_features()

    doctest.testmod()
