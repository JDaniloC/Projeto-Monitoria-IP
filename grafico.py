import matplotlib.pyplot as plt

class Grafico:
    def __init__(self, dicionario):
        self.dicionario = dicionario

    def graficoDeBarras(self, tipo, titulo, nomeX, nomeY = "Quantidade"):
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

    def graficoDeBarrasDeLado(self, tipo, titulo, nomeY, nomeX = "Quantidade"):
        labels, quantidade = self.contaDados(tipo)

        plt.barh(labels, quantidade)
        plt.ylabel(nomeY)
        plt.xlabel(nomeX)
        plt.title(titulo)
        for indice, valor in enumerate(quantidade):
            plt.text(valor, indice, str(valor))
        plt.show()

    def graficoPizza(self, tipo, titulo, tituloDaLegenda):
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
        labels, quantidade = [], []
        for x in self.dicionario[dado]:
            if x not in labels:
                labels.append(x)
                quantidade.append(0)
            quantidade[labels.index(x)] += 1
        return labels, quantidade 

if __name__ == '__main__':
    print(help(Grafico))