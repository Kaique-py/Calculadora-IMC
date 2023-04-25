"""
Calculadora de IMC em Python, com interface gráfica feita com Biblioteca Tkinter

Forma de utilização:
Aplicativo desenvolvido para utilização Desktop.
- Usuário irá inserir os valores de peso e altura
    Peso e altura são do tipo float, as casas devem ser separadas por ponto (.) e não por vírgula
- Clicar no botão "Calcular IMC"
- Observar o resultado do IMC do indivíduo

"""

def calculaIMC(peso, altura):
    return peso / (altura * altura)

