score = 0
score1 = 0

def windowI():
    import tkinter as tk
    window8.destroy()

    def selection():
        global score
        global score1
        selected = "you have selected an option, proceed to next"
        label.config(text=selected)
        if str(radio.get()) == "correct choice":
            score += 10
            print("Correct!Your final score is=", score)
            score1 = score
            print("YOUR TOTAL SCORE IS=", score1)
            val1 = (score1)
            string1 = "INSERT INTO QUIZDATA(NAME,AGE,SCORE) VALUES(%s,%s,%s)"
            val = (Name, age, val1)
            print(Name)
            print(score)
            print(age)
            mycursor.execute(string1, val)
            mydb.commit()

        else:
            score += 0
            print("Wrong!Your final score is=", score)
            score1 = score
            print("YOUR TOTAL SCORE IS=", score1)

    global window9
    window9=Tk()
    radio=StringVar()
    window9.title("questionairre")
    window9["background"]="white"
    lbl = Label(window9, text="Question 10 of 10", font=("Arial",15),background="white").pack()

    lbl1 = Label(window9, text="Q.10 Which chess player has the highest rating in chess ", font=("Arial",25),background="cyan", compound=LEFT).pack()

    R1=Radiobutton(window9, text="Vishwanathananand", font=("Arial",20),background="White",
                         variable=radio, value="Wrong choice", command=selection).pack(anchor=NW)
    R2 =Radiobutton(window9, text="Garry kasparov", font=("Arial", 20),background="White",
                         variable=radio, value="wrong option", command=selection).pack(anchor=NW)
    R3 =Radiobutton(window9, text="vladimir kramnink", font=("Arial", 20),background="White",
                         variable=radio, value="incorrect choice", command=selection).pack(anchor=NW)
    R4 =Radiobutton(window9, text="Magnus Carlsen", font=("Arial", 20),background="White",
                         variable=radio, value="correct option", command=selection).pack(anchor=NW)

    label = Label(window9)
    label.pack()

    B1 = Button(window9, text="Next", font=("Helvetica",12)).pack()
    window9.mainloop()


def windowH():
    import tkinter as tk
    window7.destroy()
    def selection():
        global score
        selected = "you have selected" + str(radio.get())
        label.config(text=selected)
        if str(radio.get()) == "correct choice":
            score += 10
            print(score)
        else:
            score += 0
            print(score)


    global window8
    window8 = Tk()
    radio = StringVar()
    window8.title("questionairre")
    window8["background"] = "white"

    lbl = Label(window8, text="Question 9 of 10", font=("Arial",15),background="white").pack
    lbl1=Label(window8,text="Q9.Which sport does not use the term ring?",font=("Arial",25),background="cyan",compound=LEFT).pack()

    R1 = Radiobutton(window8, text="Boxing", font=("Arial",20),background="white",
                     variable=radio, value="Wrong choice", command=selection).pack(anchor=NW)
    R2 = Radiobutton(window8, text="Gymnastics", font=("Arial",20),background="white",
                     variable=radio, value="wrong option", command=selection).pack(anchor=NW)
    R3 = Radiobutton(window8, text="Icehockey", font=("Arial",20),background="white",
                     variable=radio, value="incorrect choice", command=selection).pack(anchor=NW)
    R4 = Radiobutton(window8, text="Baseball", font=("Arial",20),background="white",
                     variable=radio, value="correct option", command=selection).pack(anchor=NW)

    label = Label(window8)
    label.pack()

    B1 = Button(window8, text="Next", font=("Helvetica",12),command=windowI).pack()
    window8.mainloop()



def windowG():
    import tkinter as tk
    window6.destroy()
    def selection():
        global score
        selected="you have selected"+str(radio.get())
        label.config(text=selected)
        if str(radio.get())=="correct choice":
            score+=10
            print(score)
        else:
            score+=0
            print(score)
    global window7
    window7=Tk()
    radio=StringVar()
    window7.title("questionairre")
    window7["background"]="white"
    lbl=Label(window7,text="Question 8 of 10",font=("Arial",15),
    background="White").pack()

    lbl1=Label(window7,text="Q.8 When was the SportAccord renamed as the GASIF?",
    font=("Arial",25),background="cyan",compound=LEFT).pack()

    R1=Radiobutton(window7,text=2005,font=("Arial",20),background="White",
    variable=radio,value="wrong choice",command=selection).pack(anchor=NW)
    R2=Radiobutton(window7,text=2017,font=("Arial",20),background="White",
    variable=radio,value="correct option",command=selection).pack(anchor=NW)
    R3=Radiobutton(window7,text=2016,font=("Arial",20),background="White",
    variable=radio,value="incorrect choice",command=selection).pack(anchor=NW)
    R4=Radiobutton(window7,text=2010,font=("Arial",20),background="White",
    variable=radio,value="wrong option",command=selection).pack(anchor=NW)

    label=Label(window7)
    label.pack()

    B1=Button(window7,text="Next",font=("Helvetica",12),command=windowH).pack()
    window7.mainloop()


def windowF():
    import tkinter as tk
    window5.destroy()

    def selection():
        global score
        selected = "you have selected" + str(radio.get())
        label.config(text=selected)
        if str(radio.get()) == "correct choice":
            score += 10
            print(score)
        else:
            score += 0
            print(score)


    global window6
    window6 = Tk()
    radio = StringVar()
    window6.title("questionairre")
    window6["background"] = "white"
    lbl = Label(window6, text="Question 7 of 10", font=("Arial", 15), background="White").pack()

    lbl1 = Label(window6, text="Q.7 Which cricket team won the 2019-2020 Vijay Hazare Trophy?", font=("Arial",25), background="cyan",
                 compound=LEFT).pack()

    R1 = Radiobutton(window6, text="Karnataka", font=("Arial", 20), background="White",
                     variable=radio, value="Correct option", command=selection).pack(anchor=NW)
    R2 = Radiobutton(window6, text="Himachal Pradesh", font=("Arial",20), background="White",
                     variable=radio, value="wrong choice", command=selection).pack(anchor=NW)
    R3 = Radiobutton(window6, text="Maharahstra", font=("Arial",20), background="White",
                     variable=radio, value="wrong option", command=selection).pack(anchor=NW)
    R4 = Radiobutton(window6, text="Delhi", font=("Arial",20), background="White",
                     variable=radio, value="incorrect choice", command=selection).pack(anchor=NW)

    label = Label(window6)
    label.pack()

    B1 = Button(window6, text="Next", font=("Helvetica",12),command=windowG).pack()
    window6.mainloop()

def windowE():
    import tkinter as tk
    window4.destroy()

    def selection():
        global score
        selected = "you have selected" + str(radio.get())
        label.config(text=selected)
        if str(radio.get()) == "correct choice":
            score += 10
            print(score)
        else:
            score += 0
            print(score)


    global window5
    window5 = Tk()
    radio = StringVar()
    window5.title("questionairre")
    window5["background"] = "white"


    lbl=Label(window5,text="Question 6 of 10",font=("Arial",15),
    background="White").pack()

    lbl1=Label(window5,text="Q.6 Which cricket team won the semifinals but lost in the finals of the world cup 2019?",
    font=("Arial",25),background="cyan",compound=LEFT).pack()

    R1=Radiobutton(window5,text="India",font=("Arial",20),background="White",
    variable=radio,value="Wrong choice",command=selection).pack(anchor=NW)
    R2=Radiobutton(window5,text="Australia",font=("Arial",20),background="White",
    variable=radio,value="wrong option",command=selection).pack(anchor=NW)
    R3=Radiobutton(window5,text="Newzealand",font=("Arial",20),background="White",
    variable=radio,value="correct option",command=selection).pack(anchor=NW)
    R4=Radiobutton(window5,text="England",font=("Arial",20),background="White",
    variable=radio,value="incorrect choice",command=selection).pack(anchor=NW)

    label=Label(window5)
    label.pack()

    B1=Button(window5,text="Next",font=("Helvetica",12),command=windowF).pack()
    window5.mainloop()

def windowD():
    import tkinter as tk
    window3.destroy()

    def selection():
        global score
        selected = "you have selected" + str(radio.get())
        label.config(text=selected)
        if str(radio.get()) == "correct choice":
            score += 10
            print(score)
        else:
            score += 0
            print(score)


    global window4
    window4 = Tk()
    radio = StringVar()
    window4.title("questionairre")
    window4["background"] = "white"

    lbl=Label(window4,text="Question 5 of 10",font=("Arial",15),
    background="White").pack()

    lbl1=Label(window4,text="Q.5 Which player is given the title of the flying sikh?",
    font=("Arial",25),background="cyan",compound=LEFT).pack()

    R1=Radiobutton(window4,text="Milkha Singh",font=("Arial",20),background="White",
    variable=radio,value="correct option",command=selection).pack(anchor=NW)
    R2=Radiobutton(window4,text="Bahadur Singh Chauhan",font=("Arial",20),background="White",
    variable=radio,value="wrong choice",command=selection).pack(anchor=NW)
    R3=Radiobutton(window4,text="Kamaljeet Sandhu",font=("Arial",20),background="White",
    variable=radio,value="wrong option",command=selection).pack(anchor=NW)
    R4=Radiobutton(window4,text="Harmanpreet singh",font=("Arial",20),background="White",
    variable=radio,value="incorrect choice",command=selection).pack(anchor=NW)

    label=Label(window4)
    label.pack()

    B1=Button(window4,text="Next",font=("Helvetica",12),command=windowE).pack()
    window4.mainloop()

def windowC():
    import tkinter as tk
    window2.destroy()

    def selection():
        global score
        selected = "you have selected" + str(radio.get())
        label.config(text=selected)
        if str(radio.get()) == "correct choice":
            score += 10
            print(score)
        else:
            score += 0
            print(score)


    global window3
    window3 = Tk()
    radio = StringVar()
    window3.title("questionairre")
    window3["background"] = "white"

    lbl=Label(window3,text="Question 4 of 10",font=("Arial",15),
    background="White").pack()

    lbl1=Label(window3,text="Q.4 Who was the first cricketer who smacked 6 sixers in an over?",
    font=("Arial",25),background="cyan",compound=LEFT).pack()


    R1=Radiobutton(window3,text="Garry sobers",font=("Arial",20),background="White",
    variable=radio,value="correct option",command=selection).pack(anchor=NW)
    R2=Radiobutton(window3,text="Yuvraj singh",font=("Arial",20),background="White",
    variable=radio,value="wrong choice",command=selection).pack(anchor=NW)
    R3=Radiobutton(window3,text="kireon Pollard",font=("Arial",20),background="White",
    variable=radio,value="wrong option",command=selection).pack(anchor=NW)
    R4=Radiobutton(window3,text="Stuard Broad",font=("Arial",20),background="White",
    variable=radio,value="incorrect choice",command=selection).pack(anchor=NW)

    label=Label(window3)
    label.pack()

    B1=Button(window3,text="Next",font=("Helvetica",12),command=windowD).pack()
    window3.mainloop()


def windowB():
    import tkinter as tk
    window1.destroy()

    def selection():
        global score
        selected = "you have selected" + str(radio.get())
        label.config(text=selected)
        if str(radio.get()) == "correct choice":
            score += 10
            print(score)
        else:
            score += 0
            print(score)


    global window2
    window2 = Tk()
    radio = StringVar()
    window2.title("questionairre")
    window2["background"] = "White"
    lbl = Label(window2,text="Question 3 of 10",font=("Arial", 15),
                background="white").pack()


    lbl1=Label(window2,text="Q.3 Which batsmen has the highest rating in T20 cricket",font=("Arial",25),background="Cyan",compound=LEFT).pack()

    R1=Radiobutton(window2,text="Babar azam",font=("Arial",20),background="White",
    variable=radio,value="wrong choice",command=selection).pack(anchor=NW)
    R2=Radiobutton(window2,text="Sachin Tendulkar",font=("Arial",20),background="White",
    variable=radio,value="wrong option",command=selection).pack(anchor=NW)
    R3=Radiobutton(window2,text="Dawid Malan",font=("Arial",20),background="White",
    variable=radio,value="correct option",command=selection).pack(anchor=NW)
    R4=Radiobutton(window2,text="Virat kohli",font=("Arial",20),background="White",
    variable=radio,value="incorrect choice",command=selection).pack(anchor=NW)

    label=Label(window2)
    label.pack()

    B1=Button(window2,text="Next",font=("Helvetica",12),command=windowC).pack()
    window2.mainloop()

def windowA():
    import tkinter as tk
    window.destroy()

    def selection():
        global score
        selected = "you have selected" + str(radio.get())
        label.config(text=selected)
        if str(radio.get()) == "correct choice":
            score += 10
            print(score)
        else:
            score += 0
            print(score)


    global window1
    window1 = Tk()
    radio = StringVar()
    window1.title("questionairre")
    window1["background"] = "white"

    lbl=Label(window1,text="Question 2 of 10",font=("Arial",15),
    background="White").pack()

    lbl1=Label(window1,text="Q.2 Which football club does David Beckham play for?",
    font=("Arial",25),background="cyan",compound=LEFT).pack()

    R1=Radiobutton(window1,text="Manchester united",font=("Arial",20),background="White",
    variable=radio,value="wrong choice",command=selection).pack(anchor=NW)
    R2=Radiobutton(window1,text="Liverpool",font=("Arial",20),background="White",
    variable=radio,value="wrong option",command=selection).pack(anchor=NW)
    R3=Radiobutton(window1,text="Real Madrid",font=("Arial",20),background="White",
    variable=radio,value="correct option",command=selection).pack(anchor=NW)
    R4=Radiobutton(window1,text="Montevideo Wanderers",font=("Arial",20),background="White",
    variable=radio,value="incorrect choice",command=selection).pack(anchor=NW)

    label=Label(window1)
    label.pack()

    B1=Button(window1,text="Next",font=("Helvetica",12),command=windowB).pack()
    window1.mainloop()

def Questions():
    import tkinter as tk  # imports the tkinter module of python which is a GUI
    from tkinter import Label

    def selection():
        global score
        selected = "you have selected" + str(radio.get())
        label.config(text=selected)
        if str(radio.get()) == "correct choice":
            score += 10
            print(score)
        else:
            score += 0
            print(score)
    window = Tk()
    radio = StringVar()
    window.title("questionairre")
    window["background"] = "white"
    lbl=Label(window,text="Question 1 of 10",font=("Arial",15),
    background="White").pack()

    lbl1=Label(window,text="Q.1 Where were the 2002 worldcup fnals held?",
    font=("Arial",25),background="cyan",compound=LEFT).pack()

    R1=Radiobutton(window,text="Japan and Korea",font=("Arial",20),background="White",
    variable=radio,value="correct option",command=selection).pack(anchor=NW)
    R2=Radiobutton(window,text="Germany",font=("Arial",20),background="White",
    variable=radio,value="wrong choice",command=selection).pack(anchor=NW)
    R3=Radiobutton(window,text="Scotland",font=("Arial",20),background="White",
    variable=radio,value="wrong option",command=selection).pack(anchor=NW)
    R4=Radiobutton(window,text="Colombia",font=("Arial",20),background="White",
    variable=radio,value="incorrect choice",command=selection).pack(anchor=NW)

    label=Label(window)
    label.pack()

    B1=Button(window,text="Next",font=("Helvetica",12),background="cyan",command=windowA).pack()
    window.mainloop()

from tkinter import *
import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    charset="utf8",
    passwd="1234",
    auth_plugin='mysql_native_password',
    database="Quiz")
mycursor = mydb.cursor()

window = Tk()


def check():
    global Name
    global age
    Name = Namefield.get()
    age = int(variable1.get())
    print(Name)
    print(score)
    print(age)
    Questions()


window.title("Player Info")
window['background'] = "White"
var1 = StringVar(window)
lbl1 = Label(window, text="Before We Begin:", font=("Arial", 30), background="cyan", compound=CENTER)
lbl1.pack(anchor=NW)
lbl3 = Label(window, text="Enter your Name:", font=("Arial", 20), background="White", compound=CENTER)
lbl3.pack(anchor=W)
Namefield = Entry()
Namefield.pack(anchor=NE)
lbl2 = Label(window, text="Enter your Age:", font=("Arial", 20), background="White", compound=CENTER)
lbl2.pack(anchor=W)
qty_list = ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
variable1 = StringVar(window)
variable1.set(qty_list[12])
field1 = OptionMenu(window, variable1, *qty_list)
field1.pack(anchor=NE)
B1 = Button(window, text="Finish", font=("Arial", 15), command=check, compound=CENTER)
B1.pack(anchor=S)


mydb.commit()
window.mainloop()