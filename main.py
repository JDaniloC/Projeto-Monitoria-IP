from leitor import Leitor
from carro import Carro
from grafico import Grafico
import pandas as pd

if __name__ == '__main__':
    # Obtenção dos dados
    veiculos = Carro.formatadorDeCarros(Leitor.lerArquivos('./database'))
    
    print("Todos os veículos")
    for i in veiculos: print(i, '\n')


    # Filtrando e montando um dicionário com os dados 
    excluir = ['_Carro__modelo', '_Carro__etc'] # O que não quero mostrar no dataframe
    dataframe = {key[8:]:[] for (key, value) in veiculos[0].__dict__.items() if key not in excluir}
        
    for carro in veiculos:
        for chave, valor in carro.__dict__.items():
            if chave not in excluir:
                dataframe[chave[8:]].append(valor)
    dataframe['quilometragem'] = [int(x) for x in dataframe['quilometragem']] # Transformando em int
    resultado = pd.DataFrame(dataframe) # Criando o dataframe do pandas a partir do dicionário
    
    print('- - ' * 20 + "\n" + "Pandas.DataFrame") # Não pode, é feio!!
    print(resultado)
    resultado.plot(kind='bar', x = 'marca', y = 'quilometragem', figsize = (8, 7),      #1
    title = "Quilometragem por marca")       

    
    # Manipulando o Matplotlib
    criadorDeGrafico = Grafico(dataframe)
    criadorDeGrafico.graficoDeBarras('motor', 'Potência do motor', 'Potência')           #2
    criadorDeGrafico.graficoDeBarrasDeLado('transmissao', 'Tipo de transmissão', 'Tipo') #3
    criadorDeGrafico.graficoPizza('cor', "Quantidade de cores", "Cores")                 #4