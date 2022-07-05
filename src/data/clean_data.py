"""
modulo para limpiar datos
"""
import doctest
from msilib.schema import Error
import os
import pandas as pd


cwd = os.getcwd()


path_raw = os.path.join(cwd, "data_lake/raw/")
path_cleansed = os.path.join(cwd, "data_lake/cleansed/")


def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo
    data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """


    list_archivos = get_lista_archivos()
    df_completo = get_df_completo(list_archivos)
    df_formateado = formatear_df(df_completo)
    guardar_df(path_cleansed + "precios-horarios.csv", df_formateado)


def guardar_df(path, df_guardar):
    """
    funcion para guardar df
    """
    df_guardar.to_csv(path, index=False, header=True)


def get_lista_archivos():
    """
    funcion para listar los archivos
    """
    lista = []
    list_files = os.listdir(path_raw)

    for archivo in list_files:
        year = int(archivo.split(".")[0])
        if 1997 <= year <= 2021:
            lista.append(path_raw + archivo)

    return lista


def get_df_completo(lista_archivos):
    """
    funcion que concatena los df
    """

    arreglo_df = []

    for archivo in lista_archivos:
        arreglo_df.append(pd.read_csv(archivo))

    df_completo = pd.concat(arreglo_df, sort=False)

    return df_completo


def set_hora(hora):
    """
    funcion que elimina el H de la hora
    """
    return hora[1:]


def formatear_df(df_completo):
    """
    funcion para cambiar la hora en todo el df
    """
    df_arreglo = df_completo.copy()
    df_arreglo["hora"] = df_arreglo.apply(lambda row: set_hora(row["hora"]), axis=1)

    return df_arreglo


if __name__ == "__main__":


    doctest.testmod()
    clean_data()
