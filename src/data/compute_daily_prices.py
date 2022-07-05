import pandas as pd
import os

cwd = os.getcwd()

path_datos = os.path.join(cwd, "data_lake/cleansed/precios-horarios.csv")
path_datos_computados = os.path.join(cwd, "data_lake/business/precios-diarios.csv")


def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



    """
    df_datos = pd.read_csv(path_datos)
    df_promedio_diario = get_datos(df_datos)
    guardar_df(path_datos_computados, df_promedio_diario)

    # df_promedio_diario.to_csv(path_datos_computados ,index=False,header=True)


# raise NotImplementedError("Implementar esta función")


def guardar_df(path, df):
    df.to_csv(path, index=False, header=True)


def get_datos(df_datos):

    dic_datos = {"fecha": [], "precio": []}

    grupo_df_diarios = df_datos.groupby("fecha")

    for titulo, df_diario in grupo_df_diarios:

        dic_datos["fecha"].append(titulo)
        dic_datos["precio"].append(df_diario[["precio"]].mean()[0])

    return pd.DataFrame.from_dict(dic_datos)


if __name__ == "__main__":
    import doctest

    compute_daily_prices()

    doctest.testmod()
