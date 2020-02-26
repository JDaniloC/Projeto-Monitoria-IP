from tkinter import *
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt

from utils.leitor import Leitor
from utils.carro import Carro
from utils.grafico import Grafico
from main import criaDataframe

class Programa:
    '''
    Interface gráfica
    '''
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Gráficos')
        self.widgets()
        self.carregado, self.veiculos, self.dataframe, self.dicionario, self.criadorDeGrafico  = False, [], None, {}, None
        
        self.janela.mainloop()

    def widgets(self):
        '''
        Carrega todos os widgets
        '''
        tipos, valores = ['bar', 'barh', 'line', 'hist', 'box', 'area', 'scatter'], ['marca', 'quilometragem', 'motor', 'transmissao', 'cor']

        Label(self.janela, text = 'Nome da pasta: ').grid(row = 0, column = 0)
        self.entrada = Entry(self.janela, width = 23, textvariable = StringVar(value = './database'))
        Button(self.janela, text = 'Carregar arquivos', command = self.carregar).grid(row = 0, column = 2)
        self.entrada.grid(row = 0, column = 1)

        Label(self.janela, text = 'Gráfico númerico (pandas): ').grid(row = 1, column = 0)
        self.pandas = StringVar(value = tipos[0])
        ttk.Combobox(self.janela, textvariable = self.pandas, values = tipos, state = 'readonly').grid(row = 1, column = 1)
        Button(self.janela, text = 'Plotar', width = 13, command = self.plotPandas).grid(row = 1, column = 2)

        Label(self.janela, text = 'Gráfico de barras: ').grid(row = 2, column = 0)
        self.vertical = StringVar(value = valores[2])
        ttk.Combobox(self.janela, textvariable = self.vertical, values = valores[2:], state = 'readonly').grid(row = 2, column = 1)
        Button(self.janela, text = 'plotar', width = 13, command = self.plotGraficoVertical).grid(row = 2, column = 2)

        Label(self.janela, text = 'Gráfico horizontal: ').grid(row = 3, column = 0)
        self.horizontal = StringVar(value = valores[3])
        ttk.Combobox(self.janela, textvariable = self.horizontal, values = valores[2:], state = 'readonly').grid(row = 3, column = 1)
        Button(self.janela, text = 'plotar', width = 13, command = self.plotGraficoHorizontal).grid(row = 3, column = 2)

        Label(self.janela, text = 'Gráfico de pizza: ').grid(row = 4, column = 0)
        self.pizza = StringVar(value = valores[4])
        ttk.Combobox(self.janela, textvariable = self.pizza, values = valores[2:], state = 'readonly').grid(row = 4, column = 1)
        Button(self.janela, text = 'plotar', width = 13, command = self.plotGraficoPizza).grid(row = 4, column = 2)

    def carregar(self):
        '''
        Tenta ler os arquivos e formatalos, se der errado devolve uma lista vazia
        '''
        self.veiculos = Carro.formatadorDeCarros(Leitor.lerArquivos(self.entrada.get()))

        if self.veiculos != []:
            self.carregado = True
            self.dataframe, self.dicionario = criaDataframe(['_Carro__modelo', '_Carro__etc'], self.veiculos, 'quilometragem')
            self.criadorDeGrafico = Grafico(self.dicionario)
        else:
            self.carregado = False
            messagebox.showwarning('Arquivo', "Pasta não encontrada ou arquivos vazios")

    def plotPandas(self):
        '''
        Plota o gráfico da quilometragem que é o único numérico de fato
        '''
        if self.carregado: 
            self.dataframe.plot(kind = self.pandas.get(), x = 'marca', y = 'quilometragem', figsize = (8, 7))
            plt.show()
        else: messagebox.showinfo('Aviso', 'Você precisa carregar os arquivos primeiro!')

    def plotGraficoVertical(self):
        '''
        Plota o gráfico de barras verticais
        '''
        if self.carregado: self.criadorDeGrafico.graficoDeBarras(self.vertical.get()) 
        else: messagebox.showinfo('Aviso', 'Você precisa carregar os arquivos primeiro!')
    
    def plotGraficoHorizontal(self):
        '''
        Plota o gráfico de barras horizontais
        '''
        if self.carregado: self.criadorDeGrafico.graficoDeBarrasDeLado(self.horizontal.get())
        else: messagebox.showinfo('Aviso', 'Você precisa carregar os arquivos primeiro!')
    
    def plotGraficoPizza(self):
        '''
        Plota o gráfico de pizza
        '''
        if self.carregado: self.criadorDeGrafico.graficoPizza(self.pizza.get()) 
        else: messagebox.showinfo('Aviso', 'Você precisa carregar os arquivos primeiro!')

if __name__ == '__main__':
    programa = Programa()