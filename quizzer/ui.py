THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class Uiquizz:
    
    def __init__(self,quizzdata:QuizBrain) -> None:
        self.screen = Tk()
        self.screen.config(bg=THEME_COLOR,padx=20,pady=20)
        
        self.data = quizzdata
        
        self.point = self.data.score
        self.score = Label(text=f'Score: {self.data.score}',bg=THEME_COLOR,fg='#FFF',font=('Arial',16,'bold'))
        self.score.grid(row=0,column=1,padx=20,pady=20,)        
        
        self.quizznote = Canvas(width=400,height=400)
        self.quizztext = self.quizznote.create_text(200,200,width=300,font=('Arial',20,'bold'))
        self.quizznote.grid(row=1,column=0,columnspan=2,pady=20,padx=20)
        
        self.quizznote.config(bg='#fff')
        xbutton_image = PhotoImage(file='images/false.gif')
        self.xbutton = Button(image=xbutton_image,command=self.it_is_false,highlightthickness=0)
        self.xbutton.grid(row=2,column=0,padx=20,pady=20)
        
        yesbutton_image = PhotoImage(file='images/true.gif')
        self.yes_button = Button(image=yesbutton_image,command=self.it_is_true,highlightthickness=0)
        self.yes_button.grid(row=2,column=1,padx=20,pady=20)
        self.get_question()
        
        self.screen.mainloop()
        
    def it_is_false(self):
        is_correct = self.data.check_answer('false')
        self.feedback(is_correct)
        
    def it_is_true(self):
        is_correct = self.data.check_answer('true')
        self.feedback(is_correct)
        
    def feedback(self,is_correct):
        if is_correct == True:
            self.quizznote.config(bg='#47fb00')
            self.screen.after(1000,self.get_question)   
            self.point = self.data.score
        else:
            self.quizznote.config(bg='#ed0103')    
            self.next_question()
    
    def get_question(self):
        self.quizznote.config(bg='#fff')
        if self.data.still_has_questions():
            self.score.config(text=f'Score: {self.data.score}')
            question = self.data.next_question()
            self.quizznote.itemconfig(self.quizztext,text=question)
        else:
            self.quizznote.itemconfig(self.quizztext,text='You answer all the questions succesfully')
            self.xbutton.config(state='disable')    
            self.yes_button.config(state='disable')    
        
        
    def next_question(self):
        self.screen.after(1000,self.get_question)   