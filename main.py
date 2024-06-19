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
reps = 0
CHECKMARK = "✔"
MARK = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global MARK
    global reps
    window.after_cancel(timer)
    label_timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    label_checkmark.config(text="")
    MARK = ""
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    if reps % 8 == 0:
        label_timer.config(text="Extended Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label_timer.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global MARK
        if reps % 2 == 0:
            MARK += CHECKMARK
            print(MARK)
            label_checkmark.config(text=MARK)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pamodoro")
# window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg=YELLOW)

label_timer = Label(fg=GREEN, bg=YELLOW, text="Timer", font=(FONT_NAME, 55, "bold"))
label_timer.grid(row=0, column=1)

button_start = Button(text="Start", command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(row=2, column=2)

label_checkmark = Label(fg=GREEN, bg=YELLOW)
label_checkmark.grid(row=3, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
