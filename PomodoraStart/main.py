from cProfile import label
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
i=1
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global i
    i += 1

    if i==8:

        count_down(LONG_BREAK_MIN*60)
        TimerText.config( text="Break", fg=RED)
    elif i%2==0:
        count_down(SHORT_BREAK_MIN*60)
        TimerText.config( text="Break", fg=PINK)
    else:
        count_down(WORK_MIN*60)
        TimerText.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec==0:
        count_sec="00"
    elif count_sec<10:
        count_sec="0"+str(count_sec)
    canva.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:

        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50,bg=YELLOW)

window.after(1000 )

TimerText=Label(window,text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,))
TimerText.grid(column=1,row=0)

canva=Canvas(window, width=200, height=224,bg=YELLOW,highlightthickness=0)
photoImage=PhotoImage(file="tomato.png")
canva.create_image(100,112,image=photoImage)
timer_text=canva.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canva.grid(row=1,column=1)


## Creating start button
button1=Button(window,text="Start ",command=start_timer,highlightthickness=0)
button1.grid(column=0, row=2)



button2=Button(window,text="Reset ",command="",highlightthickness=0)
button2.grid(column=2, row=2)


tick=Label(window,text="✔",fg=GREEN,bg=YELLOW,font=(FONT_NAME,20))
tick.grid(column=1,row=3)






window.mainloop()