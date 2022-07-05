import pandas as pd
import os
from pyparsing import col
from sklearn.neural_network import MLPRegressor
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler

cwd = os.getcwd()

path_datos = os.path.join(cwd,"data_lake/business/precios-diarios.csv")
path_archivo = os.path.join(cwd,"data_lake/business/features/precios_diarios.csv")
path_modelo = os.path.join(cwd,"src/models/precios-diarios.pkl")
path_salida = os.path.join(cwd,"data_lake/business/forecasts/precios-diarios.csv")

def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """

    data = leer_datos()
    modelo = load_model()

    y_scaled_m1 = modelo.predict(data[0])
    df_y_m1 = pd.DataFrame(get_precio_transformado(y_scaled_m1)).rename(columns={0:"pronostico"})
    df_z = get_datos_reales()

    df_completo = df_y_m1.join(df_z)[["fecha","precio","pronostico"]]

    df_completo.to_csv(path_salida,index=False,header=True)

    #raise NotImplementedError("Implementar esta función")


def leer_datos():
    datos = pd.read_csv(path_archivo)
    return (
        datos[[ str(i) for i in range(13)]].to_numpy(),
        datos["precio_transformado"].to_numpy()
        )

def load_model():

    modelo = pickle.load( open( path_modelo , 'rb' ))

    return modelo


def get_precio_transformado(y_scaled_m1):

    df = pd.read_csv(path_datos)
    data = list(df["precio"])
    # crea el transformador
    scaler = MinMaxScaler()

    # escala la serie
    data_scaled = scaler.fit_transform(np.array(data).reshape(-1, 1))

    # z es un array de listas como efecto
    # del escalamiento
    data_scaled = [u[0] for u in data_scaled]

    y_m1 = scaler.inverse_transform([[u] for u in y_scaled_m1])
    y_m1 = [u[0] for u in y_m1]

    return y_m1

def get_datos_reales():
    df = pd.read_csv(path_datos)
    return df[["fecha","precio"]]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_forecasts()