import tkinter as tk
from App.calculadora import Calculadora

if __name__ == "__main__":
    master = tk.Tk()
    main = Calculadora(master)
    main.start()
    