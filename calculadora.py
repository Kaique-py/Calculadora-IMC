"""
Calculadora de IMC em Python, com interface gráfica feita com Biblioteca Tkinter

Forma de utilização:
Aplicativo desenvolvido para utilização Desktop.
- Usuário irá inserir os valores de peso e altura
    Peso e altura são do tipo float, as casas devem ser separadas por ponto (.) e não por vírgula
- Clicar no botão "Calcular IMC"
- Observar o resultado do IMC do indivíduo

"""
from tkinter import *
janela = Tk()
peso_var = float()
altura_var = float()

def calculaIMC():
    peso = peso_var.get()
    altura = altura_var.get()
    return peso / (altura * altura)


janela.title("Calculadora de IMC")
orientacao_uso = Label(janela, text="Insira os valores do Peso e Altura e, em seguida, clique em Calcular IMC. \n(Utilize ponto ao invés de vírgula para separa casas decimais)")
orientacao_uso.grid(column=1, row=0)
botao = Button(janela, text="Calcular IMC", command=calculaIMC)
botao.grid(column=1, row=2)

janela.mainloop()
