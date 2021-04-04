import webbrowser
from tkinter import  *
from tkinter import filedialog

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
Panel.grid(row=1,column=1,columnspan=2,  pady=20)

text = Label(Panel, text="Panel", bg = "yellow", pady=20)
text.pack()
cuadro = Label(Panel, text="Cuadro", bg = "green", height=10, width=15,padx=20)
cuadro.pack(side=LEFT)
res = Label(Panel, text="resultado", bg = "red", height=10, width=15, padx=20)
res.pack(side=RIGHT)

ventana.mainloop()

root = Tk()
def fileOpen():
    root.fileName = filedialog.askopenfilename(filetypes=(("Arch texto", ".txt"), ("Todo", ".")))
    file = root.fileName
    return file

Button(root, text = "SELECCIONE ENTRADA",command=fileOpen).pack()

def reportweb():
    GG = open("menu.html", "w")

    fase = """<!DOCTYPE html>
              <html lang="en">
                <head>
                  <title>RESTAURANTE LFP</title>
                  <meta charset="utf-8">
                  <meta name="viewport" content="width=device-width, initial-scale=1">
                  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
                  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
                  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
                  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
                </head>
                <body class="bg-primary">
                <h1 align="center" class="bg-info">RESTAURANTE</h1>
                <h1 align="center" class="bg-info">UWU</h1>
                 <div  class="container shadow p-3 mb-5">
                  <h2 class="text-light">BEBIDAS</h2>
                   <h3>BEBIDA 1 Q11</h3>
                   <p>descripcion de bebida</p>
                  <h2 class="text-light">COMIDAS</h2>
                   <h3>COMIDA 1 Q21</h3>
                   <p>descripcion de comida</p>
                  <h2 class="text-light">POSTRES</h2>
                   <h3>POSTRE 1 Q18</h3>
                   <p>descripcion de postre</p>
                 </div>
                </body>
              </html>"""
    GG.write(fase)
    GG.write("</tbody>")
    GG.write("</table>")
    GG.write("</body>")
    GG.write("</html>")
    GG.close()
    webbrowser.open_new_tab("menu.html")
def datos_est():
    print("GERARDO JOSE CIFUENTES LUNA")
    print("201900952")
    print('Introduccion a la Programacion y Computacion 2 seccion "E" ')
    print("Ingenieria en Ciencias y Sistemas")
    print("5to Semestre")

def docu():
    webbrowser.open_new(r"C:\Users\Cifuentes\Desktop\IPC2_Proyecto2_201900952\docu.pdf")