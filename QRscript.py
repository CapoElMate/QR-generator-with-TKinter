from email import message
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
import qrcode

class app():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry("500x1000")        
        
        self.img = PhotoImage(file = 'QR.jpg')
        self.label_img = Label(self.raiz, image = self.img)
        self.label_img.pack()

        self.texto = Text(width=100,height=1)
        self.texto.pack()

        botonGenerar = Button(text = "generar QR",command= self.generarQR)
        botonGenerar.pack()

        self.raiz.mainloop()

    def generarQR(self):
        img = qrcode.make(self.texto.get("1.0",'end-1c'))
        img.save("QR.jpg")
        print("imagen guardada: " + self.texto.get("1.0",'end-1c'))
        
        self.img = PhotoImage(file = 'QR.jpg')
        self.label_img.configure(image=self.img)




def main():
    mi_app = app()
    return 0


if __name__ == '__main__':
    main()