import tkinter as tk
from tkinter import *
from tkinter import messagebox
# from tkinter.ttk import *
# from tkinter import ttk
import pymysql
# import inventario

class Student():
			
	def inicio_sesion(self):
		global pantalla1
		pantalla1 = Toplevel(pantalla)
		pantalla1.geometry("400x250")
		pantalla1.title("Inicio de Sesión")
		pantalla1.iconbitmap("logoujat.ico")

		# Label(pantalla1, text="Por favor ingrese Usuario y Contraseña").pack()
		# Label(pantalla1, text="").pack()

		cinta2=Label(pantalla1,text="Ingrese Usuario y Contraseña", bg="green", fg="white", width="50", height="2", font=("Arial",15)).pack()
		Label(pantalla1,text="").pack()

		global nombreusuario_verify
		global contrasenausuario_verify

		self.nombreusuario_verify=StringVar()
		self.contrasenausuario_verify=StringVar()

		global nombre_usuario_entry
		global contrasena_usuario_entry


		Label(pantalla1, text="Usuario", font="Arial 10 bold").pack()
		nombre_usuario_entry = Entry(pantalla1, textvariable=self.nombreusuario_verify)
		nombre_usuario_entry.focus()
		nombre_usuario_entry.pack()
		Label(pantalla1).pack

		Label(pantalla1, text="Contraseña", font="Arial 10 bold").pack()
		contrasena_usuario_entry = Entry(pantalla1,  show="*", textvariable=self.contrasenausuario_verify)
		contrasena_usuario_entry.pack()
		Label(pantalla1).pack()

		Button(pantalla1, text="Iniciar sesión", font="Arial 10 bold", height="2", width="30", borderwidth=5, bg="snow", command=self.validando_datos).pack()


	def registrar(self):
		global pantalla2

		pantalla2=Toplevel(pantalla)
		pantalla2.geometry("400x250")
		pantalla2.title("Registro")
		pantalla2.iconbitmap("logoujat.ico")

		global nombreusuario_entry
		global contrasenausuario_entry

		self.nombre_usuario_entry=StringVar()
		self.contrasena_usuario_entry=StringVar()

		cinta3=Label(pantalla2,text="Registro de Usuario", bg="green", fg="white", width="50", height="2", font=("Arial",15)).pack()
		Label(pantalla2,text="").pack()

		Label(pantalla2, text="Nuevo Usuario", font="Arial 10 bold").pack()
		self.nombreusuario_entry = Entry(pantalla2)
		self.nombreusuario_entry.focus()
		self.nombreusuario_entry.pack()
		Label(pantalla2).pack

		Label(pantalla2, text="Nueva Contraseña", font="Arial 10 bold").pack()
		self.contrasenausuario_entry = Entry(pantalla2, show="*")
		self.contrasenausuario_entry.pack()
		Label(pantalla2).pack

		# nombreusuario_entry.delete(0, END)
		# contrasenausuario_entry.delete(0, END)

		Label(pantalla2,text="").pack()
		Button(pantalla2, text="Registrar", font="Arial 10 bold", height="2", width="30", borderwidth=5, bg="snow", command=self.inserta_datos).pack()

	def inserta_datos(self):
		bd=pymysql.connect(
			host="localhost",
			user="root",
			password="",
			db="inventariodacea"
			)

		fcursor=bd.cursor()
		sql="INSERT INTO login (usuario, contraseña) VALUES ('{0}', '{1}')".format(self.nombreusuario_entry.get(), self.contrasenausuario_entry.get())

		try:
			fcursor.execute(sql)
			bd.commit()
			messagebox.showinfo(message="Registro Exitoso", title="Aviso")
			pantalla2.destroy()
		except Exception as e:
			bd.rollback()
			messagebox.showerror(message="No se registro", title="Error")

		bd.close()

	def validando_datos(self):
	
		bd=pymysql.connect(
			host="localhost",
			user="root",
			password="",
			db="inventariodacea"
		)

		fcursor=bd.cursor()
		fcursor.execute("SELECT contraseña FROM login WHERE usuario = '"+self.nombreusuario_verify.get()+"'AND contraseña='"+self.contrasenausuario_verify.get()+"'")

		try:
			if fcursor.fetchall():
				# messagebox.showinfo(title="Inicio de sesion correcta", message="Usuario y Contraseña correcta")
				pantalla1.destroy()
				pantalla.destroy()
				self.inventario()
				con.close()
						

			else:
				messagebox.showerror(title="Inicio de sesion incorreta", message="Usuario y Contraseña Incorrecta")
				pantalla1.destroy()
					
			bd.close()

		except Exception as es:
			 messagebox.showerror('Error',es)
		

	def inventario(self):
		self.pantalla4=pantalla4
		self.pantalla4.title("Sistema de Inventario")
		self.pantalla4.geometry("1350x690+0+0")
		self.pantalla4.resizable(False,False)

		cinta=Label(self.pantalla4,text="Inventario", bg="green", fg="white", width="210", height="2", font=("Arial",30))
		cinta.pack(side=TOP)

		#Frame de edicion de datos de la base de datos
		frame1 = Frame(self.pantalla4, bd=4, relief=RIDGE, bg="white")
		frame1.place(x=10, y=100, width=410, height=515)

		tituloedicion = Label(frame1, text="Control de Inventario", bd=2, bg="white", font=("Arial", 25, "bold"))
		tituloedicion.grid(row=0, columnspan=4, pady=10)

		#==VARIABLES==#

		numeroinventario_var=StringVar()
		nombre_var=StringVar()
		descripcion_var=StringVar()
		ubicacion_var=StringVar()
		encargado_var=StringVar()
		nota_var=StringVar()
		maestro_var=StringVar()

		style = ttk.Style() 
		style.configure('TEntry', foreground = 'green') 

		lbl_numeroinventario = Label(frame1, text="No. De Inventario:", bg="white", font=("Arial", 15, "bold"))
		lbl_numeroinventario.grid(row=1, column=0, pady=10, padx=8, sticky="w")
		txt_numeroinventario = ttk.Entry(frame1, textvariable=self.numeroinventario_var, font=("Arial", 12, "bold"), justify = CENTER)
		txt_numeroinventario.focus_force() 
		txt_numeroinventario.grid(row=1, column=1, pady=10, padx=1, sticky="w")

		lbl_nombre = Label(frame1, text="Nombre:", bg="white", font=("Arial", 15, "bold"))
		lbl_nombre.grid(row=2, column=0, pady=10, padx=8, sticky="w")
		txt_nombre = ttk.Entry(frame1, textvariable=self.nombre_var, font=("Arial", 12), justify = CENTER)
		txt_nombre.grid(row=2, column=1, pady=10, padx=1, sticky="w")

		lbl_descripcion = Label(frame1, text="Descripción:", bg="white", font=("Arial", 15, "bold"))
		lbl_descripcion.grid(row=3, column=0, pady=10, padx=8, sticky="w")
		txt_descripcion = ttk.Entry(frame1, textvariable=self.descripcion_var, font=("Arial", 12), justify = CENTER)
		txt_descripcion.grid(row=3, column=1, pady=10, padx=1, sticky="w")

		lbl_ubicacion = Label(frame1, text="Ubicación: ", bg="white", font=("Arial", 15, "bold"))
		lbl_ubicacion.grid(row=4, column=0, pady=10, padx=8, sticky="w")
		txt_ubicacion = ttk.Entry(frame1, textvariable=self.ubicacion_var, font=("Arial", 12), justify = CENTER)
		txt_ubicacion.grid(row=4, column=1, pady=10, padx=1, sticky="w")

		lbl_encargado = Label(frame1, text="Encargado: ", bg="white", font=("Arial", 15, "bold"))
		lbl_encargado.grid(row=5, column=0, pady=10, padx=8, sticky="w")
		txt_encargado = ttk.Entry(frame1, textvariable=self.encargado_var, font=("Arial", 12), justify = CENTER)
		txt_encargado.grid(row=5, column=1, pady=10, padx=1, sticky="w")

		lbl_nota = Label(frame1, text="Nota: ", bg="white", font=("Arial", 15, "bold"))
		lbl_nota.grid(row=6, column=0, pady=10, padx=8, sticky="w")
		txt_nota = Text(frame1)
		txt_nota.config(width=20, height=8, font=("Arial",12),  bd=5, padx=1, pady=2, foreground = 'green', selectbackground="red")
		txt_nota.grid(row=6, column=1, pady=10, padx=1, sticky="s")

		#Frame de la lista de la base de datos

		frame2 = Frame(self.pantalla4, bd=4, relief=RIDGE, bg="white")
		frame2.place(x=440, y=100, width=900, height=515)

		lbl_buscar = Label(frame2, text="Buscar por: ", bg="white", font=("Arial", 15, "bold"))
		lbl_buscar.grid(row=0, column=0, pady=10, padx=20, sticky="w")

		combo_search = ttk.Combobox(frame2, width=10, textvariable=self.maestro_var, font=("Arial", 15, "bold"), state='readonly')
		combo_search['values']=["Ramiro","Natividad"]
		combo_search.grid(row=0, column=2, padx=20, pady=10)

		txt_search = Entry(frame2, width=20, font=("Arial", 15, "bold"), bd=5, relief=GROOVE)
		txt_search.grid(row=0, column=3, padx=10, pady=10, sticky="w")

		btn_buscar= Button(frame2, text="Buscar", height= 2, width=15,  borderwidth=5, bg="snow")
		btn_buscar.grid(row=0, column=4, padx=10, pady=2)

		btn_mostrartodo= Button(frame2, text="Mostrar todo", height=2, width=15,  borderwidth=5, bg="snow")
		btn_mostrartodo.grid(row=0, column=5, padx=10, pady=2)

		tabla_frame=Frame(frame2, bd=4, relief=RIDGE, bg="crimson")
		tabla_frame.place(x=10, y=55, width=874, height=445)


		scroll_x=Scrollbar(tabla_frame, orient=HORIZONTAL)
		scroll_y=Scrollbar(tabla_frame, orient=VERTICAL)
		tabla_inventario=ttk.Treeview(tabla_frame, columns=("numeroinventario", "nombre", "descripcion", "ubicacion", "encargado", "nota"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM, fill=X)
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_x.config(command=tabla_inventario.xview)
		scroll_y.config(command=tabla_inventario.yview)
		tabla_inventario.heading("numeroinventario", text="No. de Inventario")
		tabla_inventario.heading("nombre", text="Nombre")
		tabla_inventario.heading("descripcion", text="Descripción")
		tabla_inventario.heading("ubicacion", text="Ubicación")
		tabla_inventario.heading("encargado", text="Encargado")
		tabla_inventario.heading("nota", text="Nota")
		tabla_inventario.pack(fill=BOTH, expand=1)
		tabla_inventario['show']='headings'
		tabla_inventario.column("numeroinventario", width=70)
		tabla_inventario.column("nombre", width=100)
		tabla_inventario.column("descripcion", width=100)
		tabla_inventario.column("ubicacion", width=100)
		tabla_inventario.column("encargado", width=70)
		tabla_inventario.column("nota", width=160)

		#Frame de los botones


		frame3 = Frame(self.pantalla4, bd=4, relief=FLAT, bg="green")
		frame3.place(x=0, y=620, width=1400, height=80)

		btn1 = Button(frame3,text="Crear", font="Arial 10 bold", height="2", width="30", borderwidth=5, bg="snow").grid(row=1, column=0, padx=40, pady=10)

		btn1 = Button(frame3,text="Actualizar", font="Arial 10 bold", height="2", width="30", borderwidth=5, bg="snow").grid(row=1, column=1, padx=40, pady=10)

		btn1 = Button(frame3,text="Eliminar", font="Arial 10 bold", height="2", width="30", borderwidth=5, bg="snow").grid(row=1, column=2, padx=40, pady=10)

		btn1 = Button(frame3,text="Consultar", font="Arial 10 bold", height="2", width="30", borderwidth=5, bg="snow").grid(row=1, column=3, padx=40, pady=10)

		return inventario

#Pantalla1
	def __init__(self, pantalla):
		pantalla.geometry("320x450")
		pantalla.title("Bienvenidos")
		
		miFrame=Frame(pantalla)
		miFrame.pack()


		


		miFrame2=Frame(pantalla)
		miFrame2.pack()

		cinta=Label(miFrame2,text="Acceso al Sistema", bg="green", fg="white", width="28", height="2", font=("Arial",15))
		cinta.grid(row=0, column=0, sticky="e", padx=1, pady=1)


		btn1 = Button(miFrame2,text="Iniciar sesion", font="Arial 10 bold", height="2", width="30", borderwidth=5, bg="snow", command=self.inicio_sesion).grid(row=1, column=0, padx=9, pady=10)

		Label(miFrame2,text="")

		btn2 = Button(miFrame2,text="Registrar", font="Arial 10 bold", height="2", width="30", borderwidth=5, bg="snow", command=self.registrar).grid(row=2, column=0, padx=9, pady=1)





pantalla = Tk()
pantalla.iconbitmap("logoujat.ico")
image=PhotoImage(file="logodacea.png")
image=image.subsample(2,2)
label=Label(image=image)
label.pack()

ob=Student(pantalla)
pantalla.mainloop()