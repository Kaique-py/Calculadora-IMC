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
from tkinter import messagebox

class Interface:
    def __init__(self):
        #Janela principal
        self.janela = Tk()

        #Frames que vamos utilizar (Em pcp serão 3, um pra cada linha do app)
        self.frame_1 = Frame(self.janela)
        self.frame_2 = Frame(self.janela)
        self.frame_3 = Frame(self.janela)
        self.frame_4 = Frame(self.janela)
        
        #Agora vamos criar um Label para cada Frame (espaço) criado
        self.label_1 = Label(self.frame_1, text='Peso em quilos: (Utilize ponto ao invés de vírgula para separar casas decimais)', background='white', height=5, width=100)
        #Dentro de cada Label eu vou criar os botões ou caixas de texto que eu quiser
        self.peso = Entry(self.frame_1, width=50)
        
        self.label_2 = Label(self.frame_2, text='Altura em metros: (Utilize ponto ao invés de vírgula para separar casas decimais)', background='white', height=5, width=100)
        self.altura = Entry(self.frame_2, width=50)
        
        self.label_3 = Label(self.frame_3, text='Clique aqui para calcular seu IMC', background='white', height=5, width=100)
        #No ultimo Frame eu quero que contenha um botão para o calculo do IMC, que chamará a função.
        self.botao = Button(self.frame_3, text='Calcular IMC', command=self.calculaIMC)
        #Vou criar um botão aqui também para o usuario quitar da aplicação
        
        self.label_4 = Label(self.frame_4, height=1, width=100)
    
        self.botao_sair = Button(self.frame_4, text='Sair', command=self.janela.quit)    
        
        #Temos que posicionar esses botoes nos frames e depois na janela principal
        self.botao.pack(side='bottom')
        self.botao_sair.pack(side='bottom')

        self.botao.pack()
        self.botao_sair.pack()

        #Agora temos que posicionar os Labels nos Frames criados
        self.label_1.pack(side='top')
        self.peso.pack(side='top')
        self.label_2.pack(side='top')
        self.altura.pack(side='top')
        self.label_3.pack(side='top')
        self.label_4.pack(side='top')
     
        #Agora temos que posicionar os Frames na janela
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()
        
        #Agora temos que fazer essa janela se manter aberta o tempo todo de execução
        mainloop()
    
    def calculaIMC(self):
        try:
            peso = float(self.peso.get())
            altura = float(self.altura.get())
            IMC = peso / (altura * altura)
            messagebox.showinfo('CÁLCULO IMC', 'Seu IMC foi de {:.2f}'. format(IMC))
        except:
            messagebox.showinfo('Erro', 'Entrada inválida. Lembre de utilizar ponto para separar casas decimais.')

resultado_janela = Interface()
