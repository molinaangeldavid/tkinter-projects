
# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import * 
import math
import pygame
PURPLE = '#502064'
ORANGE = "#F14A16"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
ok_emoji = '✔'
part = 0
loop_timer = None
pygame.mixer.init()



# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    screen.after_cancel(loop_timer)
    timer.config(text='TIMER', font=(FONT_NAME,30,'bold'),fg=RED,bg=YELLOW)
    check['text'] = ''
    canvas.itemconfig(timer_text,text='00:00')

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def play_break():
    pygame.mixer.music.load('rest.mp3')
    pygame.mixer.music.play()

def play_alarm():
    pygame.mixer.music.load('alarm_5.mp3')
    pygame.mixer.music.play()

def st_timer():
    
    
    # time_rest = SHORT_BREAK_MIN *60
    # time_work =  WORK_MIN *60
    # time_long_rest = LONG_BREAK_MIN * 60
    time_rest = 5
    time_work =  10
    time_long_rest = 8
    
    
    global part
    part += 1
    if part == 8:
        play_break
        timer.config(text='LONG BREAK' ,fg=GREEN)
        count_down(time_long_rest)
    elif part % 2 != 0: 
        play_alarm()
        timer.config(text='WORK',fg=RED)
        count_down(time_work)
    else:
        play_break()
        timer.config(text='BREAK',fg=ORANGE)
        count_down(time_rest)
        if part >= 2:
            check['text'] += f'{ok_emoji}  '
    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    min_timer = math.floor(count / 60)
    sec_timer = count % 60
    if sec_timer < 10:
        sec_timer = f'0{sec_timer}'    
    
    canvas.itemconfig(timer_text,text=f'{min_timer}:{sec_timer}')
    if count > 0:
        global loop_timer
        loop_timer = screen.after(1000,count_down,count-1)
    else:
        st_timer()    


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title('Pomodoro')
screen.configure(bg=YELLOW,padx=100,pady=100)

timer = Label(text='TIMER', font=(FONT_NAME,30,'bold'),fg=RED,bg=YELLOW)
timer.grid(row=0,column=1)

canvas = Canvas(width=203,height=224,bg=YELLOW,highlightthickness=0)
imag = PhotoImage(file='tomato.png')
canvas.create_image(103,112,image=imag)
timer_text = canvas.create_text(103,130,text='00:00',font=(FONT_NAME,33,'bold'),fill='white')
canvas.grid(row=1,column=1)

start = Button(text='Start',highlightthickness=0,command=st_timer)
start.grid(row=2,column=0)

reset = Button(text='Reset',highlightthickness=0,command=reset_timer)
reset.grid(row=2,column=2)

check = Label(bg=YELLOW,fg=PURPLE,padx=10,font=(20))
check.grid(row=3,column=1)



screen.mainloop()






