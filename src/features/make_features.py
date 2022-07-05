import os
import pandas as pd

cwd = os.getcwd()

path_datos = os.path.join(cwd,"data_lake/business/precios-diarios.csv")
path_salida = os.path.join(cwd,"data_lake/business/features/precios-diarios.csv")

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
    df =  df.iloc[13: , :]

    df_variables_explicativas = get_df_variables_explicativas(df,p=13)

    df_completo = df.join(df_variables_explicativas)

    df_completo.to_csv(path_salida)





    
    #raise NotImplementedError("Implementar esta función")



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
