import tkinter as tk


win = tk.Tk()
win.title('Calculator')
win.geometry('380x550+200+100')
win.resizable(0,0)

# ******************** Functions **************************


def enter_number(x):
    last_char = entry_box.get()[-1]

    if entry_box.get() == '0' or entry_box.get() == 'Syntax error':
        entry_box.delete(0,'end')
        entry_box.insert(0,str(x))
    elif last_char in ['+', '-','*','/'] and x == '0':
        pass
    else:
        length = len(entry_box.get())
        entry_box.insert(length,str(x))


def func_dot(x):
    content = entry_box.get()
    length = len(content)

    if entry_box.get() == '0':
        if x == '.':
            entry_box.insert(1,'.')
    else:
        entry_box.insert(length,'.')


def enter_operators(x):
    if entry_box.get() != '0':
        length = len(entry_box.get())
        content = entry_box.get()
        last_char = content[-1]

        if last_char in ['+','-','/'] or content[-2:] == '**':
            pass
        else:
            entry_box.insert(length, operators_list[x]['text'])


def fun_clr():
    entry_box.delete(0,'end')
    entry_box.insert(0,'0')


result = 0
history = []
def func_equal():
    content = entry_box.get()
    try:
        result=eval(content)
        entry_box.delete(0,'end')
        entry_box.insert(0,str(result))
        history.append(content)
        history.reverse()
        status.configure(text='History: '+ ' | '.join(history[0:7]), font='verdana 7 bold')
    except:
        entry_box.delete(0,'end')
        entry_box.insert(0,'Syntax error')


def func_del():
    if entry_box.get() == 'Syntax error':
        entry_box.delete(0, 'end')
        entry_box.insert(0, '0')
    if entry_box.get() !='0':
        length = len(entry_box.get())
        entry_box.delete(length-1, 'end')

        if length == 1:
            entry_box.insert(0,'0')


# ********************** Entry Box ********************

entry_box = tk.Entry(font='verdana 14 bold', width=22, bd=6, justify=tk.RIGHT)
entry_box.insert(0,'0')
entry_box.pack(padx=10, pady=10)


btn_list = []
for i in range(10):
    btn_list.append(tk.Button(text=str(i), bd=6,font='verdana 14 bold', width=4, command = lambda x=i:enter_number(x)))

btn_numbers=1
for i in range(3):
    for j in range(3):
        btn_list[btn_numbers].place(x=30+j*90, y=70+i*70)
        btn_numbers+=1

# ************** operators btn ***************

operators_list = []
for i in range(4):
    operators_list.append(tk.Button(width=4, font='verdana 14 bold', bd=5, command = lambda x=i: enter_operators(x)))

operators_list[0]['text'] = '+'
operators_list[1]['text'] = '-'
operators_list[2]['text'] = '*'
operators_list[3]['text'] = '/'

for i in range(4):
    operators_list[i].place(x=290, y=70+i*70)


# *************** zero btn *************

zero_btn = tk.Button(text='0',width=11, font='verdana 14 bold', bd=5, command = lambda x='0': enter_number(x))
zero_btn.place(x=30, y=280)

# ************ clr btn **********

clr_btn = tk.Button(text='C',width=11, font='verdana 14 bold', bd=5, command = fun_clr)
clr_btn.place(x=30, y=350)

# *************** dot btn **************

btn_dot = tk.Button(text='.',width=4, font='verdana 14 bold', bd=5, command = lambda x='.': func_dot(x))
btn_dot.place(x=210, y=280)

# *************** del btn **************

btn_del = tk.Button(text='Del',width=10, font='verdana 14 bold', bd=5, command = func_del)
btn_del.place(x=210, y=350)

# ************************** equal btn ****************

btn_equal = tk.Button(text='=',width=24, font='verdana 14 bold', bd=5, command = func_equal)
btn_equal.place(x=30, y=420)


# ****************** status bar *************

status = tk.Label(win, text='History ', font='verdana 7 bold')
status.place(x=30,y=490)


# *************** copyright message *************

message = tk.Label(text='©All rights reserved to Ekram',font='verdana 7')
message.pack(side=tk.BOTTOM, fill=tk.Y)


win.mainloop()