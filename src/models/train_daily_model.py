import pandas as pd
import os
from sklearn.neural_network import MLPRegressor
import numpy as np

cwd = os.getcwd()

path_archivo = os.path.join(cwd,"data_lake/business/features/precios_diarios.csv")


def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    data = leer_data()
    print(data)
    #raise NotImplementedError("Implementar esta función")

def entrenar(datos):
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


def leer_data():
    datos = pd.read_csv(path_archivo)
    
    return list(datos["variables"])[:-13]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    train_daily_model()