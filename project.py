from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
import pymysql
from pymysql import *



def salvar():
    connection = pymysql.connect(host='localhost', user='root', password='', db='test')
    if connection:
        print("Conectado!\n")

    cursor = connection.cursor()
    try:
        cursor.execute ("INSERT INTO equipamentos (Numero_Patrimonio,Tipo_Equipamento,Valor ) VALUES ("+str(editnumero.get()) 
        +",'" + edittipo.get() + editvalor.get() + "','")
        print("Comando executado!\n")

        connection.commit()
        showinfo(title='Cadastro com sucesso', message="Cadastro com sucesso")
    except MySQLError as erro:
        print("Algum erro aconteceu\n")
        print(erro)

    connection.close()
    print("conexao fechada!\n")


window = Tk()

lbl1 = Label(window, text="Numero de patrimonio")
lbl1.grid(column=0, row=0)

lbl2 = Label(window, text="Tipo de equipamento (impressora ou computador)")
lbl2.grid(column=0, row=2)

lbl3 = Label(window, text="Valor")
lbl3.grid(column=0, row=4)





editnumero = tk.Entry(window, width=20, textvariable='Digite o numero de patrimonio')
editnumero.grid(column=1, row=3, padx=20)


edittipo = tk.Entry(window, width=20, textvariable='Digite o tipo de equipamento')
edittipo.grid(column=1, row=1, padx=20)


editvalor = tk.Entry(window, width=20, textvariable='Digite o valor')
editvalor.grid(column=1, row=0, padx=20)


btn = Button(window, text="Salvar", command=salvar)
btn.grid(column=1, row=6)

window.geometry('500x500')


window.mainloop()

