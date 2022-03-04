from tkinter import *
from datetime import date as dt
from datetime import datetime, timedelta
from tkinter import ttk
from tkcalendar import DateEntry
import sqlite3
from tkinter import messagebox


# ------------- Variables -----------------------

categorias = {
    'Alimentos': ('Supermercado', 'Carniceria',
                  'Almuerzo/Cena', 'Desayuno', 'Panaderia', 'Pastas', 'Fiambreria', 'Helado/dulces', 'Pescaderia', 'Verduleria', 'Kiosco'),
    'Casa': ('Seguro', 'Arreglos MO', 'Materiales', 'Electro', 'Limpieza'),
    'Auto': ('Seguro', 'Nafta', 'Service/Arreglos', 'Peajes', 'Lavadero', 'Patente'),
    'Impuestos': ('Rentas ABL', 'Aysa', 'Edesur', 'Metrogas'),
    'Servicios': ('Cablevisión', 'Netflix', 'Otro streaming',
                  'Movistar', 'Rappi/Pedidoya', 'Cuota club', 'Alertas Mercado'),
    'Viaticos': ('SUBE', 'Taxi'),
    'Entretenimiento': ('Restaurante', 'Juegos',
                        'Cine/Teatro', 'Reuniones', 'Deportes'),
    'Cuidado personal': ('Medicamentos', 'Gimnasio', 'Obra Social', 'Peluqueria'),
    'Manutención': ('Manutención'),
    'Mascota': ('Comida', 'Piedritas', 'Jueguitos', 'Veterinaria', 'Medicamentos'),
    'Educación': ('Libreria', 'Libros', 'Cursos', 'Ingles'),
    'Indumentaria': ('Indumentaria Felipe',
                     'Indumentaria Ayelen', 'Indumentaria Leo'),
    'Regalos': ('Regalos'),
    'Vacaciones': ('Alquiler', 'Compra millas', 'Suscripciones', 'Aereos')
}

# ------------- Interface -----------------------

raiz = Tk()
raiz.title("Ingreso de gastos")
raiz.resizable(width=True, height=True)
# raiz.iconbitmap('icono.ico')

miframe1 = Frame(raiz)
miframe1.config()
miframe1.pack()

miframe2 = Frame(raiz)
miframe2.config()
miframe2.pack()

# ------------- Funciones -----------------------


def conexionBBDD():

    try:

        miConexion = sqlite3.connect("GASTOS")

        miCursor = miConexion.cursor()

        miCursor.execute('''CREATE TABLE DATOS_GASTOS (
	                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    FECHA TEXT,
                    USUARIO VARCHAR(10),
                    DESTINO VARCHAR(10),
                    CATEGORIA VARCHAR(30),
                    SUBCATEGORIA VARCHAR(30),
                    MEDIO_PAGO VARCHAR(30),
                    MONTO FLOAT
                    ) ''')

        messagebox.showinfo("BBDD", "BBDD creada con éxito")

    except:

        miConexion = sqlite3.connect("GASTOS")
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")


def salir_app():

    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

    if valor == 'yes':
        raiz.destroy()


def on_combobox_select(event):
    subcategoriaentry.set("")
    subcategoriaentry.config(values=categorias[categoriaentry.get()])


def limpiar_campos():
    usuario.set("")
    destino.set("")
    fecha.set("")
    categoria.set("")
    subcategoria.set("")
    subcategoriaentry.config(values="")
    medio.set("")
    monto.set("")
    cuotaslabel.config(state='disable')
    cuotasentry.config(state='disable')
    cuotas.set("")


def crear():

    activado = leer_var.get()
    if activado:
        actualizar()
    else:
        if usuario.get() == "" or destino.get() == "" or fecha.get() == "" or categoria.get() == "" or subcategoria.get() == "" or medio.get() == "" or monto.get() <= 0:
            messagebox.showerror("Registro", "Faltan datos en el registro")

        else:
            fecha_carga = datetime.strptime(fecha.get(), "%m/%d/%y")

            miConexion = sqlite3.connect("GASTOS")
            miCursor = miConexion.cursor()

            if medio.get() == "Credito":

                for i in range(cuotas.get()):

                    fecha_carga = fecha_carga + timedelta(days=(30.5))

                    miCursor.execute(F'''INSERT INTO DATOS_GASTOS VALUES (
                        NULL,
                        "{fecha_carga.strftime("%Y-%m-%d")}",
                        "{usuario.get()}",
                        "{destino.get()}",
                        "{categoria.get()}",
                        "{subcategoria.get()}",
                        "{medio.get()}",
                        {monto.get()}
                        ) ''')
            else:

                miCursor.execute(F'''INSERT INTO DATOS_GASTOS VALUES (
                        NULL,
                        "{fecha_carga.strftime("%Y-%m-%d")}",
                        "{usuario.get()}",
                        "{destino.get()}",
                        "{categoria.get()}",
                        "{subcategoria.get()}",
                        "{medio.get()}",
                        {monto.get()}
                        ) ''')

            miConexion.commit()
            messagebox.showinfo("BBDD", "Registro insertado con exito")
            limpiar_campos()


def activar_leer():
    activado = leer_var.get()
    if activado:
        identry.config(state='normal')
    else:
        identry.config(state='disabled')
        id.set(0)
        limpiar_campos()


def leer(event):
    ID = id.get()
    if ID == 0:
        limpiar_campos()
    else:
        miConexion = sqlite3.connect("GASTOS")

        miCursor = miConexion.cursor()

        miCursor.execute(F"SELECT * FROM DATOS_GASTOS WHERE ID = {ID}")

        datos = miCursor.fetchall()

        if len(datos):

            for dato in datos:
                fecha.set(datetime.strptime(
                    dato[1], "%Y-%m-%d").strftime("%m/%d/%y"))
                usuario.set(dato[2])
                destino.set(dato[3])
                categoria.set(dato[4])
                subcategoria.set(dato[5])
                medio.set(dato[6])
                monto.set(dato[7])
        else:
            messagebox.showerror("Error", "No existe registro")
            limpiar_campos()


def actualizar():
    if usuario.get() == "" or destino.get() == "" or fecha.get() == "" or categoria.get() == "" or subcategoria.get() == "" or medio.get() == "" or monto.get() <= 0:
        messagebox.showerror("Registro", "Faltan datos en el registro")

    else:
        fecha_carga = datetime.strptime(fecha.get(), "%m/%d/%y")

        miConexion = sqlite3.connect("GASTOS")
        miCursor = miConexion.cursor()

        miCursor.execute(F'''UPDATE DATOS_GASTOS SET 
                    FECHA = "{fecha_carga.strftime("%Y-%m-%d")}",
                    USUARIO = "{usuario.get()}",
                    DESTINO = "{destino.get()}",
                    CATEGORIA = "{categoria.get()}",
                    SUBCATEGORIA = "{subcategoria.get()}",
                    MEDIO_PAGO = "{medio.get()}",
                    MONTO = {monto.get()}
                    WHERE ID = "{id.get()}"
                    ''')

        miConexion.commit()
        messagebox.showinfo("BBDD", "Registro actualizado con exito")
        limpiar_campos()


def eliminar():
    activado = leer_var.get()
    if activado and id.get() != 0:
        miConexion = sqlite3.connect("GASTOS")
        miCursor = miConexion.cursor()

        miCursor.execute(F'DELETE FROM DATOS_GASTOS WHERE ID = {id.get()}')

        miConexion.commit()
        messagebox.showinfo("BBDD", "Registro eliminado con exito")
        limpiar_campos()

    else:
        messagebox.showerror(
            "Error", "Debe seleccionar un registro para eliminarlo")


def cuotas():
    if medio.get() == "Credito":
        cuotaslabel.config(state='active')
        cuotasentry.config(state='active')

    else:
        cuotaslabel.config(state='disable')
        cuotasentry.config(state='disable')
        cuotas.set("")

    # ------------- Barra Menu -----------------------
barramenu = Menu(raiz)
raiz.config(menu=barramenu)

bbddmenu = Menu(barramenu, tearoff=0)
bbddmenu.add_command(label='Conectar', command=conexionBBDD)
bbddmenu.add_command(label='Salir', command=salir_app)

borrarmenu = Menu(barramenu, tearoff=0)
borrarmenu.add_command(label='Borrar campos', command=limpiar_campos)

crudmenu = Menu(barramenu, tearoff=0)
crudmenu.add_command(label='Crear Registro', command=crear)
crudmenu.add_command(label='Actualizar Registro', command=actualizar)
crudmenu.add_command(label='Eliminar Registro', command=eliminar)

ayudamenu = Menu(barramenu, tearoff=0)
ayudamenu.add_command(label='Licencia')
ayudamenu.add_command(label='Acerca de ..')

barramenu.add_cascade(label='BBDD', menu=bbddmenu)
barramenu.add_cascade(label='Borrar', menu=borrarmenu)
barramenu.add_cascade(label='CRUD', menu=crudmenu)
barramenu.add_cascade(label='Ayuda', menu=ayudamenu)

# ------------- Labels -----------------------

idlabel = Label(miframe1, text='ID')
idlabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)

pagolabel = Label(miframe1, text='¿Quien pago?')
pagolabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)

fechalabel = Label(miframe1, text='Fecha:')
fechalabel.grid(row=2, column=0, sticky='e', padx=10, pady=10)

destinolabel = Label(miframe1, text='¿Para quién?')
destinolabel.grid(row=3, column=0, sticky='e', padx=10, pady=10)

categorialabel = Label(miframe1, text='Categoria:')
categorialabel.grid(row=4, column=0, sticky='e', padx=10, pady=10)

subcategorialabel = Label(miframe1, text='Subcategoria:')
subcategorialabel.grid(row=5, column=0, sticky='e', padx=10, pady=10)

mediolabel = Label(miframe1, text='Medio de pago:')
mediolabel.grid(row=6, column=0, sticky='e', padx=10, pady=10)

cuotaslabel = Label(miframe1, text='Cuotas:', state='disable')
cuotaslabel.grid(row=7, column=0, sticky='e', padx=10, pady=10)

costolabel = Label(miframe1, text='Costo:')
costolabel.grid(row=8, column=0, sticky='e', padx=10, pady=10)

# ------------- Dataentry -----------------------

id = IntVar()
identry = Entry(miframe1, textvariable=id,
                state='disabled')
identry.grid(row=0, column=1, padx=10, pady=10)
identry.config(width=5)
identry.bind('<Return>', leer)

leer_var = IntVar()
leerentry = Checkbutton(miframe1, text='Leer registro', onvalue=1, offvalue=0,
                        variable=leer_var, indicatoron=False, command=activar_leer)
leerentry.grid(row=0, column=2)


usuario = StringVar()
pagoentry1 = Radiobutton(miframe1, text='Ayelen',
                         value='Ayelen', indicatoron=False, variable=usuario, width=10)
pagoentry2 = Radiobutton(miframe1, text='Leonardo',
                         value='Leonardo', indicatoron=False, variable=usuario, width=10)

pagoentry1.grid(row=1, column=1)
pagoentry2.grid(row=1, column=2)

fecha = StringVar()
fechaentry = DateEntry(miframe1, width=20, textvariable=fecha)
fechaentry.grid(row=2, column=1, columnspan=2)

destino = StringVar()
destinoentry1 = Radiobutton(miframe1, text='Comun',
                            value='Comun', indicatoron=False, variable=destino, width=10)
destinoentry2 = Radiobutton(
    miframe1, text='Ayelen', value='Ayelen', indicatoron=False, variable=destino, width=10)
destinoentry3 = Radiobutton(
    miframe1, text='Leonardo', value='Leonardo', indicatoron=False, variable=destino, width=10)

destinoentry1.grid(row=3, column=1, padx=10)
destinoentry2.grid(row=3, column=2, padx=10)
destinoentry3.grid(row=3, column=3, padx=10)

categoria = StringVar()
categoriaentry = ttk.Combobox(miframe1, values=list(
    categorias.keys()), textvariable=categoria)
categoriaentry.grid(row=4, column=1, columnspan=2)
categoriaentry.bind("<<ComboboxSelected>>", on_combobox_select)

subcategoria = StringVar()
subcategoriaentry = ttk.Combobox(miframe1, textvariable=subcategoria)
subcategoriaentry.grid(row=5, column=1, columnspan=2)

medio = StringVar()
medioentry1 = Radiobutton(miframe1, text='Efectivo',
                          value='Efectivo', indicatoron=False, variable=medio, width=10, command=cuotas)
medioentry2 = Radiobutton(
    miframe1, text='Debito/Transferencia', value='Debito', indicatoron=False, variable=medio, width=10, command=cuotas)
medioentry3 = Radiobutton(
    miframe1, text='Credito', value='Credito', indicatoron=False, variable=medio, width=10, command=cuotas)

medioentry1.grid(row=6, column=1, padx=10)
medioentry2.grid(row=6, column=2, padx=10)
medioentry3.grid(row=6, column=3, padx=10)

cuotas = IntVar()
cuotasentry = ttk.Combobox(
    miframe1, textvariable=cuotas, state='disable', values=list(range(1, 19)))
cuotasentry.grid(row=7, column=1, columnspan=2)
cuotas.set("")


monto = IntVar()
costoentry = Entry(miframe1, textvariable=monto)
costoentry.grid(row=8, column=1, columnspan=2)

botonenvio = Button(miframe2, text='Enviar', command=crear)
botonenvio.grid(row=1, column=0, padx=10, pady=10, sticky="e")

botonborrar = Button(miframe2, text='Borrar', command=limpiar_campos)
botonborrar.grid(row=1, column=1, padx=10, pady=10, sticky="e")

botonsalir = Button(miframe2, text='Salir', command=salir_app)
botonsalir.grid(row=1, column=2, padx=10, pady=10, sticky="e")

raiz.mainloop()
