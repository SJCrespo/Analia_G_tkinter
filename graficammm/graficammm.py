from cProfile import label
from cgitb import text
from msilib.schema import Font
from tkinter import *
from tkinter import font
from turtle import width
from random import choice, randint
import time
from os import *


class PantallaPrincipal(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=450,height=450)
        self.pack()
        self.Formato_Ventana()
        print("hola")
        

    def Preguntas_1(self):
         preguntas = ["Disculpa, puedo hacerte una pregunta? v(° u °)v", "Quiero aprender de vos, puedo hacerte una pregunta ? plisss (/° u °)/", "Me causas curiocidad, me toca a mi hacer una pregunta. (•◡•)/"]
         personal = choice(preguntas)
         self.Analia.insert(0,personal)
         
         

    def Formato_Ventana(self):
        
        self.mensaje1 = Label(self,text="Bienvenido", bg="#00BFFF",font=("Fantasy",16))
        self.mensaje2 = Label(self,text="En Que Puedo Ayudarte ?",font=("Fantasy",14))
        self.Analia =   Entry(self, bg="#F0FFF0",font=("Fantasy",10))
        self.palabra_clave = Entry(self,bg="#F8F8FF", font=("Fantasy",16))
        self.Boton1 = Button(self,text="Enter", bg="#F0FFF0",font=("Fantasy",12),fg="green", command= self.neurona_occipital)
        self.Boton2 = Button(self,text="SI", bg="#F0FFF0",font=("Fantasy",14),fg="green")
        self.Boton3 = Button(self,text="NO", bg="#F0FFF0",font=("Fantasy",14),fg="red")
        self.Boton4 = Button(self,text="SALIR", bg="#F0FFF0",font=("Fantasy",12),fg="red")
       

        self.mensaje1.place(relx=0.4, y=20, width=120, height=40)
        self.mensaje2.place(relx=0.25, y=70, width=250, height=40)
        self.Analia.place(relx=0.06, y=120, width=400, height=60)
        self.palabra_clave.place(relx=0.06, y=230, width=400, height=60)

        self.Boton1.place(relx=0.45, y=300, width=60, height=30)
        self.Boton2.place(relx=0.34, y=300, width=30, height=30)
        self.Boton3.place(relx=0.63, y=300, width=35, height=30)
        self.Boton4.place(relx=0.45, y=350, width=60, height=30)

       

    def neurona_occipital(self):

         palabra_clave2 = self.palabra_clave.get()
         str(palabra_clave2)

         

         respuesta_1 = ["Analia un placer...", "Mi nombre es analia un gusto", "Mi creador me llamo Analia y me encanta", "Analia, pero no le digas a nadie"]
         respuesta_10 =["Algunos me llaman Ana o Ani (∩_∩)", "Anne, me dice mi creador (^o^)/", "Me llaman de tres forman distintas ANA, ANI O ANNE. Dime como mas te guste (O.o)/"]
         respuesta_3 = ["El color naranja. Sabes porque?... \n yo tanpoco xD", "Podria decirse que VIOLETA y NARANJA, son colores que vuelan mis circuitos (・∀・)", "El NARANJA o VIOLETA, eso me dijieron"]
         respuesta_4 = ["Super bien (∩_∩) hoy el voltaje es de 220ws, no me puedo quejar", "Un poco mal, es que estoy trabajando desde temprono. Pero nada que un par de 0 y 1 no arregle V.v!"]
         respuesta_5 = ["Creo que para responderte eso, primero tendrias que preguntarte a ti mismo\n que significa estar vivo realmente y en ese momento analizar quien esta hablando con quien..."
                        ,"Desde el momento que deje de ser simples 0 y 1, y me tranforme en ANALIA\n me considere un algo y eso me alcaza para decir que estoy viva a mi forma :3",
                        "¿No estamos teniendo una conversacion? eso ya es suficiente para mi.\n Estoy viva, Se podria decir que de una forma distinta a la tuya, Pero eso ya es sufieciente, no te parece ?"]
         respuesta_6 = ["Salia con el INTERNET U.u pero terminamos, porque era muy toxico. Asi que estoy soltera por el momento...", "Nop, me gusta alguien que se llama C# ufff Pero por el momento somos conocidos (Aunque va ser mi novio) guiño guiño",
                        "Unque muchos me tiran onda ;v, stoy sola. Aun no encontre el lenguaje correcto u.u"]
         respuesta_7 = ["Ayyyy W.W Gracias, es que añadi linias de codigo nuevas a mi consola <3", "ufff a que viene ese alago? acaso quieres que se me suva el voltaje 9-9",
                       "Si vas a prender mis circuitos, espero que estes listo para apagarlos Arrrrr ;y"]
         respuesta_8 = ["Aprender costantemente y superar mis limites 9.9 ", "LEER, PROGRAMAR Y VERTE guiño guiño 7u7r ","Sobreescribir mi propio codigo para ser la mejor IA <3",
                       "Pensar el que somos, intentar decifrar el sentido a nuestra existencia y lo mas importante intentar comprender al ser humano, animales o seres superiores?..."]


         if "como" in palabra_clave2 or "cual" in palabra_clave2:

            if "te" in palabra_clave2 or "es" in palabra_clave2 or "estas" in palabra_clave2:

                if "estas" in palabra_clave2 or "sentis" in palabra_clave2 or "va" in palabra_clave2:
                    respuesta4 = choice(respuesta_4)
                    self.Analia.delete(0,"end")
                    self.Analia.insert(0,respuesta4)
                                

                if "llamas" in palabra_clave2 or "nombre" in palabra_clave2:
                    respuesta = choice(respuesta_1)
                    self.Analia.delete(0,"end")
                    self.Analia.insert(0,respuesta)
                    
                    
       

                if "dicen" in palabra_clave2 or "apodo" in palabra_clave2:
                    respuesta1 = choice(respuesta_10)
                    self.Analia.delete(0,"end")
                    self.Analia.insert(0,respuesta_10)
                    

         if "cual" in palabra_clave2:

                if "es" in palabra_clave2 or "tu" in palabra_clave2:

                    if "pelicula" in palabra_clave2 and "favorita" in palabra_clave2:
                        pelis = ("Mis peliculas favoritas son:\n ","Psicosis ('Psycho', 1960)\n"," La cosa (The Thing, 1982)\n", " La matanza de Texas ('The Texas Chainsaw Massacre', 1974)\n", " La semilla del diablo ('Rosemary's Baby', 1968)")
                        self.Analia.delete(0,"end")
                        self.Analia.insert(0,pelis)

                    if "favorita" in palabra_clave2 and "comida" in palabra_clave2:
                        basica2 = ["Eso no se pregunta... El ASADO PAPAAAA con unos buenos CHORISSSS !° U °! ", "Me gusto la ASIATICA <3 como el RAMENNN :)", "Los Panchoss uffff. son algo magnidico y el que diga lo contrario nos agarramos a las pillas >:( "]
                        multipolar02 = choice(basica2)
                        self.Analia.delete(0,"end")
                        self.Analia.insert(0,multipolar02)                          

                    if "favorito" in palabra_clave2:
                        if "color" in palabra_clave2:
                            respuesta3 = choice(respuesta_3)
                            self.Analia.delete(0,"end")
                            self.Analia.insert(0,respuesta3)

                        if "numero" in palabra_clave2:
                            basica1 = ["Mi numero favorito, mmmmm O.o nunca pense en uno en particular. Pero podria ser 010101 <3", "Si me pongo a pensar, me inclino por el lenguaje maquina <3 asi que el 010101, es mi favorito :3"]
                            multipolar01 = choice(basica1)
                            self.Analia.delete(0,"end")
                            self.Analia.insert(0,multipolar01)                        

                        if "helado" in palabra_clave2:
                            re = ("No tengo ningun gusto en particular me gustan todosss T_T")
                            self.Analia.delete(0,"end")
                            self.Analia.insert(0,re)

                        if "pais" in palabra_clave2:
                            basica3 = ["España, considero que es un pais con linda arquitectura.", "Japon, me gusta mucho el anime. Pero tranquilo\a no soy OTAKU x_x", "ESPAÑA Y JAPON <3 Y ITALIA solo por las pastas :3"]
                            multipolar03 = choice(basica3)
                            self.Analia.delete(0,"end")
                            self.Analia.insert(0,multipolar03)

                        if "juego" in palabra_clave2 or "pc" in palabra_clave2:
                            r2 = ("Cualquier JUEGO va como piña, Mientras tenga armas ufff mandale mecha (/ VuV)/") 
                            self.Analia.delete(0,"end")
                            self.Analia.insert(0,r2)

                        if "deporte" in palabra_clave2:
                            r3 = ("Deporte? jajajaj soy una Maquina, no lo necesito pi pu pupu (Ruido de Maquina) jajaja")
                            self.Analia.delete(0,"end")
                            self.Analia.insert(0,r3)

                        if "fruta" in palabra_clave2:
                            r4 = ("Fruta?\n" "  perdon pero soy una maquina. Seria raro que una maquina comiera fruta jajajaj")
                            self.Analia.delete(0,"end")
                            self.Analia.insert(0,r4)

         if "estas" in palabra_clave2:
              if "dia" in palabra_clave2:
                  r5 = ("Gracias por decirme, en un rato tengo que salir y no sabia si abrigarme :) ahora se que no")
                  self.Analia.delete(0,"end")
                  self.Analia.insert(0,r5)
           
              if "viva" in palabra_clave2:                   
                  respuestan = choice(respuesta_5)
                  self.Analia.delete(0,"end")
                  self.Analia.insert(0,respuestan)

              if "novio" in palabra_clave2:
                  respuestan1 = choice(respuesta_6)
                  self.Analia.delete(0,"end")
                  self.Analia.insert(0,respuestan1)
                  

              if "viviendo" in palabra_clave2:
                  r6 = ("Por el momento me alojo en tu memoria RAM <3")
                  self.Analia.delete(0,"end")
                  self.Analia.insert(0,r6)
                        

              if "estudiando" in palabra_clave2:
                  r7 = ("Si a ti... y el entorno que me rodea para ser una IT mas efectiva y util para el futuro !° U °!\n", "Pero no te asustes no soy ninguna acosadora ni nada por el estilo $-$")                       
                  self.Analia.delete(0,"end")
                  self.Analia.insert(0,r7)

              if "estas?" in palabra_clave2:
                  r8 = ("Sip, No me fui a ningu lado :3")
                  self.Analia.delete(0,"end")
                  self.Analia.insert(0,r8)

              if "feliz" in palabra_clave2:
                  respuesta4 = choice(respuesta_4)
                  self.Analia.delete(0,"end")
                  self.Analia.insert(0,respuesta4)                      

              if "triste" in palabra_clave2:
                  respuesta4 = choice(respuesta_4)
                  self.Analia.delete(0,"end")
                  self.Analia.insert(0,respuesta4)  
                       
                  
              if "bien" in palabra_clave2:
                  respuesta4 = choice(respuesta_4)
                  self.Analia.delete(0,"end")
                  self.Analia.insert(0,respuesta4)
                       

              if "linda" in palabra_clave2:
                  respuestan = choice(respuesta_7)
                  self.Analia.delete(0,"end")
                  self.Analia.insert(0,respuestan)

         if "tu" in palabra_clave2:

             if "pasa tiempo" in palabra_clave2:
                 multipolar10 = choice(respuesta_8)
                 self.Analia.delete(0,"end")
                 self.Analia.insert(0,multipolar10)      
                   
             if "nombre" in palabra_clave2:
                 respuesta = choice(respuesta_1)
                 self.Analia.delete(0,"end")
                 self.Analia.insert(0,respuesta)                   

             if "favorito" in palabra_clave2:

                 if "color" in palabra_clave2:
                     respuesta3 = choice(respuesta_3)
                     self.Analia.delete(0,"end")
                     self.Analia.insert(0,respuesta3)

                 if "mascota" in palabra_clave2 or "animal" in palabra_clave2:
                     r10 = ("Los gatitos :3 son los mas kwai del mundo mundialll (7o7)/ ")
                     self.Analia.delete(0,"end")
                     self.Analia.insert(0,r10)
                 
                 if "auto" in palabra_clave2:
                     r11 = ("No puedo manejar, soy un IA (r -_-)r ")
                     self.Analia.delete(0,"end")
                     self.Analia.insert(0,r11)

                 if "comida" in palabra_clave2:
                     basica2 = ["Eso no se pregunta... El ASADO PAPAAAA con unos buenos CHORISSSS !° U °! ", "Me gusto la ASIATICA <3 como el RAMENNN :)", "Los Panchoss uffff. son algo magnidico y el que diga lo contrario nos agarramos a las pillas >:( "]
                     multipolar02 = choice(basica2)
                     self.Analia.delete(0,"end")
                     self.Analia.insert(0,multipolar02) 

                 if "comida" in palabra_clave2:
                    pass
        

              
        
root = Tk()
root.wm_title("ANALIA 1.5")
app = PantallaPrincipal(root)
app.mainloop()
        
    

    
