import tkinter as tkinter
from tkinter import messagebox

# def add_digit(digit) :
#     value = calc.get() + str(digit)
#     calc.delete(0, tk.END)
#     calc.insert(0, value)

window = tkinter.Tk()

# def calculate() :
    
    

# def add_digit_func(sign) :
#     if(sign == '-') :
#         print('-')
#     elif(sign == '+') :
#         print('+')
#     elif(sign == '=') :
#         print('=')
#     # let's save our number before we clear into a new variable
#     # add old saved number to new one, clear again, return added results
#     calc.delete(0, tk.END)



# win.title('Calculator')
# win.geometry('500x500+1000+0')

# calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=10)
# calc.grid(row=0, column=0, columnspan=3, stick='wens')

# tk.Button(text='1', bd=5, command=lambda : add_digit(1)).grid(row=1, column=0, stick='wens')
# tk.Button(text='2', bd=5, command=lambda : add_digit(2)).grid(row=1, column=1, stick='wens')
# tk.Button(text='3', bd=5, command=lambda : add_digit(3)).grid(row=1, column=2, stick='wens')
# tk.Button(text='4', bd=5, command=lambda : add_digit(4)).grid(row=2, column=0, stick='wens')
# tk.Button(text='5', bd=5, command=lambda : add_digit(5)).grid(row=2, column=1, stick='wens')
# tk.Button(text='6', bd=5, command=lambda : add_digit(6)).grid(row=2, column=2, stick='wens')
# tk.Button(text='7', bd=5, command=lambda : add_digit(7)).grid(row=3, column=0, stick='wens')
# tk.Button(text='8', bd=5, command=lambda : add_digit(8)).grid(row=3, column=1, stick='wens')
# tk.Button(text='9', bd=5, command=lambda : add_digit(9)).grid(row=3, column=2, stick='wens')
# tk.Button(text='0', bd=5, command=lambda : add_digit(0)).grid(row=4, column=0, stick='wens')

# tk.Button(text='+', bd=5, command=lambda : add_digit_func('+')).grid(row=3, column=1, stick='wens')
# tk.Button(text='-', bd=5, command=lambda : add_digit_func('-')).grid(row=3, column=2, stick='wens')
# tk.Button(text='=', bd=5, command=lambda : add_digit_func('=')).grid(row=4, column=0, stick='wens')


# win.grid_columnconfigure(0, minsize=60)
# win.grid_columnconfigure(1, minsize=60)
# win.grid_columnconfigure(2, minsize=60)


# win.grid_rowconfigure(1, minsize=60)
# win.grid_rowconfigure(2, minsize=60)
# win.grid_rowconfigure(3, minsize=60)
# win.grid_rowconfigure(4, minsize=60)


# win.mainloop()

window.title("Login form")
window.geometry('340x440')
window.configure(bg='#333333')

def login():
    username = "johnsmith"
    password = "12345"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tkinter.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()