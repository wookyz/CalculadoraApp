import tkinter as tk
import App.style as style

class Calculadora:
    """
        Classe para modelagem de calculadora, layout, distribuição de botões
        e funcionalidades!
            
            |          |
            1 | 2 | 3 | C
            4 | 5 | 6 | +
            7 | 8 | 9 | -
            0 | / | * | =
            
    """
    # Distribuição de todos os botões.
    _bts = ['1','2','3','C',
            '4','5','6','+',
            '7','8','9','-',
            '0','/','*','=']
    
    def __init__(self,master):
        self.style = style.Dark()
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("310x435")
        self.master.maxsize(width=310,height=435)
        self.master.minsize(width=310,height=435)
        self.master.configure(background=self.style.master_bg)
        self.__isResultado = False

        #Input area
        

        #Inicialização de metódos
        self.__criar_entrada(self.master)
        self.__criar_bts(self.master)

    # Metódo para criar a entrada
    def __criar_entrada(self,master):
        
        self._dados = tk.Entry(master,cnf=self.style.ENTRADA)
        self._dados.insert(0,0)
        self._dados.grid(row=0,column=0,columnspan=4,padx=2,pady=2)
    
    # Metódo para criar botões na grid.
    def __criar_bts(self,master):
        
        r = 1
        c = 0
        # Para elemento em _bts cria um botão e posiciona na grid.
        for bt in Calculadora._bts:
            comando = lambda x=bt: self.__calcular(x)
            self.buttons = tk.Button(master,cnf=self.style.BOTOES,text=bt,command=comando)
            self.buttons.grid(row=r,column=c,padx=1,pady=1)
            c += 1
            if c > 3:
                c = 0
                r += 1
    
    # Metódo que calcula e faz validação da Entrada.
    def __calcular(self,botao):
        last = len(self._dados.get())
        if botao == "=":
            if self._dados.get()[0] not in Calculadora._bts:
                self._dados.delete(0,last)
                self._dados.insert(0,"Operação inválida!")
            else:
                try:
                    resultado = str(eval(self._dados.get()))
                    self._dados.delete(0,last)
                    self._dados.insert(last,resultado)
                    self.__isResultado = True
                except:
                    self._dados.delete(0,last)
                    self._dados.insert(last,"ERROR")
        elif botao == "C":
            self._dados.delete(0,last)
            self._dados.insert(0,0)
        elif self._dados.get() == '0':
                self._dados.delete(0,1)
                self._dados.insert(last,botao)
        else:
            if self.__isResultado:
                self._dados.delete(0,last)
                self._dados.insert(last,botao)
                self.__isResultado = False
            else:
                self._dados.insert(last,botao)
            
    # Metódo que inicia a aplicação.
    def start(self):
        print("Calculadora Tkinter iniciada!")
        self.master.mainloop()