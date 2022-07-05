import pandas as pd
import os
from sklearn.neural_network import MLPRegressor
import numpy as np
import pickle

cwd = os.getcwd()

path_archivo = os.path.join(cwd,"data_lake/business/features/precios_diarios.csv")
path_salida = os.path.join(cwd,"src/models/precios-diarios.pkl")


def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    data = leer_datos()
    entrenar(data[0],data[1])
    #print(data)
    #raise NotImplementedError("Implementar esta función")

def entrenar(X, observed_scaled):
    np.random.seed(123456)

    H = 1  # Se escoge arbitrariamente

    mlp = MLPRegressor(
        hidden_layer_sizes=(H,),
        activation="logistic",
        learning_rate="adaptive",
        momentum=0.0,
        learning_rate_init=0.1,
        max_iter=10000,
    )

    # Entrenamiento
    mlp.fit(X[0:215], observed_scaled[0:215])  # 239 - 24 = 215

    pickle.dump( mlp , open( path_salida , 'wb' ) )




def leer_datos():
    datos = pd.read_csv(path_archivo)
    return (
        datos[[ str(i) for i in range(13)]].to_numpy(),
        datos["precio_transformado"].to_numpy()
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    train_daily_model()