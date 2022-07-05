"""
Modulo para crear el datalake
"""
import os
import esquema_data_lake


def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    |___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         |___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```
    Para crear crear las carpetas que componen el datalake se debe ejecutar :
    >>> create_data_lake()
    True
    """
    for path_carpeta in esquema_data_lake.get_esquema():
        try:
            if not os.path.exists(path_carpeta):
                path_absoluto = os.path.join(os.getcwd(), path_carpeta)
                os.mkdir(path_absoluto)
            return True
        except  FileNotFoundError  :
            return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
