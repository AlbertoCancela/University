from email.errors import MessageError
from fractions import Fraction
import imp
from logging import root
from pickle import FALSE, TRUE
from pydoc import text
from queue import Empty
from sre_parse import State
from tarfile import FIFOTYPE
import tkinter, serial, time
from tkinter import messagebox
from turtle import onclick, width
from tkinter.tix import NoteBook
from tkinter import BOTH, Y, Checkbutton, Frame, ttk
from datetime import datetime
from tkinter import *

from setuptools import Command
#inicializado
ventana = tkinter.Tk()
ventana.title("Timbre Automatizado")
ventana.iconbitmap("IESPS.ico")
NoteBook = ttk.Notebook(ventana)
NoteBook.pack(pady=15)
ventana.geometry("260x520")
ventana.resizable(0,0)
img = tkinter.PhotoImage(file="IESPS.png")
lbl_img = tkinter.Label(ventana, image=img)
lbl_img.pack()
lbl_img.place(x=80, y=72)
#tabs
ventanaLV = Frame(NoteBook, width=260, height=440)
ventanaS = Frame(NoteBook, width=260, height=440)
NoteBook.add(ventanaLV, text="Escolarizado")
NoteBook.add(ventanaS, text="Sabatino")     
NoteBook.pack(expand=True,fill="both")

#Variables y arreglo de las tbx
TBXHora = []
TBXHoraLV = []
i=0
px=114
py=180
pyc=30
PUERTO="COM11"
#------------------------------------
#Día Semana
weekDayAut=datetime.today().weekday()
weekDayList=["Lunes", "Martes","Miércoles", "Juéves", "Viernes", "Sábado", "Domingo"]
if weekDayAut == 0:
    weekDay=tkinter.Label(text=weekDayList[0])
    weekDay.pack()
    weekDay.place(x=10, y=40)
if weekDayAut == 1:
    weekDay=tkinter.Label(text=weekDayList[1])
    weekDay.pack()
    weekDay.place(x=10, y=40)
if weekDayAut == 2:
    weekDay=tkinter.Label(text=weekDayList[2])
    weekDay.pack()
    weekDay.place(x=10, y=40)
if weekDayAut == 3:
    weekDay=tkinter.Label(text=weekDayList[3])
    weekDay.pack()
    weekDay.place(x=10, y=40)
if weekDayAut == 4:
    weekDay=tkinter.Label(text=weekDayList[4])
    weekDay.pack()
    weekDay.place(x=10, y=40)
if weekDayAut == 5:
    weekDay=tkinter.Label(text=weekDayList[5])
    weekDay.pack()
    weekDay.place(x=10, y=40)
if weekDayAut == 6:
    weekDay=tkinter.Label(text=weekDayList[6])
    weekDay.pack()
    weekDay.place(x=10, y=40)

#-----------------------------------------------------
#Labels
hmsLV = tkinter.Label(ventanaLV,text="       HH  / MM")
hmsLV.pack()
hmsLV.place(x=px, y=py-20)
hms = tkinter.Label(ventanaS,text="HH  / MM")
hms.pack()
hms.place(x=px, y=py-20)
lugarToqueLV=["Primer toque", "Segundo toque", "Tercer toque", "Cuarto toque", "Quinto toque", "Sexto toque", "Séptimo toque", "Octavo toque"]
lugarToqueLV2=["Primer toque", "Segundo toque", "Tercer toque", "Cuarto toque", "Quinto toque", "Sexto toque", "Séptimo toque", "Octavo toque"]

j=0
for j in lugarToqueLV:
    lugarToqueLV[i]=tkinter.Label(ventanaS,text=lugarToqueLV[i])
    lugarToqueLV[i].pack()
    lugarToqueLV2[i]=tkinter.Label(ventanaLV,text=lugarToqueLV2[i])
    lugarToqueLV2[i].pack()
    i+=1
    #Sabatinos
lugarToqueLV[0].place(x=24,y=py)
lugarToqueLV[1].place(x=24,y=py+30)
lugarToqueLV[2].place(x=24,y=py+60)
lugarToqueLV[3].place(x=24,y=py+90)
lugarToqueLV[4].place(x=24,y=py+120)
lugarToqueLV[5].place(x=24,y=py+150)
lugarToqueLV[6].place(x=24,y=py+180)
lugarToqueLV[7].place(x=24,y=py+210)
    #Escolarizados
lugarToqueLV2[0].place(x=24,y=py)
lugarToqueLV2[1].place(x=24,y=py+30)
lugarToqueLV2[2].place(x=24,y=py+60)
lugarToqueLV2[3].place(x=24,y=py+90)
lugarToqueLV2[4].place(x=24,y=py+120)
lugarToqueLV2[5].place(x=24,y=py+150)
lugarToqueLV2[6].place(x=24,y=py+180)
lugarToqueLV2[7].place(x=24,y=py+210)
#---------------------------------------------------
#TextBoxes
i=0 #reiniciar i
while i <= 15:
    if i < 10:
        TBXHoraLV.append(tkinter.Entry(ventanaLV, width=7, justify="center"))
        TBXHoraLV[i].insert(0,"00")
        TBXHoraLV[i].pack()
        TBXHora.append(tkinter.Entry(ventanaS, width=7, justify="center"))
        TBXHora[i].insert(0,"00")
        TBXHora[i].pack()
    elif i >=10:
        TBXHoraLV.append(tkinter.Entry(ventanaLV, width=7, justify="center"))
        TBXHoraLV[i].insert(0,"00")
        TBXHoraLV[i].config(state='disabled')
        TBXHoraLV[i].pack()
        TBXHora.append(tkinter.Entry(ventanaS, width=7, justify="center"))
        TBXHora[i].insert(0,"00")
        TBXHora[i].config(state='disabled')
        TBXHora[i].pack()
    
    if i==0:
        TBXHoraLV[i].place(x=px,y=py)
        TBXHora[i].place(x=px,y=py)
        px=px+45
    if i==1:
        TBXHoraLV[i].place(x=px+5,y=py)
        TBXHora[i].place(x=px+5,y=py)
        px=px+45
    if i>=2:
        TBXHora[i].place(x=px-90,y=py+30)
        TBXHoraLV[i].place(x=px-90,y=py+30)
        px=px+50
    if i>=4:
        TBXHora[i].place(x=px-240,y=py+60)
        TBXHoraLV[i].place(x=px-240,y=py+60)
    if i>=6:
        TBXHora[i].place(x=px-340,y=py+90)
        TBXHoraLV[i].place(x=px-340,y=py+90)
    if i>=8:
        TBXHora[i].place(x=px-440,y=py+120)
        TBXHoraLV[i].place(x=px-440,y=py+120)
    if i>=10:
        TBXHora[i].place(x=px-540,y=py+150)
        TBXHoraLV[i].place(x=px-540,y=py+150)
    if i>=12:
        TBXHora[i].place(x=px-640,y=py+180)
        TBXHoraLV[i].place(x=px-640,y=py+180)
    if i>=14:
        TBXHora[i].place(x=px-740,y=py+210)
        TBXHoraLV[i].place(x=px-740,y=py+210)
    i = i+1
#CheckBoxes && DisableBoxes
def dBxs():
    if (varLV.get()==1):
        TBXHoraLV[10].config(state='normal')
        TBXHoraLV[11].config(state='normal')
    if(var3LV.get()==1):
        TBXHoraLV[14].config(state='normal')
        TBXHoraLV[15].config(state='normal')
    if(var2LV.get()==1):
        TBXHoraLV[12].config(state='normal')
        TBXHoraLV[13].config(state='normal')
    if(varLV.get()==0):
        TBXHoraLV[10].config(state='disabled')
        TBXHoraLV[11].config(state='disabled')
    if(var2LV.get()==0):
        TBXHoraLV[12].config(state='disabled')
        TBXHoraLV[13].config(state='disabled')
    if(var3LV.get()==0):
        TBXHoraLV[14].config(state='disabled')
        TBXHoraLV[15].config(state='disabled')
#-----------Sábado
    if (var.get()==1):
        TBXHora[10].config(state='normal')
        TBXHora[11].config(state='normal')
    if(var3.get()==1):
        TBXHora[14].config(state='normal')
        TBXHora[15].config(state='normal')
    if(var2.get()==1):
        TBXHora[12].config(state='normal')
        TBXHora[13].config(state='normal')
    if(var.get()==0):
        TBXHora[10].config(state='disabled')
        TBXHora[11].config(state='disabled')
    if(var2.get()==0):
        TBXHora[12].config(state='disabled')
        TBXHora[13].config(state='disabled')
    if(var3.get()==0):
        TBXHora[14].config(state='disabled')
        TBXHora[15].config(state='disabled')

varLV = IntVar()
var2LV = IntVar()
var3LV = IntVar()
cb1 = Checkbutton(ventanaLV, variable=varLV, onvalue=1, offvalue=0, command=dBxs)
cb1.pack()
cb1.place(x=210,y=326)
cb2 = Checkbutton(ventanaLV, variable=var2LV, onvalue=1, offvalue=0, command=dBxs)
cb2.pack()
cb2.place(x=210,y=356)
cb3 = Checkbutton(ventanaLV, variable=var3LV, onvalue=1, offvalue=0, command=dBxs)
cb3.pack()
cb3.place(x=210,y=386)

var = IntVar()
var2 = IntVar()
var3 = IntVar()
cb1 = Checkbutton(ventanaS, variable=var, onvalue=1, offvalue=0, command=dBxs)
cb1.pack()
cb1.place(x=210,y=326)
cb2 = Checkbutton(ventanaS, variable=var2, onvalue=1, offvalue=0, command=dBxs)
cb2.pack()
cb2.place(x=210,y=356)
cb3 = Checkbutton(ventanaS, variable=var3, onvalue=1, offvalue=0, command=dBxs)
cb3.pack()
cb3.place(x=210,y=386)
#------------------------------------

def toArduino(prueba):
    #Comprobación de errores
    i=0
    while i<=15:
        if len(TBXHoraLV[i].get()) == 0 or len(TBXHora[i].get()) == 0:
            messagebox.showinfo("Error", "Cuadros sin rellenar")
            return
        i+=1

    
    #Variables a mandar
        #Fragmentos y Horas de horario escolarizado  
    firstLV=(TBXHoraLV[0].get()+":"+TBXHoraLV[1].get())
    secondLV=(TBXHoraLV[2].get()+":"+TBXHoraLV[3].get())
    thirdLV=(TBXHoraLV[4].get()+":"+TBXHoraLV[5].get())
    fourthLV=(TBXHoraLV[6].get()+":"+TBXHoraLV[7].get())
    fiftLV=(TBXHoraLV[8].get()+":"+TBXHoraLV[9].get())
    sixthLV=(TBXHoraLV[10].get()+":"+TBXHoraLV[11].get())
    seventhLV=(TBXHoraLV[12].get()+":"+TBXHoraLV[13].get())
    eighthLV=(TBXHoraLV[14].get()+":"+TBXHoraLV[15].get())
    E_ring= firstLV+":"+secondLV+":"+thirdLV+":"+fourthLV+":"+fiftLV+":"+sixthLV+":"+seventhLV+":"+eighthLV
        #Fragmentos y Horas de horario sabatino
    firstS=(TBXHora[0].get()+":"+TBXHora[1].get())
    secondS=(TBXHora[2].get()+":"+TBXHora[3].get())
    thirdS=(TBXHora[4].get()+":"+TBXHora[5].get())
    fourthS=(TBXHora[6].get()+":"+TBXHora[7].get())
    fiftS=(TBXHora[8].get()+":"+TBXHora[9].get())
    sixthS=(TBXHora[10].get()+":"+TBXHora[11].get())
    seventhS=(TBXHora[12].get()+":"+TBXHora[13].get())
    eighthS=(TBXHora[14].get()+":"+TBXHora[15].get())
    S_ring= firstS+":"+secondS+":"+thirdS+":"+fourthS+":"+fiftS+":"+sixthS+":"+seventhS+":"+eighthS+":"+str(weekDayAut)

    #Trama Esscolarizados
    serialArduino = serial.Serial(PUERTO, 9600)
    time.sleep(2)
    serialArduino.write(E_ring.encode('ascii'))
    String = serialArduino.readline()
    print(String)
    #Trama Sabatinos
    time.sleep(2)
    serialArduino.write(S_ring.encode('ascii'))
    String = serialArduino.readline()
    print(String)
    serialArduino.close()
boton = tkinter.Button(ventana, border=4,text="Insertar toques", command=lambda: toArduino(TBXHora))
boton.pack()
boton.place(x=90,y=460)
ventana.mainloop()