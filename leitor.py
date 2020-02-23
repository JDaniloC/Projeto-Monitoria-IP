import os

# Já que é pra fazer tudo com orientação a objetos

class Leitor:
    '''
    Objeto leitor dos arquivos no estilo do projeto
    Use o método lerArquivos, devolvendo uma lista das informações de cada arquivo onde:
        - Será retirado todos os '\n'
    '''
    @staticmethod
    def lerArquivos(caminhoRelativoDaPasta):
        '''
        1 - Tenta ver todos os arquivos de uma pasta
        2 - Cria uma lista de listas se utilizando o método abrirArquivo com exceção do 'README.md'
        3 - Caso der errado, devolve uma lista vazia
        '''
        try:
            # Deixou ser um pouco pythonic
            listaDeInformacoes = [ 
                Leitor.abrirArquivo(caminhoRelativoDaPasta + '/' + x) for x in os.listdir(caminhoRelativoDaPasta) if x != 'README.md'
            ]
        except:
            listaDeInformacoes = []
        return listaDeInformacoes
    
    @staticmethod
    def abrirArquivo(archivePath):
        '''
        1 - Tenta abre o arquivo
        2 - Lê todas as linhas
        3 - Cria uma lista tirando o '/n' de cada uma
        4 - Se der errado, devolve uma lista vazia
        '''
        try:
            with open(archivePath, 'r') as arquivo:
                informacoes = arquivo.readlines()
        except:
            informacoes = []
        return list(map(lambda x: x.strip(), informacoes))

if __name__ == '__main__':
    print(help(Leitor))