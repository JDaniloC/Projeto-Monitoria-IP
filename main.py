from leitor import Leitor
from carro import Carro

for i in Carro.formatadorDeCarros(Leitor.lerArquivos('./database')): print(i)