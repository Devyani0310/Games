
import tkinter as tk 
hr,min,sec = 00,00,00
tim = f"{hr:02} : {min:02} : {sec:02}"
state = False
root = tk.Tk()

txt = tk.Label(root,text=tim)
but_frame = tk.Frame(root)
but_stop = tk.Button(but_frame,text = "STOP")
but_start = tk.Button(but_frame,text = "START")
but_reset = tk.Button(but_frame,text = "RESET")
xt = tk.Button(root,text="EXIT")

def reset():
    global hr,min,sec,state
    hr,min,sec = 00,00,00
    tim = f"{hr:02} : {min:02} : {sec:02}"
    txt.config(text = tim)
    state = False

def start():
    global state
    state = True
    counting()

def counting():
    global hr,min,sec,state
    if state==False:
        return
    sec += 1
    if sec==60:
        min+=1
        sec=0
        if min==60:
            min=0
            hr+=1
    tim = f"{hr:02} : {min:02} : {sec:02}"
    txt.config(text = tim)
    root.after(1000,counting)

def stop():
    global state
    state = False

txt.config(font=("Times", 15, "bold"), width=30, fg='#eeeeee', bg='#123456',height=5, )
but_frame.config(width=30,bg="#ffeeee",height=10)
but_start.config(font=("Times",6),height=4,width=17, \
    bg='#eeeeee', fg='#123456',command = start)
but_stop.config(font=("Times",6),height=4,width=17, \
    bg='#eeeeee', fg='#123456', command = stop)
but_reset.config(font=("Times",6),height=4,width=17, \
    bg='#eeeeee', fg='#123456',command = reset)
xt.config(font=("Times",6),height=4,width=20, \
    fg='#eeeeee', bg='#123456',command=root.quit)

txt.pack(fill=tk.BOTH)
but_frame.pack(fill=tk.BOTH)
but_stop.pack(side="left",fill=tk.BOTH,pady=3,padx=3)
but_reset.pack(side="left",fill=tk.BOTH,pady=3,padx=3)
but_start.pack(side="left",fill=tk.BOTH,pady=3,padx=3)
xt.pack(side=tk.BOTTOM,fill=tk.BOTH)

root.title("Stopwatch")
root.minsize(300,220)
root.maxsize(300,220)
root.mainloop()