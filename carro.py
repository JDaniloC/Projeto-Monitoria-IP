# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Eu poderia ter usado os índices para armazenar as informações,
# mas achei melhor fazer uma procura caso mudassem a ordem dos dados,
# não utilizei uma procura mais eficiente como o regEx ou index, por que
# de todo jeito ele vai fazer um for para encontrar... Então acredito que
# percorrer os dados apenas uma vez é mais eficiente do que vários regEx,
# apesar de ser mais atraente a ideia.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Carro:
    '''
    Objeto que irá manter todas as informações coletadas
    E formatará uma lista de informações numa lista do mesmo
    '''

    def __init__(self, modelo, **kwargs):
        self.__modelo = modelo
        self.__ano = kwargs.get('ano', None)
        self.__cor = kwargs.get('cor', None)
        self.__motor = kwargs.get('motor', None)
        self.__quilometragem = kwargs.get('quilometragem', None)
        self.__marca = kwargs.get('marca', None)
        self.__transmissao = kwargs.get('transmissao', None)
        self.__etc = kwargs.get('etc', None)
    
    @staticmethod
    def formatadorDeCarros(listaDeObjetos):
        '''
        Recebe uma lista de informações dos arquivos
        Devolve uma lista de Carros a partir da lista anterior
        '''
        resultado = []
        for veiculo in listaDeObjetos:
            if veiculo != []:
                # Todas as informações realmente importantes e demais
                caracteristicas = {'modelo': " ".join(veiculo[0].split()[1:]), 
                                'ano':None, 'cor':None, 'potência do motor':None,
                                'quilometragem':None, 'marca':veiculo[0].split()[0],
                                'câmbio':None, 'km': None, 'transmissão:': None, 'motor:': None}
                etc = {}


                # Pula de dois em dois por causa da disposição dos dados
                for informacoes in range(0, len(veiculo), 2):
                    # Verifica se o tipo está nas características e adiciona o valor (em seguida)
                    if veiculo[informacoes].lower() in caracteristicas:
                        caracteristicas[veiculo[informacoes].lower()] = veiculo[informacoes + 1]
                    
                    # O caso especial onde tá tudo em uma linha
                    elif informacoes + 1 != len(veiculo) and veiculo[informacoes + 1].split()[0] == 'Conservação:':
                        especial = veiculo[informacoes + 1].split()
                        for i in range(0, len(especial), 2):
                            if especial[i].lower() in caracteristicas:
                                caracteristicas[especial[i].lower()] = especial[i + 1]
                            elif especial[i] == 'Final':
                                etc[' '.join(especial[i:i+3])] = especial[i + 3]
                            elif especial[i] != 'placa:':
                                etc[especial[i]] = especial[i + 1]
                                    
                    # Os extras
                    elif informacoes + 1 != len(veiculo):
                        if veiculo[informacoes] == caracteristicas['marca'] + ' ' + caracteristicas['modelo']:
                            etc['Estado'] = veiculo[informacoes + 1]
                        else:
                            etc[veiculo[informacoes]] = veiculo[informacoes + 1]
                
                
                # Criando o objeto Carro com as informações coletadas
                resultado.append(Carro(caracteristicas['modelo'], ano = caracteristicas['ano'],
                                        cor = caracteristicas['cor'],
                                        motor = caracteristicas['potência do motor'] if caracteristicas['motor:'] == None else caracteristicas['motor:'],
                                        quilometragem = caracteristicas['quilometragem'] if caracteristicas['km'] == None else caracteristicas['km'],
                                        marca = caracteristicas['marca'],
                                        transmissao = caracteristicas['câmbio'] if caracteristicas['câmbio'] != None else caracteristicas['transmissão:'],
                                        etc =  etc))
        return resultado

    def __str__(self):
        '''
        Método que serve para caso for usado print(Carro())
        '''
        resultado = f'''
        Modelo:        {self.modelo}
        Ano:           {self.ano}
        Cor:           {self.cor}
        Motor:         {self.motor}
        Quilometragem: {self.quilometragem}
        Marca:         {self.marca}
        Transmissão:   {self.transmissao}
        Outros:        {self.etc}'''
        return resultado
    
    # Métodos para não precisar de getters (setters, docs e etc.. também)
    modelo = property(lambda self: self.__modelo)
    ano = property(lambda self: self.__ano)
    cor = property(lambda self: self.__cor)
    motor = property(lambda self: self.__motor)
    quilometragem = property(lambda self: self.__quilometragem)
    marca = property(lambda self: self.__marca)
    transmissao = property(lambda self: self.__transmissao)
    etc = property(lambda self: self.__etc)

if __name__ == '__main__':
    print(help(Carro))