from leitor import Leitor
from carro import Carro
from grafico import Grafico
import pandas as pd

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Isso daqui é só pra zuar como se fosse Java, e dar uma hiperbolizada
# quando pediu pra usar POO
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Main:
    @staticmethod
    def publicStaticVoidMain():
        veiculos = Carro.formatadorDeCarros(Leitor.lerArquivos('./database'))
        
        print("Todos os veículos")
        for i in veiculos: print(i, '\n')

        excluir = ['_Carro__modelo', '_Carro__etc']
        dataframe = {key[8:]:[] for (key, value) in veiculos[0].__dict__.items() if key not in excluir}
            
        for carro in veiculos:
            for chave, valor in carro.__dict__.items():
                if chave not in excluir:
                    dataframe[chave[8:]].append(valor)
        dataframe['quilometragem'] = [int(x) for x in dataframe['quilometragem']]
        resultado = pd.DataFrame(dataframe)
        
        print('- - ' * 20 + "\n" + "Pandas.DataFrame")
        print(resultado)
        resultado.plot(kind='bar', x = 'marca', y = 'quilometragem', figsize = (8, 7))       

        criadorDeGrafico = Grafico(dataframe)
        criadorDeGrafico.graficoDeBarras('motor', 'Potência do motor', 'Potência')           
        criadorDeGrafico.graficoDeBarrasDeLado('transmissao', 'Tipo de transmissão', 'Tipo') 
        criadorDeGrafico.graficoPizza('cor', "Quantidade de cores", "Cores")                 

if __name__ == '__main__':
    Main.publicStaticVoidMain()