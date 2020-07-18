import tkinter as tk
import App.style as style
from functools import partial
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
    
    # Váriavel de instância que confirma se o resultado está no input.
    _result_in_input = False

    def __init__(self,master):
        self.style = style.Dark()
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("310x445")
        self.master.maxsize(width=310,height=445)
        self.master.minsize(width=310,height=445)
        self.master.configure(background=self.style.master_bg)

        #Inicialização de metódos
        self.__criar_entrada(self.master)
        self.__criar_bts(self.master)
        
    
    def __criar_entrada(self,master):
        # Metódo para criar a entrada
        self.__data = tk.Entry(master,cnf=self.style.ENTRADA)
        self.__data.insert(0,0)
        self.__data.grid(row=0,column=0,columnspan=4,padx=2,pady=2)
    
   
    def __criar_bts(self,master):
         # Metódo para criar botões e posicionar na grid.
        r = 1
        c = 0
        for bt in Calculadora._bts:
            if bt in '0123456789':
                comando = lambda x=bt: self.__set_values_input(x)
            elif bt in '+-/*':
                comando = lambda x=bt: self.__set_operator_input(x)
            elif bt in '=C':
                comando = lambda x=bt: self.__set_features_input(x)
            self.buttons = tk.Button(master,cnf=self.style.BOTOES,text=bt, command=comando)
            self.buttons.grid(row=r,column=c,padx=1,pady=1)
            c += 1
            if c > 3:
                c = 0
                r += 1

    def __set_values_input(self,value):
        # Metódo que atribui o valor no input.
        if self.__data.get() == "ERRO":
            self.__data.delete(0,len(self.__data.get()))
        
        if self.__data.get() == '0' or Calculadora._result_in_input:
            self.__clear_input(message=value)
            Calculadora._result_in_input = False

        elif self.__length_max(self.__data.get()):
            self.__data.insert(len(self.__data.get()), value)
    
    def __set_operator_input(self,operator):
        # Metódo que insere o operador no input.
        if self.__data.get() == "ERRO":
            return
        
        if self.__data.get() == '0':
            return

        if operator in '+-/*':
            if self.__data.get()[-1] not in '+-*/' and self.__length_max(self.__data.get()):
                self.__data.insert(len(self.__data.get()), operator)
                Calculadora._result_in_input = False
    
    def __set_features_input(self,button):
        # Metódo responsável por adicionar as funcionalidades dos botões de igualdade e Clear.
        if button == 'C':
            self.__clear_input()

        elif button == '=':
            self.__set_result(self.__data.get())
            
    def __set_result(self,equation='0'):
        # Atribui o resultado da equação.
        if self.__data.get() == 'ERRO':
            return

        try:
            result = str(eval(equation))
            self.__clear_input(message=result)
            Calculadora._result_in_input = True
        except:
            self.__clear_input(message="ERRO")
    
    def __length_max(self, data_input):
        # Metódo que verifica se a entrada dos dados é maior que a quantidade máxima de caracteres.
        if len(data_input) >= 15:
            return False
        return True

    def __clear_input(self,message='0'):
        # Metódo que apaga o input e substitui por uma string.
        self.__data.delete(0,len(self.__data.get()))
        self.__data.insert(0,message)
    
    def __set_button_input(self,button):
        # Método que verifica qual é o botão.
        if button in '+-*/':
            self.__set_operator_input(button)
        elif button in '0123456789':
            self.__set_values_input(button)

    def start(self):
        # Metódo que inicia a aplicação.
        print("Calculadora Tkinter iniciada!")
        self.master.mainloop()