import tkinter as tk
from tkinter import * 
from tkinter import ttk
import webbrowser
import time
import mysql.connector

miCon = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='hospital-campaña-ctes' )
cur = miCon.cursor()


ventana= tk.Tk()
ventana.title("Hospital de Campaña Corrientes")
ventana.geometry("600x600+600+60")
ventana.resizable(width=False, height=False)
ventana.iconbitmap("H_C.ico")



# login
loginframe=Frame()
loginframe.pack(side="bottom",anchor="center")
loginframe.config(width="840",height="800", bg="skyblue",bd=15,relief="groove")
loginframe.config(relief="sunken")
# .image("campaña.jpg")

#variables
usuario=tk.StringVar()
password=tk.StringVar()


lebelUsuario=Label(loginframe, text="USUARIO", font=("sant serif",20),fg="Blue",background="skyblue" )
lebelUsuario.place(x="55",y="250")
textoUsuario=tk.Entry(ventana, textvar=usuario, width=30, relief="flat")
textoUsuario.place(x="40", y="300", width=200, height=30)
textoUsuario.config(justify="right")

lebelContrasena=Label(loginframe, text="CONTRASEÑA", font=("sant serif",20),fg="Blue",background="skyblue" )
lebelContrasena.place(x="20",y="350")
textoContrasena=tk.Entry(ventana, textvar=password, width=30, relief="flat")
textoContrasena.place(x="40", y="400",width=200,height=30)
textoContrasena.config(justify="right", show="*")

 #funciones
def guardar_datos():
    # Obtener los valores de los cuadros de texto
    
    usuario = textoUsuario.get()
    contrasena = textoContrasena.get()

    consulta = "INSERT INTO login (DNI_Personal, Contrasena) VALUES (%s, %s )"
    valores = (int(usuario), contrasena)
    cur.execute(consulta, valores)

    miCon.commit()
    miCon.close()


crear_button=tk.Button(ventana, text='Ingresar', command=guardar_datos, cursor="hand2", width=14, height=3, fg="blue", background="skyblue", activeforeground="green")
crear_button.pack()
crear_button.place(x="300",y="500")



def login():
    nombre=usuario.get()
    contraseña=password.get()
    if nombre == "12345678" and contraseña == "1234":
        correcta()
    else:
        incorrecta()



Boton1=tk.Button(ventana, text='Ingresar', command=login, cursor="hand2", width=14, height=3, fg="blue", background="skyblue", activeforeground="green")
Boton1.place(x="80",y="500")


def incorrecta():
    incorrect= Tk()
    incorrect.title("Hospital de Campaña Corrientes")
    incorrect.geometry("400x200+200+40")
    incorrect.resizable(width=False, height=False)
    incorrect.title("Hospital de Campaña Corrientes")
    
    incorrect.iconbitmap("H_C.ico")
    incorrect.config(bg="blue")
    incorrect.config(bd=0.5)
    incorrect.config(relief="groove")
    lebelincorrecto=Label(incorrect, text="Usuario o Contraseña Incorrecta", bg="red", font=("comic sans ms",15),fg="skyblue")
    lebelincorrecto.place(x="50",y="80")

    incorrect.mainloop()



def correcta():
    ventana.withdraw()
    raiz= Tk()
    raiz.title("Hospital de Campaña Corrientes")
    raiz.geometry("800x600+800+60")
    raiz.iconbitmap("H_C.ico")
    raiz.config(bg="skyblue")
    raiz.config(bd=35)
    raiz.config(relief="groove")
    raiz.resizable(width=False, height=False)

    lebeladmision=Label(raiz, text="ADMISION", bg="Skyblue", font=("comic sans ms",25),fg="white")
    lebeladmision.place(x="50",y="20")

    #lebel datos paciente
    lebeldatospac=Label(raiz, text="Datos Paciente", bg="orange", font=("comic sans ms",15),fg="white" )
    lebeldatospac.place(x="50",y="100")
    lebelnombre_pac=Label(raiz, text="Nombre :", font=("comic sans ms",10),fg="black" )
    lebelnombre_pac.place(x="50",y="210")
    lebeliapellido_pac=Label(raiz, text="Apellido :", font=("comic sans ms",10),fg="black" )
    lebeliapellido_pac.place(x="50",y="180")
    lebelidni_pac=Label(raiz, text="D.N.I :", font=("comic sans ms",10),fg="black" )
    lebelidni_pac.place(x="50",y="150")
    lebelfecha_nac=Label(raiz, text="Fecha Nac :", font=("comic sans ms",10),fg="black" )
    lebelfecha_nac.place(x="50",y="240")

    #cadros de textos datos paciente
    cuadrotnombre_pac=Entry(raiz)
    cuadrotnombre_pac.place(x="200",y="210")
    cuadrotnombre_pac.config(justify="right")
    cuadrotapellido_pac=Entry(raiz)
    cuadrotapellido_pac.place(x="200",y="180")
    cuadrotapellido_pac.config(justify="right")
    cuadrotdni_pac=Entry(raiz)
    cuadrotdni_pac.place(x="200",y="150")
    cuadrotdni_pac.config(justify="right")
    cuadrotfecha_nac_pac=Entry(raiz)
    cuadrotfecha_nac_pac.place(x="200",y="240")
    cuadrotfecha_nac_pac.config(justify="right")


    #lebel contacto paciente
    lebelcontacac=Label(raiz, text="Contacto Paciente", bg="orange", font=("comic sans ms",15),fg="white" )
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

    #cuadros contacto paciente
    cuadrotcelular_pac=Entry(raiz)
    cuadrotcelular_pac.place(x="550",y="150")
    cuadrotcelular_pac.config(justify="right")
    cuadrotdireccion_pac=Entry(raiz)
    cuadrotdireccion_pac.place(x="550",y="180")
    cuadrotdireccion_pac.config(justify="right")
    cuadrottel_alter_pac=Entry(raiz)
    cuadrottel_alter_pac.place(x="550",y="210")
    cuadrottel_alter_pac.config(justify="right")
    cuadrotlocalidad_pac=Entry(raiz)
    cuadrotlocalidad_pac.place(x="550",y="240")
    cuadrotlocalidad_pac.config(justify="right")
    cuadrotc_p_pac=Entry(raiz)
    cuadrotc_p_pac.place(x="550",y="270")
    cuadrotc_p_pac.config(justify="right")
    cuadrotcorreo_elec_pac=Entry(raiz)
    cuadrotcorreo_elec_pac.place(x="550",y="300")
    cuadrotcorreo_elec_pac.config(justify="right")

    #datos obra social
    lebeldatospac=Label(raiz, text="Obra Social Paciente", bg="orange", font=("comic sans ms",15),fg="white" )
    lebeldatospac.place(x="50",y="350")

    lebelCoberturaSocial=Label(raiz, text="Cobertura Social", font=("comic sans ms",10),fg="Black" )
    lebelCoberturaSocial.place(x="50",y="410")

    cuadrotCoberturaSocial=Entry(raiz)
    cuadrotCoberturaSocial.place(x="400",y="410")
    cuadrotCoberturaSocial.config(justify="right", width=50)
    


    # --------------------------------contraseña-----------------------------------

    #cuadrotcontraseña=Entry(miframe)
    #cuadrotcontraseña.place(x="200",y="350")
    #cuadrotcontraseña.config(justify="right",show="*")

    # ---------------------------------botton---------------------------------
    buttonregistrar=Button(raiz, text="REGISTRAR", font="15",  background="black", fg="red")
    buttonregistrar.place(x="550",y="20")

    def obras_sociales():
        webbrowser.open_new('https://sisa.msal.gov.ar/sisa/#sisa')
    buttonbuscar=Button(raiz, text="BUSCAR", font="15",  background="black", fg="red")
    buttonbuscar.place(x="400",y="20")

    
    buttonsigiente=Button(raiz, text="PUCO", font="15", background="black", fg="red", command=obras_sociales)
    buttonsigiente.place(x="400",y="350")
    
   



# salir de la app
    def cerrarSecion():
        raiz.destroy()

    buttonCerrarSesion=Button(raiz, text="CERRAR SESION",command=cerrarSecion, font="15",  background="black", fg="red")
    buttonCerrarSesion.place(x="300",y="500")


    raiz.mainloop()
    






ventana.mainloop()

