# Projeto-Monitoria-IP

```shell
>> Projeto para a avaliação de candidatos à monitoria da disciplina IF-669
```

<p align="center">
    <image src="./static/dual-grafico.png">
</p>

Objetivo: Ler [arquivos](https://github.com/rodrigoap2/projetoMonitoriaIp) (bem desorganizados) de modo a produzir gráficos

> Download, dependências e execução

1 - Faça o download ou clone do repositório: [aqui](https://github.com/JDaniloC/Projeto-Monitoria-IP.git)

2 - Tenha o python 3.6 acima, com a biblioteca pandas e matlibplot e rode o arquivo [main.py](./src/main.py)

3 - De modo alternativo, pode fazê-lo com a interface gráfica rodando com as mesmas dependências o script [programa.py](./src/programa.py)


<p align = 'center'>
    <image width = 100% src="./static/ui.png"/> 
</p>


>>> Foi permitido ser pythonic
>>>
>>> Pediu pra usar orientação a objeto, então exagerei

<img align="right" width='55%' src="./static/grafico02.png">

## Main
Onde o programa realmente vai rodar, printando as formas dos objetos e plotando os gráficos.

## Objeto leitor
Faz a leitura de todos os arquivos em encoding UTF-8 (por causa do windows)


## Objeto carro
Condiciona todas as informações em objetos, filtrando os resultados do objeto anterior

<image align="left" width='60%' src="./static/grafico01.png"/> 

## Objeto grafico
Recebe os dados e transforma em um gráfico

### Programa
Uma interface gráfica para o script, onde é possível escolher que tipo de gráfico irá ser exibido

### Filtragem
<image src="./static/formato.png"/> 