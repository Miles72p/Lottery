import random
import tkinter as tk
from tkinter import Spinbox


def megamillions():
    pool = 0
    pool = [i for i in range(1, 71)] # Pool with numbers from 1 to 70
    sample_numbers = random.sample(pool, 5)
    sample_numbers.sort()
    mega_ball = random.randint(1, 25)
    numbers = '\n  ' + str(sample_numbers) + ' + ' + str(mega_ball) + '\n'
    txt.insert(1.0, numbers)
    print('Mega')


def powerball():
    pool = 0
    pool = [i for i in range(1, 70)] # Pool with numbers from 1 to 69
    sample_numbers = random.sample(pool, 5)
    sample_numbers.sort()
    power_ball = random.randint(1, 26)
    numbers = '\n  ' + str(sample_numbers) + ' + ' + str(power_ball) + '\n'
    txt.insert(1.0, numbers)
    print('Power')


def clear(event): # Clear the Text and Label
    txt['state'] = tk.NORMAL  # Enable writing in the text box
    txt.delete(1.0,tk.END)
    txt['state'] = tk.DISABLED  # Disable writing in the text box
    lbl_good_luck.config(text = '\n\n\n\n     ')


def go():
    lottery = radio.get()   
    draws_number = int(spin.get())

    txt['state'] = tk.NORMAL  # Enable writing in the text box
    txt.delete(1.0, tk.END)
    for draws in range(draws_number):
        if lottery == 0:
            megamillions()

        elif lottery == 1:
            powerball()
    txt['state'] = tk.DISABLED  # Disable writing in the text box
    lbl_good_luck.config(text = '\n\n\n\nGood Luck !!!')


# GUI
window = tk.Tk()
window.title('Lucky numbers')
#window.geometry('355x235')

frm = tk.Frame(window)
frm.grid( row = 0, column = 0, sticky = 'n')

# Radiobuttons
radio = tk.IntVar()

r_mega = tk.Radiobutton(frm, text = 'Mega Millions', font=('Arial Bold', 10), fg = 'blue',  variable=radio, value=0)  
r_mega.grid(row = 0, column = 0, sticky = 'w')  
r_mega.bind('<Button-1>', clear) # if you click on the this Entry it will erase the Text Box
  
r_power = tk.Radiobutton(frm, text = 'Powerball', font=('Arial Bold', 10), fg = 'blue', variable=radio, value=1)  
r_power.grid(row = 1, column = 0, sticky = 'w')
r_power.bind('<Button-1>', clear) # if you click on the this Entry it will erase the Text Box

# spin Label             
lbl_spin = tk.Label(frm, text = 'Draws:')
lbl_spin.grid(row = 2,column = 0)

# spinbox  
spin = Spinbox(frm, from_ = 1, to = 6,width=4,bd=1)  
spin.grid(row = 3, column = 0)
spin.bind('<Button-1>', clear) # if you click on the this Entry it will erase the Text Box
  
# Button "Go"
btn = tk.Button(frm, text = 'GO!', font=('Arial Bold', 10), fg = 'blue', command = go)
btn.grid(row = 4, column = 0, pady = 5)

#txt = Text(master = window, width=20, height=6)
txt = tk.Text(window, width=30, height=14)
txt.grid(row = 0, column = 1, padx = 5, pady = 5)

# Message 'Good Luck !!!'
lbl_good_luck = tk.Label(frm, text = '\n\n\n\nGood Luck !!!',font=('Arial Bold', 12), fg = 'green' ) # Label "Good Luck"
lbl_good_luck = tk.Label(frm, text = '\n\n\n\n            ',font=('Arial Bold', 12), fg = 'green' ) # Label "Good Luck"
lbl_good_luck.grid(row = 5, column = 0)


# Copy in context menu 
def text_copy(event=None):
        window.clipboard_clear()
        text = txt.get("sel.first", "sel.last")
        window.clipboard_append(text)

# Context menu
m = tk.Menu(txt, tearoff = 0) 
m.add_command(label ="Copy", command = text_copy)  
  
def do_popup(event): 
    try: 
        m.tk_popup(event.x_root, event.y_root) 
    finally: 
        m.grab_release() 
  
txt.bind("<Button-3>", do_popup) 
  

window.mainloop()
 
