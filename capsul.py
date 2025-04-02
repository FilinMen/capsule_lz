import getpass
from datetime import date, datetime
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from log import log

class Weather:

    @log
    def __init__(self):
        self

    def day(self):

        df = pd.read_csv('heavy.csv', usecols= ['MONTH','BASEL_sunshine'])
        names = ['January','February','March','April','May','June','July','August','September','October','November','December']

        for i in range(1,len(names)+1):
            df['MONTH'] = df['MONTH'].replace(i, names[i-1]) # Замена числовых месяцев на названия
        df = df.groupby('MONTH')['BASEL_sunshine'].sum()

        fig, ax = plt.subplots()
        ax = df.plot(kind='barh', x='MONTH', y='BASEL_sunshine', title='number of sunny days per year', color='white')# Построение горизонтальной диаграммы

        fig.patch.set_facecolor('#0000B2')  # Фон всей области графика
        ax.set_facecolor('#0000B2')     

        for i, v in enumerate(df): #текст с количеством рядом с каждым столбцом
            ax.text(v + 1, i, str(v), color='white', va='center', fontsize=10)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.tick_params(colors='white')  # Цвет отметок на осях
        ax.xaxis.label.set_color('white')  # Цвет подписи оси X
        ax.yaxis.label.set_color('white')  # Цвет подписи оси Y
        ax.title.set_color('white')        # Цвет заголовка
        # Добавляем подписи к осям
        plt.xlabel('day')
        plt.ylabel('month')
        # Plot formatting
        plt.legend()
        plt.show()

    def __del__(self): #деструктор
        print("del done")


def main(): 

    weather = Weather()
    weather.day()

if __name__ == "__main__":
    main()