import tkinter as tk

class Calculadora:
    """
        Classe para modelagem de calculadora, layout, distribuição de botões
        e funcionalidades!

        1 | 2 | 3 | C
        4 | 5 | 6 | +
        7 | 8 | 9 | -
        / | * | ^ | =
        |          |
    """
    _bts = ['1','2','3','C','4','5','6','+','7','8','9','-','/','*','^','=']
    
    def __init__(self,master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("300x450")
        self.master.maxsize(width=300,height=450)
        self.master.minsize(width=300,height=450)
        self.master.configure(background="#696969")
        self._dados = tk.Entry(master,width=50,justify="left")
        self._dados.grid(row=5,column=0,columnspan=4)
        
        
        """
        Inicialização de metódos
        """
    
        self._criar_bts(self.master)

    def _criar_bts(self,master):
        r = 0
        c = 0
        for bt in Calculadora._bts:
            comando = lambda x=bt: self._calcular(x)
            self.buttons = tk.Button(master,width=10,height=5,text=bt,bg="#C0C0C0",bd=0,activebackground="#DCDCDC",command=comando)
            self.buttons.grid(row=r,column=c)
            c += 1
            if c > 3:
                c = 0
                r += 1
            
    def _calcular(self,botao):
        last = len(self._dados.get())
        
        if botao == "=":
            if self._dados.get()[0] not in Calculadora._bts:
                self._dados.delete(0,last)
                self._dados.insert(-1,"Operação inválida!")
            else:
                try:
                    resultado = str(eval(self._dados.get()))
                    self._dados.delete(0,last)
                    self._dados.insert(last,resultado)

                except:
                    self._dados.delete(0,last)
                    self._dados.insert(last,"ERROR")
                
                
        elif botao == "C":
            self._dados.delete(0)
        else:
            self._dados.insert(last,botao)
            

    def start(self):
        print("Calculadora Tkinter iniciada!")
        self.master.mainloop()