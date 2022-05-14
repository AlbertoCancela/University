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
hmsLV = tkinter.Label(ventanaLV,text="HH  / MM")
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
while i <= 16:
    if i < 11:
        TBXHoraLV.append(tkinter.Entry(ventanaLV, width=5, justify="center"))
        #TBXHoraLV[i].insert(0,"00")
        TBXHoraLV[i].pack()
        TBXHora.append(tkinter.Entry(ventanaS, width=5, justify="center"))
        #TBXHora[i].insert(0,"00")
        TBXHora[i].pack()
    elif i >=11:
        TBXHoraLV.append(tkinter.Entry(ventanaLV, width=5, justify="center"))
        #TBXHoraLV[i].insert(0,"00")
        TBXHoraLV[i].config(state='disabled')
        TBXHoraLV[i].pack()
        TBXHora.append(tkinter.Entry(ventanaS, width=5, justify="center"))
        #TBXHora[i].insert(0,"00")
        TBXHora[i].config(state='disabled')
        TBXHora[i].pack()
    
    if i<=1:
        TBXHoraLV[i].place(x=px,y=py)
        TBXHora[i].place(x=px,y=py)
        px=px+30
    if i>=2:
        TBXHora[i].place(x=px-90,y=py+30)
        TBXHoraLV[i].place(x=px-90,y=py+30)
        px=px+30
    if i>=4:
        TBXHora[i].place(x=px-210,y=py+60)
        TBXHoraLV[i].place(x=px-210,y=py+60)
    if i>=6:
        TBXHora[i].place(x=px-300,y=py+90)
        TBXHoraLV[i].place(x=px-300,y=py+90)
    if i>=8:
        TBXHora[i].place(x=px-390,y=py+120)
        TBXHoraLV[i].place(x=px-390,y=py+120)
    if i>=10:
        TBXHora[i].place(x=px-480,y=py+150)
        TBXHoraLV[i].place(x=px-480,y=py+150)
    if i>=12:
        TBXHora[i].place(x=px-570,y=py+180)
        TBXHoraLV[i].place(x=px-570,y=py+180)
    if i>=14:
        TBXHora[i].place(x=px-660,y=py+210)
        TBXHoraLV[i].place(x=px-660,y=py+210)
    i = i+1