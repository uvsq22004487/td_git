def appui_touche0():
        canvas.create_text(300, 100, text="0", fill="red", font=("Times","25"))

def appui_touche1():
        canvas.create_text(300, 100, text="1", fill="red", font=("Times","25"))

def appui_touche2():
        canvas.create_text(300, 100, text="2", fill="red", font=("Times","25"))

def appui_touche3():
        canvas.create_text(300, 100, text="3", fill="red", font=("Times","25"))

def appui_touche4():
        canvas.create_text(300, 100, text="4", fill="red", font=("Times","25"))

def appui_touche5():
        canvas.create_text(300, 100, text="5", fill="red", font=("Times","25"))

def appui_touche6():
        canvas.create_text(300, 100, text="6", fill="red", font=("Times","25"))

def appui_touche7():
        canvas.create_text(300, 100, text="7", fill="red", font=("Times","25"))

def appui_touche8():
        canvas.create_text(300, 100, text="8", fill="red", font=("Times","25"))

def appui_touche9():
        canvas.create_text(300, 100, text="9", fill="red", font=("Times","25"))

def appui_toucheplus():
        canvas.create_text(300, 100, text="+", fill="red", font=("Times","25"))

def appui_touchemoins():
        canvas.create_text(300, 100, text="-", fill="red", font=("Times","25"))

def appui_touchefois():
        canvas.create_text(300, 100, text="*", fill="red", font=("Times","25"))

def appui_touchediv():
        canvas.create_text(300, 100, text="/", fill="red", font=("Times","25"))

def appui_touchevirgule():
        canvas.create_text(300, 100, text=".", fill="red", font=("Times","25"))

import tkinter as tk 

HEIGHT =100
WIDTH = 300


racine = tk.Tk()
racine.title("Calculatrice")
canvas = tk.Canvas(racine, bg="grey", height=HEIGHT, width=WIDTH, relief="raised", borderwidth=15)
canvas.grid(row=1, column=1, columnspan=5)
bouton0 = tk.Button(racine, text="0",font = ("Times", "15"), command=appui_touche0)
bouton0.grid(row=9, column=2)
bouton1 = tk.Button(racine, text="1",font = ("Times", "15"), command=appui_touche1)
bouton1.grid(row=8, column=1)
bouton2 = tk.Button(racine, text="2",font = ("Times", "15"), command=appui_touche2)
bouton2.grid(row=8, column=2)
bouton3 = tk.Button(racine, text="3",font = ("Times", "15"), command=appui_touche3)
bouton3.grid(row=8, column=3)
bouton4 = tk.Button(racine, text="4",font = ("Times", "15"), command=appui_touche4)
bouton4.grid(row=7, column=1)
bouton5 = tk.Button(racine, text="5",font = ("Times", "15"), command=appui_touche5)
bouton5.grid(row=7, column=2)
bouton6 = tk.Button(racine, text="6",font = ("Times", "15"), command=appui_touche6)
bouton6.grid(row=7, column=3)
bouton7 = tk.Button(racine, text="7",font = ("Times", "15"), command=appui_touche7)
bouton7.grid(row=6, column=1)
bouton8 = tk.Button(racine, text="8",font = ("Times", "15"), command=appui_touche8)
bouton8.grid(row=6, column=2)
bouton9 = tk.Button(racine, text="9",font = ("Times", "15"), command=appui_touche9)
bouton9.grid(row=6, column=3)
boutonplus = tk.Button(racine, text="+",font = ("Times", "15"), command=appui_toucheplus)
boutonplus.grid(row=8, column=4)
boutonmoins = tk.Button(racine, text="-",font = ("Times", "15"), command=appui_touchemoins)
boutonmoins.grid(row=8, column=5)
boutonfois = tk.Button(racine, text="x",font = ("Times", "15"), command=appui_touchefois)
boutonfois.grid(row=7, column=4)
boutondiv = tk.Button(racine, text="/",font = ("Times", "15"), command=appui_touchediv)
boutondiv.grid(row=7, column=5)
boutonegal = tk.Button(racine, text="=",font = ("Times", "15"))
boutonegal.grid(row=9, column=5)
boutonvirgule = tk.Button(racine, text=".",font = ("Times", "15"), command=appui_touchevirgule)
boutonvirgule.grid(row=9, column=4)
boutonsupp = tk.Button(racine, text="del",font = ("Times", "15"))
boutonsupp.grid(row=6, column=5)
racine.mainloop()   
