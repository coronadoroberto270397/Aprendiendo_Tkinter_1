import tkinter

ventana = tkinter.Tk()
ventana.geometry("600x600")

etiqueta =tkinter.Label(ventana, text ="Guadalajara te espera", bg="gray")
etiqueta.pack(fill =tkinter.X,)


boton1=tkinter.Button(ventana,text="Click aqui")
boton1.pack()

ventana.mainloop()