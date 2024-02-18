from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
reps=0
showtimer=None
already_start=False
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(showtimer)
    canvas.itemconfig(timer_text,text="00:00")
    timer.config(text="TIMER")
    check.config(text="")
    global reps
    global already_start
    already_start=False
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    if not already_start:
        start_timer()

def start_timer():
    global reps
    global already_start
    already_start=True
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60


    reps+=1
    if(reps%2!=0):
        timer.config(text="WORK", fg=GREEN)
        window.bell()
        count_down(work_sec)
    elif(reps%8==0):
        timer.config(text="BREAK", fg=RED)
        count_down(long_break_sec)
    else:
        timer.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_second=count%60

    if count_second<10:
        count_second=f"0{count_second}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_second}")
    if count>0:
        global showtimer
        showtimer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        no_checks=math.floor(reps/2)
        checktext=""
        for _ in range(no_checks):
            checktext+="✔ "
            
        check.config(text=checktext)

 


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("TOMATO")
window.config(padx=100,pady=50,bg=YELLOW)


canvas=Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white" , font=(FONT_NAME,35,"bold"))

canvas.grid(row=1,column=1)


timer=Label(text="Timer", fg=GREEN,bg=YELLOW,font=(FONT_NAME,40,"bold"))
timer.grid(row=0,column=1)

start=Button(text="Start",highlightthickness=0,command=start)
start.grid(row=2,column=0)

reset=Button(text="Reset",highlightthickness=0,command=reset)
reset.grid(row=2,column=2)

check=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
check.grid(row=3,column=1)

window.mainloop()