from tkinter import *

window = Tk()


class Aplication:

    def __init__(self):
        self.window = window
        self.firstWindow()
        self.frameFirstWindow()
        self.buttonFirstWindow()
        self.labelFirstWindow()
        self.background()
        window.mainloop()

    def firstWindow(self):
        self.window.title("Ebony SYS")
        self.window.configure(background="#3a3b3c")
        self.window.geometry("700x700")
        self.window.resizable(False, False)
        # self.window.resizable(True, True)
        # self.window.maxsize(width=700, height=700)
        # self.window.minsize(width=450, height=450)

    def frameFirstWindow(self):
        self.frame1 = Frame(self.window, background='#3a3b3c')
        self.frame1.place(relx=0, rely=0, relwidth=1, relheight=0.06)

        self.frame2 = Frame(self.window, background='#3a3b3c')
        self.frame2.place(relx=0.01, rely=0.06, relwidth=0.98, relheight=0.90)

        self.frame3 = Frame(self.window, background='#3a3b3c')
        self.frame3.place(relx=0, rely=0.95, relwidth=1, relheight=0.07)

    def buttonFirstWindow(self):
        self.btSnake = Button(self.frame2, text='Snake', background='#3a3b3c', font='Helvética 30',
                              foreground='white')
        self.btSnake.place(relx=0.03, rely=0.03, relwidth=0.45, relheight=0.45)

        self.btCampoMinado = Button(self.frame2, text='Campo\nMinado', background='#3a3b3c', font='Helvética 30',
                                    foreground='white')
        self.btCampoMinado.place(relx=0.52, rely=0.03, relwidth=0.45, relheight=0.45)

        self.btCorrida = Button(self.frame2, text='Corrida', background='#3a3b3c', font='Helvética 30',
                                foreground='white')
        self.btCorrida.place(relx=0.03, rely=0.52, relwidth=0.45, relheight=0.45)

        self.btForca = Button(self.frame2, text='Forca', background='#3a3b3c', font='Helvética 30',
                              foreground='white')
        self.btForca.place(relx=0.52, rely=0.52, relwidth=0.45, relheight=0.45)

    def labelFirstWindow(self):
        self.lbLogo = Label(self.frame1, text='ebony', font='abnes 15', background='#3a3b3c', foreground='white')
        self.lbLogo.place(relx=0.01, rely=0.2)
        self.lbLogo1 = Label(self.frame1, text='sys', font='Debum 28', background='#3a3b3c', foreground='#39ff14')
        self.lbLogo1.place(relx=0.20, rely=0.00)
        self.lbRodape = Label(self.frame3, text='@ebony.programador', font='ubuntu 12', background='#3a3b3c',
                              foreground='gray')
        self.lbRodape.place(relx=0.76, rely=0.1)

    def background(self):
        ...


Aplication()
