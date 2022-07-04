import pandas as pd
import matplotlib.pyplot as plt
import os

cwd = os.getcwd()

path_archivo = os.path.join(cwd, "data_lake/business/precios-diarios.csv")
path_imagen =  os.path.join(cwd,"data_lake/business/reports/figures/daily_prices.png") 

def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """


    #raise NotImplementedError("Implementar esta función")
    
    df = pd.read_csv(path_archivo)
    df.plot.line(x="fecha",y="precio")
    plt.savefig(path_imagen)


if __name__ == "__main__":
    import doctest
    make_daily_prices_plot()
    doctest.testmod()
