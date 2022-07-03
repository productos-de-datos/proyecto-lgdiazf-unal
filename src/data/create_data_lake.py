import os
import esquema_data_lake



def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```
    >>> create_data_lake()
    """
    for path_carpeta in esquema_data_lake.get_esquema():
        try:
            if not os.path.exists(path_carpeta):
                path_absoluto = os.path.join(os.getcwd(),path_carpeta)
                os.mkdir(path_absoluto)
        except :
            raise Exception("no se pudo crear la carpeta")




if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
    #create_data_lake()
