import basic
import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import basic
from tkinter import *
from tkinter import messagebox as MessageBox


def validar_linea(text,cuadro_text):

	result, error = basic.run('<stdin>', text)
	if error:  MessageBox.showerror("Compilador",error.as_string()+"en la  linea")
	if result: cuadro_text.insert (END, result)

class Aplicacion:
    
    def __init__(self):
        self.ventana1=tk.Tk()
        self.agregar_menu()
        self.ventana1.title("ComPy")
        self.ventana1.geometry("950x600")
        self.ventana1.resizable(0,0)
        self.ventana1.config(bg="#248A7D")
        self.scrolledtext1=st.ScrolledText(self.ventana1, width=70, height=50)
        self.scrolledtext2=st.ScrolledText(self.ventana1, width=40, height=50)
        
        self.scrolledtext1.config(bg="#C6E0DE",fg="RED")
        self.scrolledtext2.config(state=DISABLED,bg="#90B6B3",fg="RED")
        self.scrolledtext1.insert(1.0, "Selecione File -> Cargar Codigo (busque el archivo Ejemplo.cp)-> abrir -> opciones y compilar")
        
        self.scrolledtext1.grid(column=0,row=0, padx=20, pady=5)     
        self.scrolledtext2.grid(column=0,row=0, padx=20, pady=5,sticky=N+E)

        self.scrolledtext2.place(x=600,y=40)
        self.scrolledtext1.place(x=20,y=40)
    

        texto = Label(self.ventana1, text="Escritorio",font=("Times", 13))
        texto.pack()
        texto.place(x=290,y=10)
        texto.config(relief="raised",bg="#05FADB")
        

        compilador = Label(self.ventana1, text="Compilador",font=("times", 13))
        compilador.pack()
        compilador.place(x=730,y=10)
        compilador.config(relief="raised",bg="#05FADB")
        self.nombrearch = ""

        self.ventana1.mainloop()
        

    def agregar_menu(self):
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Salvar", command=self.guardar)
        opciones1.add_command(label="Salvar como", command=self.guardar_como)
        opciones1.add_command(label="Cargar Codigo", command=self.cargar)
        opciones1.add_separator()
        opciones1.add_command(label="Cerrar", command=self.salir)
        menubar1.add_cascade(label="File", menu=opciones1)

        opciones2 = tk.Menu(menubar1, tearoff=0)
        opciones2.add_command(label="Compilar", command=self.compilar)
        opciones2.add_command(label="Correr", command=NoDefaultRoot )
        menubar1.add_cascade(label="Opciones", menu=opciones2)
            
    
    def salir(self):
        sys.exit()
    def guardar(self):
        if self.nombrearch!='':
            archi1=open(self.nombrearch, "w", encoding="utf-8")
            archi1.write(self.scrolledtext1.get("1.0", tk.END))
            archi1.close()
            mb.showinfo("Codigo ", "Los datos se Guardaron")
        else:
            self.guardar_como()
            
    def guardar_como(self):
        self.nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Salvar como",defaultextension=".cp",filetypes = (("cp files",".cp"),("todos los archivos","*.*")))
        if self.nombrearch!='':
            archi1=open(self.nombrearch, "w", encoding="utf-8")
            archi1.write(self.scrolledtext1.get("1.0", tk.END))
            archi1.close()
            mb.showinfo("Codigo ", "Los datos se Guardaron")

    def cargar(self):
        self.nombrearch=fd.askopenfilename(initialdir = "/",title = "Elegir archivo",filetypes = (("cp files","*.cp"),("todos los archivos","*.*")))
        if self.nombrearch!='':
            archi1=open(self.nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.scrolledtext1.delete("1.0", tk.END) 
            self.scrolledtext1.insert("1.0", contenido)

    def compilar(self):
         
        if self.nombrearch!='':

            ruta=self.nombrearch
            ruta=ruta.replace("C:/","/")
            archi1=open(ruta, "r")
            contenido=""
            self.scrolledtext2.config(state=NORMAL)
          

            for linea in archi1.readlines():
                if(linea !="\n"):
                    validar_linea(linea,self.scrolledtext2)
                    contenido=contenido+linea
                    self.scrolledtext2.insert(END,'\n')
            
            self.scrolledtext2.config(state=DISABLED)
            archi1.close()
            self.scrolledtext1.delete("1.0", tk.END) 
            self.scrolledtext1.insert("1.0", contenido)

aplicacion1=Aplicacion()