import webbrowser
from tkinter import  *
from tkinter import filedialog
from datetime import date, time, datetime
ventana = Tk()
ventana.title("Principal")
ventana.geometry("500x300")

def fileOpen():
    ventana.fileName = filedialog.askopenfilename(filetypes=(("Arch texto", ".txt"), ("Todo", ".")))
    file = ventana.fileName
    return file

def datos_est():
    print("GERARDO JOSE CIFUENTES LUNA")
    print("201900952")
    print('Introduccion a la Programacion y Computacion 2 seccion "E" ')
    print("Ingenieria en Ciencias y Sistemas")
    print("5to Semestre")

def docu():
    webbrowser.open_new(r"Docu\EnsayoProyecto2_201900952.pdf")
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
                <h1 align="center" class="bg-info">Reporte de Logs</h1>
                <hr>
                 <div  class="container shadow p-3 mb-5">
                  <table class="table">
                <thead class="thead-dark">
                  <tr>
                    <th>Nombre</th>
                    <th>Espacios Llenos</th>
                    <th>Espacios vacios</th>
                    <th>Fecha-Hora</th>
                  </tr>
                </thead> 
                <tbody>
                  <tr> <td>Cargar </td>
                   <td>n/a </td>
                   <td>n/a </td>
                  <td>"""+str(datetime.now())+"""</td></tr>
                </tbody>
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


##menu##
barra=Menu(ventana)
Charge=Menu(barra)
Oper=Menu(barra)
Reprt=Menu(barra)
Help=Menu(barra)
##Opciones##
Charge.add_command(label="Seleccione Archivo", command=fileOpen)

Oper.add_command(label="Rotacion Horizontal")
Oper.add_command(label="Rotacion Vertical")
Oper.add_command(label="Transpuesta")
Oper.add_command(label="Limpiar Zona")
Oper.add_command(label="Agregar linea Horizontal")
Oper.add_command(label="Agregar linea Vertical")
Oper.add_command(label="Agregar Rectangulo")
Oper.add_command(label="Agregar Triangulo rectangulo")
Oper.add_separator()
Oper.add_command(label="UNION")
Oper.add_command(label="INTERSECCION")
Oper.add_command(label="DIFERENCIA")
Oper.add_command(label="DIFERENCIA SIMETRICA")

Reprt.add_command(label="Abrir Reporte", command=reportweb)

Help.add_command(label="Info del Estudiante",command=datos_est)
Help.add_command(label="Documentacion",command=docu)
##Agregado al menu##
barra.add_cascade(label="Cargar Archivo", menu=Charge)
barra.add_cascade(label="Operaciones", menu=Oper)
barra.add_cascade(label="Reportes", menu=Reprt)
barra.add_cascade(label="Ayuda", menu=Help)
ventana.config(menu=barra)
##BOTONES##



Panel = PanedWindow(ventana, bd=4, relief="raised")
Panel.grid(row=1,column=1,columnspan=2,  pady=20)
stock=PhotoImage(file="Quemado.png")
text = Label(Panel, text="Panel", bg = "blue", pady=10)
text.pack()
cuadro = Label(Panel, text="Cuadro", bg = "green", padx=20,image=stock)
cuadro.pack(side=LEFT)
res = Label(Panel, text="resultado", bg = "black", height=10, width=15, padx=20)
res.pack(side=RIGHT)




ventana.mainloop()





