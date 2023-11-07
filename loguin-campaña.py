import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser
import time
import mysql.connector
from PIL import ImageTk, Image


miCon = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='hospital-campaña-ctes' )
cur = miCon.cursor()

loginframe = tk.Tk()
loginframe.title("Hospital de Campaña Corrientes")
loginframe.geometry("600x600+600+60")
loginframe.resizable(width=False, height=False)
loginframe.iconbitmap("H_C.ico")

# Carga la imagen y ajusta su tamaño para que llene todo el frame
imagen = Image.open("imagen_login.jpg")
imagen = imagen.resize((600, 600))
imagen = ImageTk.PhotoImage(imagen)

# Crea una etiqueta para mostrar la imagen como fondo
etiqueta = Label(loginframe, image=imagen)
etiqueta.place(x=0, y=0, relwidth=1, relheight=1)

# Configura el frame
loginframe.config(bg="skyblue", bd=15, relief="groove")

#variables
usuario=tk.StringVar()
password=tk.StringVar()


lebelUsuario=Label(loginframe, text="USUARIO", font=("sant serif",30),fg="red",background="grey" )
lebelUsuario.place(x="200",y="50")
lebelUsuario.config(borderwidth=3, relief="raised")
textoUsuario=tk.Entry(loginframe, textvar=usuario, width=30, relief="flat")
textoUsuario.place(x="170", y="110", width=250, height=30,)
textoUsuario.config(justify="right",bg="skyblue",fg="blue", font=12, borderwidth=3, relief="raised")


lebelContrasena=Label(loginframe, text="CONTRASEÑA", font=("sant serif",30),fg="red",background="grey" )
lebelContrasena.place(x="145",y="180")
lebelContrasena.config(borderwidth=3, relief="raised")
textoContrasena=tk.Entry(loginframe, textvar=password, width=100, relief="flat")
textoContrasena.place(x="140", y="240",width=300,height=30)
textoContrasena.config(justify="right", show="*",bg="skyblue",fg="blue", font=12,borderwidth=3, relief="raised")

#funciones login

usuario = textoUsuario.get()
contrasena = textoContrasena.get()

def guardar_datos():
    usuario = textoUsuario.get()
    contrasena = textoContrasena.get()

    consulta = "INSERT INTO login (DNI_Personal, Contrasena) VALUES (%s, %s )"
    valores = (int(usuario), contrasena)
    cur.execute(consulta,valores)

    miCon.commit()
    messagebox.showinfo(title=None, message="Registro Exitoso")
    borrar_datos_adm()

def borrar_datos_adm():
    textoUsuario.delete(0, tk.END)
    textoContrasena.delete(0, tk.END)


def login():
    usuario = textoUsuario.get()
    contrasena = textoContrasena.get()   
    cur.execute("SELECT Contrasena FROM login WHERE DNI_Personal='"+usuario+"' and Contrasena='"+contrasena+"'")
    if cur.fetchall():
        messagebox.showinfo(title="Acceso", message="Acceso correcto")
        correcta()         
    else:
        messagebox.showinfo(title="Acceso", message="Usuario o contraseña incorrectos")   
    loginframe.withdraw()  
    miCon.close()          

#botones login

crear_button=tk.Button(loginframe, text='Registrarse', command=guardar_datos, font=10, cursor="hand2", width=14, height=3, fg="cyan", background="grey", activeforeground="green")
crear_button.pack()
crear_button.config(borderwidth=5, relief="raised")
crear_button.place(x="370",y="400")    
     
Boton1=tk.Button(loginframe, text='Ingresar', command=login, font=10, cursor="hand2", width=14, height=3, fg="cyan", background="grey", activeforeground="green")
Boton1.place(x="100",y="400")
Boton1.config(borderwidth=5, relief="raised")

#funcines registro paciente 

def correcta():
    loginframe.withdraw()
    raiz= Tk()
    raiz.title("Hospital de Campaña Corrientes")
    raiz.geometry("800x600+800+60")
    raiz.iconbitmap("H_C.ico")
    raiz.config(bg="skyblue")
    raiz.config(bd=35)
    raiz.config(relief="groove")
    raiz.resizable(width=False, height=False)

    lebeladmision=Label(raiz, text="ADMISION", bg="Skyblue", font=("comic sans ms",35),fg="red", borderwidth=0.5, relief="raised")
    lebeladmision.place(x="50",y="10")


    #lebel datos paciente
    lebeldatospac=Label(raiz, text="Datos Paciente", bg="cyan", font=("comic sans ms",15),fg="red" )
    lebeldatospac.place(x="50",y="100")
    lebelnombre_pac=Label(raiz, text="Nombre :", font=("comic sans ms",10),fg="black" )
    lebelnombre_pac.place(x="50",y="210")
    lebeliapellido_pac=Label(raiz, text="Apellido :", font=("comic sans ms",10),fg="black" )
    lebeliapellido_pac.place(x="50",y="180")
    lebelidni_pac=Label(raiz, text="D.N.I :", font=("comic sans ms",10),fg="black" )
    lebelidni_pac.place(x="50",y="150")
    lebelfecha_nac=Label(raiz, text="Fecha Nac :", font=("comic sans ms",10),fg="black" )
    lebelfecha_nac.place(x="50",y="240")

    #lebel contacto paciente
    lebelcontacac=Label(raiz, text="Contacto Paciente", bg="cyan", font=("comic sans ms",15),fg="red" )
    lebelcontacac.place(x="400",y="100")
    lebelcelular_pac=Label(raiz, text="Num Celular :", font=("comic sans ms",10),fg="black" )
    lebelcelular_pac.place(x="400",y="150")
    lebeldireccion_pac=Label(raiz, text="Dirección :", font=("comic sans ms",10),fg="black" )
    lebeldireccion_pac.place(x="400",y="180")
    lebelcel_alter_pac=Label(raiz, text="Tel Alternativo :", font=("comic sans ms",10),fg="black" )
    lebelcel_alter_pac.place(x="400",y="210")
    lebellocalidad_pac=Label(raiz, text="Localidad :", font=("comic sans ms",10),fg="black" )
    lebellocalidad_pac.place(x="400",y="240")
    lebelc_p_pac=Label(raiz, text="C.P :", font=("comic sans ms",10),fg="black" )
    lebelc_p_pac.place(x="400",y="270")
    lebelcorreo_elec_pac=Label(raiz, text="Correo Elec. :", font=("comic sans ms",10),fg="black" )
    lebelcorreo_elec_pac.place(x="400",y="300")


    #cadros de textos datos paciente
    cuadrotnombre_pac=tk.Entry(raiz)
    cuadrotnombre_pac.place(x="200",y="210")
    cuadrotnombre_pac.config(justify="right")
    cuadrotapellido_pac=tk.Entry(raiz)
    cuadrotapellido_pac.place(x="200",y="180")
    cuadrotapellido_pac.config(justify="right")
    cuadrotdni_pac=tk.Entry(raiz)
    cuadrotdni_pac.place(x="200",y="150")
    cuadrotdni_pac.config(justify="right")
    cuadrotfecha_nac_pac=tk.Entry(raiz)
    cuadrotfecha_nac_pac.place(x="200",y="240")
    cuadrotfecha_nac_pac.config(justify="right")

    #cuadros contacto paciente
    cuadrotcelular_pac=tk.Entry(raiz)
    cuadrotcelular_pac.place(x="550",y="150")
    cuadrotcelular_pac.config(justify="right")
    cuadrotdireccion_pac=tk.Entry(raiz)
    cuadrotdireccion_pac.place(x="550",y="180")
    cuadrotdireccion_pac.config(justify="right")
    cuadrottel_alter_pac=tk.Entry(raiz)
    cuadrottel_alter_pac.place(x="550",y="210")
    cuadrottel_alter_pac.config(justify="right")
    cuadrotlocalidad_pac=tk.Entry(raiz)
    cuadrotlocalidad_pac.place(x="550",y="240")
    cuadrotlocalidad_pac.config(justify="right")
    cuadrotc_p_pac=tk.Entry(raiz)
    cuadrotc_p_pac.place(x="550",y="270")
    cuadrotc_p_pac.config(justify="right")
    cuadrotcorreo_elec_pac=tk.Entry(raiz)
    cuadrotcorreo_elec_pac.place(x="550",y="300")
    cuadrotcorreo_elec_pac.config(justify="right")

    #datos obra social
    lebeldatospac=Label(raiz, text="Obra Social Paciente", bg="cyan", font=("comic sans ms",15),fg="red" )
    lebeldatospac.place(x="50",y="350")

    lebelCoberturaSocial=Label(raiz, text="Cobertura Social", font=("comic sans ms",10),fg="Black" )
    lebelCoberturaSocial.place(x="50",y="410")

    cuadrotCoberturaSocial=tk.Entry(raiz)
    cuadrotCoberturaSocial.place(x="400",y="410")
    cuadrotCoberturaSocial.config(justify="right", width=50)
    

    def registrar_pac():
        Nombres_Pac = cuadrotnombre_pac.get()
        Apellidos_Pac = cuadrotapellido_pac.get()
        DNI_Pac = cuadrotdni_pac.get()
        F_Nac_Pac = cuadrotfecha_nac_pac.get()
        Cel_Pac = cuadrotcelular_pac.get()
        Direc_Pac= cuadrotdireccion_pac.get()
        Tel_Alt_Pac= cuadrottel_alter_pac.get()
        Localid_Pac = cuadrotlocalidad_pac.get()
        C_Post_pac = cuadrotc_p_pac.get()
        C_Elect_Pac = cuadrotcorreo_elec_pac.get()
        Cobertura_S_Pac = cuadrotCoberturaSocial.get()

        consul = "INSERT INTO paciente (Nombres, Apellidos, DNI, Fecha_Nacimiento, Num_Celular_Pac, Direccion_Pac, Tel_Alter_Pac, Localidad_Pac, Cod_Postal_Pac, Correo_Elect_Pac, Cobertura_Social_Pac) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = ( Nombres_Pac, Apellidos_Pac, int(DNI_Pac), F_Nac_Pac, int(Cel_Pac), Direc_Pac, int(Tel_Alt_Pac), Localid_Pac, int(C_Post_pac), C_Elect_Pac, Cobertura_S_Pac,)
        cur.execute(consul, val)
        ID_Paciente = cur.lastrowid
        miCon.commit()
        messagebox.showinfo(title=None, message="Registro Exitoso")
        borrar_datos_adm()

    
    def borrar_datos_adm():
        cuadrotnombre_pac.delete(0, tk.END)
        cuadrotapellido_pac.delete(0, tk.END)
        cuadrotdni_pac.delete(0, tk.END)
        cuadrotfecha_nac_pac.delete(0, tk.END)
        cuadrotcelular_pac.delete(0, tk.END)
        cuadrotdireccion_pac.delete(0, tk.END)
        cuadrottel_alter_pac.delete(0, tk.END)
        cuadrotlocalidad_pac.delete(0, tk.END)
        cuadrotc_p_pac.delete(0, tk.END)
        cuadrotcorreo_elec_pac.delete(0, tk.END)
        cuadrotCoberturaSocial.delete(0, tk.END)
        

    def obras_sociales():
        webbrowser.open_new('https://sisa.msal.gov.ar/sisa/#sisa')


    def buscar_por_dni():
        cur.execute("SELECT * FROM paciente WHERE DNI='"+cuadrotdni_pac.get()+"'")
        rows = cur.fetchall()
        if rows:

            for row in rows:
                cuadrotnombre_pac.insert(0,row[1])
                cuadrotapellido_pac.insert(0,row[2])
                #cuadrotdni_pac.insert(0,row[3])
                cuadrotfecha_nac_pac.insert(0,row[4])
                cuadrotcelular_pac.insert(0,row[5])
                cuadrotdireccion_pac.insert(0,row[6])
                cuadrottel_alter_pac.insert(0,row[7])
                cuadrotlocalidad_pac.insert(0,row[8])
                cuadrotc_p_pac.insert(0,row[9])
                cuadrotcorreo_elec_pac.insert(0,row[10])
                cuadrotCoberturaSocial.insert(0,row[11])
        else:
            messagebox.showinfo(title="Buscar", message="Paciente no Registrado") 


    # salir de la app
    def cerrarSesion():
        res=messagebox.askquestion(title=None, message="¿Desea Cerrar Sesión?", icon="question")
        if res == "no":
            pass   
        else:
            raiz.destroy()

    #botones registro pacientes
        
    buttonsigiente=Button(raiz, text="PUCO", font="15", background="grey", fg="red", command=obras_sociales)
    buttonsigiente.place(x="400",y="350")
    buttonsigiente.config(borderwidth=5, relief="raised")

    buttonbuscar=Button(raiz, text="BUSCAR", command=buscar_por_dni, font="15",  background="grey", fg="red")
    buttonbuscar.place(x="400",y="20")
    buttonbuscar.config(borderwidth=5, relief="raised")

    buttonregistrar=tk.Button(raiz, text="REGISTRAR", command=registrar_pac, font="15",  background="grey", fg="red")
    buttonregistrar.pack()
    buttonregistrar.place(x="507",y="20")
    buttonregistrar.config(borderwidth=5, relief="raised")

    buttonlimpiar=tk.Button(raiz, text="LIMPIAR", command=borrar_datos_adm, font="15",  background="grey", fg="red")
    buttonlimpiar.pack()
    buttonlimpiar.place(x="630",y="20")
    buttonlimpiar.config(borderwidth=5, relief="raised")
            
    buttonCerrarSesion=Button(raiz, text="CERRAR SESION",command=cerrarSesion, font="15",  background="grey", fg="red")
    buttonCerrarSesion.place(x="300",y="470")
    buttonCerrarSesion.config(borderwidth=5, relief="raised")

    raiz.mainloop()

    
loginframe.mainloop()
