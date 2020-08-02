import tkinter

ventana = tkinter.Tk()
ventana.geometry("600x600")
etiqueta =tkinter.Label(ventana, text ="Guadalajara te espera", bg="blue")
etiqueta.pack(fill =tkinter.Y,expand=True)

ventana.mainloop()