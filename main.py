import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import os

class GraficoHP:
    def __init__(self, excel_file, title=None):
        self._excel_file = excel_file
        self._title = title or os.path.splitext(os.path.basename(excel_file))[0]
        self._x_label = 'X'
        self._y_label = 'Y'
        self._dataframe = None

    def _hp_filter(self):
        cycle, trend = sm.tsa.filters.hpfilter(self._dataframe['col1'])
        self._dataframe['cycle'] = cycle
        self._dataframe['trend'] = trend

    def _plot_original_data(self):
        plt.scatter(self._dataframe['col0'],
            self._dataframe['col1'], label='Original')

    def _plot_hp_trend(self):
        plt.plot(self._dataframe['col0'], self._dataframe['trend'],
            label='Tendência', color='red', linewidth=2)

    def plot(self):
        if self._dataframe is None:
            raise ValueError("O dataframe ainda não foi carregado. Chame 'load_data' antes de 'plot'.")

        self._hp_filter()

        plt.figure(figsize=(12, 8))

        self._plot_original_data()
        self._plot_hp_trend()

        plt.title(self._title)
        plt.xlabel(self._x_label)
        plt.ylabel(self._y_label)

        plt.xticks(rotation=45, ha='right')

        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def load_data(self):
      
        self._dataframe = pd.read_excel(self._excel_file,
            usecols=[0, 1], names=['col0', 'col1'])

excel_files = ['Formação bruta de capital fixo.xls',
               'horas trabalhadas - indústria.xls',
               'PIB - consumo final - APU -.xls',
               'PIB - preços de mercado.xls']

excel_folder_path = os.path.join(os.getcwd(), 'excel')

for excel_file in excel_files:
    file_path = os.path.join(excel_folder_path, excel_file)

    grafico = GraficoHP(file_path,
        title=os.path.splitext(os.path.basename(excel_file))[0])
    grafico.load_data()
    grafico.plot()
