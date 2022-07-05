import pandas as pd

import os

cwd = os.getcwd()

path_datos = os.path.join(cwd, "data_lake/cleansed/precios-horarios.csv")
path_datos_computados = os.path.join(cwd, "data_lake/business/precios-mensuales.csv")


def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    df_datos = pd.read_csv(path_datos)
    # df_datos[["fecha"]] = df_datos[["fecha"]].apply(pd.to_datetime)
    # df_datos.index = df_datos["fecha"]
    # grupo_df_datos = df_datos.groupby(pd.Grouper(freq="M"))
    # df_consolidado = grupo_df_datos['precio'].mean()

    df_formateado = format_df(df_datos)
    guardar_df(df_formateado, path_datos_computados)


# df_consolidado.to_csv(path_datos_computados ,index=True,header=True)

# raise NotImplementedError("Implementar esta función")


def format_df(df_datos):
    df_datos[["fecha"]] = df_datos[["fecha"]].apply(pd.to_datetime)
    df_datos.index = df_datos["fecha"]
    grupo_df_datos = df_datos.groupby(pd.Grouper(freq="M"))
    df_consolidado = grupo_df_datos["precio"].mean()

    return df_consolidado


def guardar_df(df, path):
    df.to_csv(path, index=True, header=True)


if __name__ == "__main__":
    import doctest

    compute_monthly_prices()

    doctest.testmod()
