from tkinter import  *

ventana = Tk()
ventana.title("Principal")
ventana.geometry("500x300")

charge = Button(ventana, text = "Cargar Archivo")
charge.grid(row=0,column=0,padx=10, pady=10)
Oper = Button(ventana, text = "Operaciones")
Oper.grid(row=0,column=1,padx=10, pady=10)
Repo = Button(ventana, text = "Reportes")
Repo.grid(row=0,column=2,padx=10, pady=10)
Help = Button(ventana, text = "Ayuda")
Help.grid(row=0,column=3,padx=10, pady=10)

Panel = PanedWindow(ventana, bd=4, relief="raised")
Panel.grid(row=1,column=1,columnspan=2,ipadx=100,ipady=100,  pady=20)

text = Label(Panel, text="Panel", bg = "yellow")
text.pack()

ventana.mainloop()