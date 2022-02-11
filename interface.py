from tkinter import *
from datetime import date as dt

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
raiz.iconbitmap('icono.ico')

miframe = Frame(raiz)
miframe.config(bg="red", bd=20)
miframe.pack()

# ------------- Funciones -----------------------

def categoria(choice):
    choice = categorias_var.get()
    return choice





hoy = dt.today()
dd = hoy.strftime('%Y.%m.%d')

# Labels
pagolabel = Label(miframe, text='¿Quien pago?')
pagolabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)

fechalabel = Label(miframe, text='Fecha:')
fechalabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)

destinolabel = Label(miframe, text='¿Para quién?')
destinolabel.grid(row=2, column=0, sticky='e', padx=10, pady=10)

categorialabel = Label(miframe, text='Categoria:')
categorialabel.grid(row=3, column=0, sticky='e', padx=10, pady=10)

subcategorialabel = Label(miframe, text='Subcategoria:')
subcategorialabel.grid(row=4, column=0, sticky='e', padx=10, pady=10)

mediolabel = Label(miframe, text='Medio de pago:')
mediolabel.grid(row=5, column=0, sticky='e', padx=10, pady=10)

costolabel = Label(miframe, text='Costo:')
costolabel.grid(row=6, column=0, sticky='e', padx=10, pady=10)

# Dataentry
option1 = StringVar(miframe)
pagoentry1 = Radiobutton(miframe, text='Ayelen',
                         value='Ayelen', indicatoron=False, variable=option1, width=10)
pagoentry2 = Radiobutton(miframe, text='Leonardo',
                         value='Leonardo', indicatoron=False, variable=option1, width=10)

pagoentry1.grid(row=0, column=1)
pagoentry2.grid(row=0, column=2)

fechaentry = Entry(miframe, textvariable=hoy)
fechaentry.grid(row=1, column=1)

option2 = StringVar(miframe)
destinoentry1 = Radiobutton(miframe, text='Comun',
                            value='Comun', indicatoron=False, variable=option2, width=10)
destinoentry2 = Radiobutton(
    miframe, text='Ayelen', value='Ayelen', indicatoron=False, variable=option2, width=10)
destinoentry3 = Radiobutton(
    miframe, text='Leonardo', value='Leonardo', indicatoron=False, variable=option2, width=10)

destinoentry1.grid(row=2, column=1, padx=10)
destinoentry2.grid(row=2, column=2, padx=10)
destinoentry3.grid(row=2, column=3, padx=10)


categorias_var = StringVar()
categoriaentry = OptionMenu(miframe, categorias_var,
                            *categorias.keys(), command=categoria)
categorias_var.set("Elegir una categoria")
categoriaentry.config()
categoriaentry.grid(row=3, column=1, columnspan=2)


subcategorias_var = StringVar()
subcategoriaentry = OptionMenu(
    miframe, subcategorias_var, *subcategoria,)
subcategorias_var.set("Elegir una categoria")
subcategoriaentry.config()
subcategoriaentry.grid(row=4, column=1, columnspan=2)

costoentry = Entry(miframe)
costoentry.grid(row=6, column=1)

botonenvio = Button(raiz, text='Enviar')

raiz.mainloop()

subcategoria