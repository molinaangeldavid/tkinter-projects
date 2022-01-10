from tkinter import *
import random
import pandas
import os

FONT_LANGUAGE = ('Arial',25,'normal')
FONT_WORD = ('Arial',35,'bold')
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FILE = 'data/italian.csv'
LANGUAGE_FATHER = "English" ## Always will be English
LANGUAGE_LEARN = "Italian" ## The language that you want to learn
BLACK_COLOR = '#000'
WHITE_COLOR = '#fff'

all_the_traslates = {}
data = {}
on = ''
# ------------------------ OPEN FILE ------------------------------------ #
def open_file():
    global all_the_traslates
    try:
        words = pandas.read_csv('data/word_learn.csv')
    except FileNotFoundError:
        words = pandas.read_csv(LANGUAGE_FILE)
        all_the_traslates = words.to_dict('records')
    else:    
        all_the_traslates = words.to_dict('records')
        
# ------------------------ PICK WORDS ----------------------------------- #
def take_word():
    global data
    data = random.choice(all_the_traslates)

# ------------------------  -----------------------------#
def return_card_white():
    card.itemconfig(card_image,image=card1)
    card.itemconfig(language_card,text=LANGUAGE_LEARN,fill=BLACK_COLOR)
    card.itemconfig(word_card,text=f'{data[LANGUAGE_LEARN]}',fill=BLACK_COLOR)
    
def return_card_blue():
    card.itemconfig(card_image,image=card2)
    card.itemconfig(language_card,text=LANGUAGE_FATHER,fill=WHITE_COLOR)    
    card.itemconfig(word_card,text=f'{data[LANGUAGE_FATHER]}',fill=WHITE_COLOR)

def xfunction():
    global on
    screen.after_cancel(on)
    on = screen.after(3000,return_card_blue)
    take_word()
    return_card_white()

def is_okfunction():
    all_the_traslates.remove(data)
    new_file = pandas.DataFrame(all_the_traslates)
    new_file.to_csv('data/word_learn.csv', index=False)
    xfunction() 

# ------------------------ GUI CREATE ----------------------------------- #
screen = Tk()
screen.config(bg=BACKGROUND_COLOR,padx=100,pady=100)
card = Canvas(width=800,height=600,bg=BACKGROUND_COLOR,highlightthickness=0)
open_file()    
take_word()
card1 = PhotoImage(file='images/card_front.gif')
card2 = PhotoImage(file='images/card_back.gif')
card_image = card.create_image(400,320,image=card1)
language_card = card.create_text(400,200,text=LANGUAGE_LEARN,font=FONT_LANGUAGE)
word_card = card.create_text(400,350,text=f'{data[LANGUAGE_LEARN]}',font=FONT_WORD)
card.grid(row=1,column=0,columnspan=2)
on = screen.after(3000,return_card_blue)
# ---------------------- CREATE BUTTONS -------------------------------- #
nots_ok = PhotoImage(file='images/wrong.gif')
incorrect = Button(width=100,heigh=100,image=nots_ok,command=xfunction)
incorrect.grid(row=2,column=0)

is_ok = PhotoImage(file='images/right.gif')
yes = Button(width=100,height=100,image=is_ok,command=is_okfunction)
yes.grid(row=2,column=1)

screen.mainloop()
