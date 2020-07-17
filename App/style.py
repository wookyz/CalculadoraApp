import tkinter as tk

class Dark():
    
    def __init__(self):
        self.master_bg = "#2d2d2d"
        self.frame_bg = "#2d2d2d"

        self.ENTRADA = {
            'bg': "#2d2d2d",
            'highlightthickness': 0,
            'borderwidth': 0,
            'fg': 'white',
            'font': 'Arial 25 bold',
            'justify': 'right',
            'width': 15
        }

        self.BOTOES = {
            'bg': "#464646",
            'highlightthickness': 0,
            'borderwidth': 0,
            'fg': 'white',
            'font': 'Arial 14 bold',
            'width': 6,
            'height': 4,
            'activebackground': "#bdbdbd"
        }