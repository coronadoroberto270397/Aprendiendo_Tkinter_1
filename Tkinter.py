import tkinter

ventana = tkinter.Tk()
ventana.geometry("600x600")

etiqueta =tkinter.Label(ventana, text ="Guadalajara te espera", bg="gray")
etiqueta.pack(fill =tkinter.X,)

def saludo():
    print ("Hola amigo")
boton1=tkinter.Button(ventana,text="Click aqui", command = saludo)
boton1.pack()

ct = tkinter.Entry(ventana, font = "Helvetica 50")
ct.pack()

def texto():
    txd=ct.get()
    print (txd)
    etiqueta["text"] = txd
boton2=tkinter.Button(ventana,text="Click aqui", command = texto)
boton2.pack()

boton3 = tkinter.Button(ventana, text = "info", width = 10, height = 10)
boton3.pack(side = tkinter.BOTTOM)

ventana.mainloop()