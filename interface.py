from tkinter import *
from datetime import date as dt
from tkinter import ttk
from tkcalendar import DateEntry


# ------------- Variables -----------------------

categorias = {
    'Alimentos': ('Supermercado', 'Carniceria',
                  'Almuerzo/Cena', 'Desayuno', 'Panaderia', 'Pastas', 'Fiambreria', 'Helado/dulces', 'Pescaderia', 'Verduleria'),
    'Casa': ('Seguro', 'Arreglos MO', 'Materiales', 'Electro'),
    'Auto': ('Seguro', 'Nafta', 'Service/Arreglos', 'Peajes', 'Lavadero', 'Patente'),
    'Impuestos': ('Rentas ABL', 'Aysa', 'Edesur', 'Metrogas'),
    'Servicios': ('Cablevisión', 'Netflix', 'Otro streaming',
                  'Movistar', 'Rappi/Pedidoya', 'Cuota club', 'Alertas Mercado'),
    'Viaticos': ('SUBE', 'Taxi'),
    'Entretenimiento': ('Restaurante', 'Juegos',
                        'Cine/Teatro', 'Reuniones', 'Deportes'),
    'Cuidado personal': ('Medicamentos', 'Obra Social', 'Peluqueria'),
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


def on_combobox_select(event):
    subcategoriaentry.set("")
    subcategoriaentry.config(values=categorias[categoriaentry.get()])


hoy = dt.today()
dd = hoy.strftime('%d-%m-%y')


# ------------- Barra Menu -----------------------

barramenu = Menu(raiz)
raiz.config(menu=barramenu)

bbddmenu = Menu(barramenu, tearoff=0)
bbddmenu.add_command(label='Conectar')
bbddmenu.add_command(label='Salir')

borrarmenu = Menu(barramenu, tearoff=0)
borrarmenu.add_command(label='Borrar campos')

ayudamenu = Menu(barramenu, tearoff=0)
ayudamenu.add_command(label='Licencia')
ayudamenu.add_command(label='Acerca de ..')

barramenu.add_cascade(label='BBDD', menu=bbddmenu)
barramenu.add_cascade(label='Borrar', menu=borrarmenu)
barramenu.add_cascade(label='Ayuda', menu=ayudamenu)

# ------------- Labels -----------------------

pagolabel = Label(miframe1, text='¿Quien pago?')
pagolabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)

fechalabel = Label(miframe1, text='Fecha:')
fechalabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)

destinolabel = Label(miframe1, text='¿Para quién?')
destinolabel.grid(row=2, column=0, sticky='e', padx=10, pady=10)

categorialabel = Label(miframe1, text='Categoria:')
categorialabel.grid(row=3, column=0, sticky='e', padx=10, pady=10)

subcategorialabel = Label(miframe1, text='Subcategoria:')
subcategorialabel.grid(row=4, column=0, sticky='e', padx=10, pady=10)

mediolabel = Label(miframe1, text='Medio de pago:')
mediolabel.grid(row=5, column=0, sticky='e', padx=10, pady=10)

costolabel = Label(miframe1, text='Costo:')
costolabel.grid(row=6, column=0, sticky='e', padx=10, pady=10)

# ------------- Dataentry -----------------------

option1 = StringVar(miframe1)
pagoentry1 = Radiobutton(miframe1, text='Ayelen',
                         value='Ayelen', indicatoron=False, variable=option1, width=10)
pagoentry2 = Radiobutton(miframe1, text='Leonardo',
                         value='Leonardo', indicatoron=False, variable=option1, width=10)

pagoentry1.grid(row=0, column=1)
pagoentry2.grid(row=0, column=2)

fechaentry = DateEntry(miframe1, width=20, year=hoy.year)
fechaentry.grid(row=1, column=1, columnspan=2)

option2 = StringVar(miframe1)
destinoentry1 = Radiobutton(miframe1, text='Comun',
                            value='Comun', indicatoron=False, variable=option2, width=10)
destinoentry2 = Radiobutton(
    miframe1, text='Ayelen', value='Ayelen', indicatoron=False, variable=option2, width=10)
destinoentry3 = Radiobutton(
    miframe1, text='Leonardo', value='Leonardo', indicatoron=False, variable=option2, width=10)

destinoentry1.grid(row=2, column=1, padx=10)
destinoentry2.grid(row=2, column=2, padx=10)
destinoentry3.grid(row=2, column=3, padx=10)

categoriaentry = ttk.Combobox(miframe1, values=list(categorias.keys()))
categoriaentry.grid(row=3, column=1, columnspan=2)
categoriaentry.bind("<<ComboboxSelected>>", on_combobox_select)

subcategoriaentry = ttk.Combobox(miframe1)
subcategoriaentry.grid(row=4, column=1, columnspan=2)

option3 = StringVar(miframe1)
medioentry1 = Radiobutton(miframe1, text='Efectivo',
                          value='efectivo', indicatoron=False, variable=option2, width=10)
medioentry2 = Radiobutton(
    miframe1, text='Debito/Transferencia', value='debito', indicatoron=False, variable=option2, width=10)
medioentry3 = Radiobutton(
    miframe1, text='Credito', value='credito', indicatoron=False, variable=option2, width=10)

medioentry1.grid(row=5, column=1, padx=10)
medioentry2.grid(row=5, column=2, padx=10)
medioentry3.grid(row=5, column=3, padx=10)

costoentry = Entry(miframe1)
costoentry.grid(row=6, column=1, columnspan=2)

botonenvio = Button(miframe2, text='Enviar')
botonenvio.grid(row=1, column=0, padx=10, pady=10, sticky="e")

botonborrar = Button(miframe2, text='Borrar')
botonborrar.grid(row=1, column=1, padx=10, pady=10, sticky="e")

botonsalir = Button(miframe2, text='Salir')
botonsalir.grid(row=1, column=2, padx=10, pady=10, sticky="e")

raiz.mainloop()
