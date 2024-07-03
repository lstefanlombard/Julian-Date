from tkinter import *
import juliandate as jd
import datetime

# Initial values for global variables
jjjj = 0
MM = 0
dd = 0
hh = 0
mm = 0
ss = 0
ms = 0

def jd2date():
    global jjjj, MM, dd, hh, mm, ss, ms
    juliandate = float(F_JD.get())
    date_tuple = jd.to_gregorian(juliandate)
    date_obj = datetime.datetime(*date_tuple)

    jjjj = date_obj.year
    MM = date_obj.month
    dd = date_obj.day
    hh = date_obj.hour
    mm = date_obj.minute
    ss = date_obj.second
    ms = date_obj.microsecond // 1000  # Convert microseconds to milliseconds

    F_Year.delete(0, END)
    F_Month.delete(0, END)
    F_Day.delete(0, END)
    F_Hour.delete(0, END)
    F_Minutes.delete(0, END)
    F_seconds.delete(0, END)
    F_Mseconds.delete(0, END)

    F_Year.insert(0, jjjj)
    F_Month.insert(0, MM)
    F_Day.insert(0, dd)
    F_Hour.insert(0, hh)
    F_Minutes.insert(0, mm)
    F_seconds.insert(0, ss)
    F_Mseconds.insert(0, ms)

def date2jd():
    jjjj = int(F_Year.get())
    MM = int(F_Month.get())
    dd = int(F_Day.get())
    hh = int(F_Hour.get())
    mm = int(F_Minutes.get())
    ss = int(F_seconds.get())
    ms = int(F_Mseconds.get())
    F_JD.delete(0, END)
    juliandate = jd.from_gregorian(jjjj, MM, dd, hh, mm, ss + ms / 1000)
    F_JD.insert(0, juliandate)

def now2jd():
    clear_date()
    now = datetime.datetime.utcnow()
    jjjj = now.year
    MM = now.month
    dd = now.day
    hh = now.hour
    mm = now.minute
    ss = now.second
    ms = 0

    F_Year.insert(0, jjjj)
    F_Month.insert(0, MM)
    F_Day.insert(0, dd)
    F_Hour.insert(0, hh)
    F_Minutes.insert(0, mm)
    F_seconds.insert(0, ss)
    F_Mseconds.insert(0, ms)

    juliandate = jd.from_gregorian(jjjj, MM, dd, hh, mm, ss + ms / 1000)
    F_JD.insert(0, juliandate)

def clear_date():
    F_Year.delete(0, END)
    F_Month.delete(0, END)
    F_Day.delete(0, END)
    F_Hour.delete(0, END)
    F_Minutes.delete(0, END)
    F_seconds.delete(0, END)
    F_Mseconds.delete(0, END)
    F_JD.delete(0, END)

root = Tk()
root.title("Julian Date Converter")

frame1 = Frame(root, padx=10, pady=10)
frame1.grid(row=0, column=0, sticky=W)

LB_Year = Label(frame1, text="Year")
LB_Year.grid(row=0, column=0)

F_Year = Entry(frame1, width=6)
F_Year.grid(row=1, column=0, padx=5, pady=5)

LB_Month = Label(frame1, text="Month")
LB_Month.grid(row=0, column=1)

F_Month = Entry(frame1, width=4)
F_Month.grid(row=1, column=1, padx=5, pady=5)

LB_Day = Label(frame1, text="Day")
LB_Day.grid(row=0, column=2)

F_Day = Entry(frame1, width=4)
F_Day.grid(row=1, column=2, padx=5, pady=5)

LB_Hour = Label(frame1, text="Hour")
LB_Hour.grid(row=0, column=3)

F_Hour = Entry(frame1, width=4)
F_Hour.grid(row=1, column=3, padx=5, pady=5)

LB_Minutes = Label(frame1, text="Minutes")
LB_Minutes.grid(row=0, column=4)

F_Minutes = Entry(frame1, width=4)
F_Minutes.grid(row=1, column=4, padx=5, pady=5)

LB_seconds = Label(frame1, text="Seconds")
LB_seconds.grid(row=0, column=5)

F_seconds = Entry(frame1, width=4)
F_seconds.grid(row=1, column=5, padx=5, pady=5)

LB_Mseconds = Label(frame1, text="Milliseconds")
LB_Mseconds.grid(row=0, column=6)

F_Mseconds = Entry(frame1, width=6)
F_Mseconds.grid(row=1, column=6, padx=5, pady=5)

frame2 = Frame(root, padx=10, pady=10)
frame2.grid(row=1, column=0, sticky=W)

LB_JD = Label(frame2, text="Julian Date")
LB_JD.grid(row=0, column=0, pady=5)

F_JD = Entry(frame2, width=30)
F_JD.grid(row=0, column=1, columnspan=2, pady=5)

frame3 = Frame(root, padx=10, pady=10)
frame3.grid(row=2, column=0, sticky=W)

BTN_Now = Button(frame3, text="Now", command=now2jd,bg="lime")
BTN_Now.grid(row=0, column=0, padx=5, pady=5)

BTN_Calc_JD = Button(frame3, text="Calculate JD", command=date2jd, bg="aqua")
BTN_Calc_JD.grid(row=0, column=1, padx=5, pady=5)

BTN_Calc_D = Button(frame3, text="Calculate Date", command=jd2date, bg="Violet")
BTN_Calc_D.grid(row=0, column=2, padx=5, pady=5)

BTN_clear = Button(frame3, text="Clear", command=clear_date, bg='red',)
BTN_clear.grid(row=0, column=3, padx=5, pady=5)

root.mainloop()

