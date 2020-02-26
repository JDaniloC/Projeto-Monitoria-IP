import matplotlib.pyplot as plt

class Grafico:
    '''
    Objeto que irá receber os dados e montar um gráfico a partir deles
    '''
    def __init__(self, dicionario):
        self.dicionario = dicionario

    def graficoDeBarras(self, tipo, titulo = '', nomeX = '', nomeY = "Quantidade"):
        '''
        Recebe o tipo de dado (que contenha no dicionário oferecido)
        O título do gráfico
        Nome do eixo X
        Nome do eixo Y (Quantidade por padrão)
        E plota um gráfico de barras verticais
        '''
        if titulo == '':
            titulo = tipo.capitalize()
        labels, quantidade = self.contaDados(tipo)

        figura, grafico = plt.subplots(figsize = (8, 7))
        grafico.set_title(titulo)
        grafico.bar(labels, quantidade)
        grafico.set_xlabel(nomeX)
        grafico.set_ylabel(nomeY)
        grafico.set_yticklabels(quantidade)
        for indice, valor in enumerate(quantidade):
            grafico.text(indice, valor + 0.1, str(valor))
        plt.show()

    def graficoDeBarrasDeLado(self, tipo, titulo = '', nomeY = '', nomeX = "Quantidade"):
        '''
        Recebe o tipo de dado (que contenha no dicionário oferecido)
        O título do gráfico
        Nome do eixo X (Quantidade por padrão)
        Nome do eixo Y 
        E plota um gráfico de barras horizontais
        '''
        if titulo == '':
            titulo = tipo.capitalize()
        labels, quantidade = self.contaDados(tipo)

        plt.barh(labels, quantidade)
        plt.ylabel(nomeY)
        plt.xlabel(nomeX)
        plt.title(titulo)
        for indice, valor in enumerate(quantidade):
            plt.text(valor, indice, str(valor))
        plt.show()

    def graficoPizza(self, tipo, titulo = '', tituloDaLegenda = ''):
        '''
        Recebe o tipo de dado (que contenha no dicionário oferecido)
        O título do gráfico
        O título da legenda
        E plota um gráfico de pizza
        '''
        if titulo == '':
            titulo = tipo.capitalize()
        labels, quantidade = self.contaDados(tipo)

        figura, grafico = plt.subplots(figsize = (7, 7))
        grafico.set_title(titulo)
        wedges, texts, autotexts = grafico.pie(quantidade, labels = labels, shadow=True,
        autopct = lambda valor: "{:.1f}%\n({:.0f})".format(valor, valor*sum(quantidade)/100))
        grafico.legend(wedges, labels,
                title = tituloDaLegenda,
                loc = "center left",
                bbox_to_anchor = (0.8, -0.5, 0.5, 1))
        plt.show()

    def contaDados(self, dado):
        '''
        Recebe um tipo de dado no dicionário
        E conta quantos elementos existem daquele dado
        Exemplo:
            O tipo de dado são as cores
            Ele vai contar quantos vermelhos, azuis, amarelos... existem
        '''
        labels, quantidade = [], []
        for x in self.dicionario[dado]:
            if x not in labels:
                labels.append(x)
                quantidade.append(0)
            quantidade[labels.index(x)] += 1
        return labels, quantidade 

if __name__ == '__main__':
    print(help(Grafico))