from tkinter import *;
from tkinter import messagebox;

def actionauthor():
    messagebox.showinfo("Author", "Pranta Sarker\nBatch: 6th\nDepartment: CSE\nNorth East University Bangladesh")

#Check weather the input string is a number or not
def is_number(s):
    if(s != ''):
        if (s.replace('.', '', 1).isdigit()):
            return True
        if (s.isdigit()):
            return True;
        if s[0] in ['-', '+', '.', '0', ' ']:
            if (s[1] == '.'):
                if (s[2:].isdigit()):
                    return True
            if (s[1] == '0' and s[2] == '.'):
                if (s[3:].isdigit()):
                    return True
            if s[1:].isdigit():
                return True;
        return False;

def casting(num):
    if('.' in num):
        return float(num);
    else:
        return int(num)


#Plus sign function
def actionPlus():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='red', bg='#9ed8ee')
    Showtemplabel.insert(0, 'Summation');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')
    ans = "0";
    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();

    if(is_number(num1) == True and is_number(num2) == True and num1 != ' ' and num2 != ' '):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 + num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='red', bg='#9ed8ee')
        Showtemplabel.insert(0, 'Summation');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")

#Minus sign function
def actionMinus():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='green', bg='#ece7e2')
    Showtemplabel.insert(0, 'Subtraction');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0";

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();

    if(is_number(num1)==True and is_number(num2)==True):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 - num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='green', bg='#ece7e2')
        Showtemplabel.insert(0, 'Subtraction');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")

#Multiplication sign function
def actionMul():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='blue', bg='#cacba9')
    Showtemplabel.insert(0, 'Multiplication');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();
    if(is_number(num1)==True and is_number(num2)==True):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 * num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='blue', bg='#cacba9')
        Showtemplabel.insert(0, 'Multiplication');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")

#Division sign function
def actionDiv():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'Division');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();
    if(is_number(num1)==True and is_number(num2)==True):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 / num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'Division');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")

root = Tk();
root.title('My First Python Calculator');
root.geometry('380x300+200+250');
Titlelabel = Label(root, fg = 'green' , font = 'none 10 bold underline' ,text = 'Python Calculator', compound = CENTER)
Titlelabel.place(relx=0.5, rely=0.1, anchor='center')
Showlabel = Entry(root);
Showtemplabel = Entry(root);
Numberentry1 = Entry(root);
Numberentry2 = Entry(root);
Numberentry1.place(relx=0.5, rely=0.3, anchor='center')
Numberentry2.place(relx=0.5, rely=0.4, anchor='center')

plusbutton = Button(root, text="+", width = 5, command = actionPlus);
plusbutton.place(relx=0.1, rely=0.7)

minusbutton = Button(root, text="-", width = 5, command = actionMinus);
minusbutton.place(relx=0.3, rely=0.7)

mulbutton = Button(root, text="*", width = 5, command = actionMul);
mulbutton.place(relx=0.5, rely=0.7)

divbutton = Button(root, text="/", width = 5, command = actionDiv);
divbutton.place(relx=0.7, rely=0.7)

authorbutton = Button(root, text='Author', width=6, command = actionauthor);
authorbutton.place(relx = 0.5, rely=0.95, anchor='center');

root.resizable(False, False);
root.mainloop();



// Another code for calculator//
#import all the necessary files in order to access the functions.
#Tkinter is the standard GUI library for Python.
from tkinter import *
from tkinter.messagebox import *
import math as m

# common font size.
font = ('Times New Roman',14, 'bold')

#functions to activate the working of button.
def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)

#this function is created to clear of all inputs in one go.
   def all_clear():
    textField.delete(0, END)

def click_btn_function(event):
    global p
    print("btn clicked")
    b = event.widget
    text = b['text']
    print(text)

    if text = = 'x':
        textField.insert(END, "*")
        return

    if text == '=':
        try:
            ex = textField.get()
            ans = eval(ex)
            textField.delete(0, END)
            textField.insert(0, ans)
        except Exception as e:
            print("Error..", e)
            showerror("Error", e)
        return

    textField.insert(END, text)

# creating a window
window = Tk()
window.title('My Calculator')
window.geometry('300x465')

# picture label
pic = PhotoImage(file='sci.png')
headingLabel = Label(window, image=pic)
headingLabel.pack(side=TOP, pady=10)

# heading label
heading = Label(window, text='Solve your problem', font=font)
heading.pack(side=TOP)

# textfiled
textField = Entry(window, font=font, justify=CENTER)
textField.pack(side=TOP, pady=10, fill=X, padx=10)

#buttons
buttonFrame = Frame(window)
buttonFrame.pack(side=TOP, padx=10)

# adding button
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief='ridge', activebackground='black',
                     activeforeground='yellow')
        btn.grid(row=i, column=j)
        temp = temp + 1
        btn.bind('<Button-1>', click_btn_function)

zeroBtn = Button(buttonFrame, text='0', font=font, width=5, relief='ridge', activebackground='black',
                 activeforeground='yellow')
zeroBtn.grid(row=3, column=0)

dotBtn = Button(buttonFrame, text='.', font=font, width=5, relief='ridge', activebackground='black',
                activeforeground='yellow')
dotBtn.grid(row=3, column=1)

equalBtn = Button(buttonFrame, text='=', font=font, width=5, relief='ridge', activebackground='black',
                  activeforeground='yellow')
equalBtn.grid(row=3, column=2)

plusBtn = Button(buttonFrame, text='+', font=font, width=5, relief='ridge', activebackground='black',
                 activeforeground='yellow')
plusBtn.grid(row=0, column=3)

minusBtn = Button(buttonFrame, text='-', font=font, width=5, relief='ridge', activebackground='black',
                  activeforeground='yellow')
minusBtn.grid(row=1, column=3)

multBtn = Button(buttonFrame, text='x', font=font, width=5, relief='ridge', activebackground='black',
                 activeforeground='yellow')
multBtn.grid(row=2, column=3)

divideBtn = Button(buttonFrame, text='/', font=font, width=5, relief='ridge', activebackground='black',
                   activeforeground='yellow')
divideBtn.grid(row=3, column=3)

sqrtBtn = Button(buttonFrame, text='√', font=font, width=5, relief='ridge', activebackground='black',
                 activeforeground='yellow')
sqrtBtn.grid(row=4, column=0)

powBtn = Button(buttonFrame, text='^', font=font, width=5, relief='ridge', activebackground='black',
                activeforeground='yellow')
powBtn.grid(row=4, column=1)

factBtn = Button(buttonFrame, text='x!', font=font, width=5, relief='ridge', activebackground='black',
                 activeforeground='yellow')
factBtn.grid(row=4, column=2)

radBtn = Button(buttonFrame, text='toRad', font=font, width=5, relief='ridge', activebackground='black',
                activeforeground='yellow')
radBtn.grid(row=4, column=3)

degBtn = Button(buttonFrame, text='toDeg', font=font, width=5, relief='ridge', activebackground='black',
                activeforeground='yellow')
degBtn.grid(row=5, column=0)

sinBtn = Button(buttonFrame, text='sinθ', font=font, width=5, relief='ridge', activebackground='black',
                activeforeground='yellow')
sinBtn.grid(row=5, column=1)

cosBtn = Button(buttonFrame, text='cosθ', font=font, width=5, relief='ridge', activebackground='black',
                activeforeground='yellow')
cosBtn.grid(row=5, column=2)

tanBtn = Button(buttonFrame, text='tanθ', font=font, width=5, relief='ridge', activebackground='black',
                activeforeground='yellow')
tanBtn.grid(row=5, column=3)

clearBtn = Button(buttonFrame, text='backspace', font=font, width=11, relief='ridge', activebackground='black',
                  activeforeground='yellow', command=clear)
clearBtn.grid(row=6, column=0, columnspan=2)

allClearBtn = Button(buttonFrame, text='AC', font=font, width=11, relief='ridge', activebackground='black',
                     activeforeground='yellow', command=all_clear)
allClearBtn.grid(row=6, column=2, columnspan=2)

# binding the buttons
plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
multBtn.bind('<Button-1>', click_btn_function)
divideBtn.bind('<Button-1>', click_btn_function)
zeroBtn.bind('<Button-1>', click_btn_function)
dotBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)

def enterClick(event):
    print('hi')
    e = Event()
    e.widget = equalBtn
    click_btn_function(e)

textField.bind('<Return>', enterClick)

#this function is created to calculate all the mathematical operations by calling the functions from the math library file.
 def calculate(event):
    print('btn..')
    btn = event.widget
    text = btn['text']
    print(text)
    ex = textField.get()
    answer = ''
    if text == 'toDeg':
        print("cal degree")
        answer = str(m.degrees(float(ex)))
    elif text == 'toRad':
        print('radian')
        answer = str(m.radians(float(ex)))
    elif text == 'x!':
        print("cal factorial")
        answer = str(m.factorial(int(ex)))
    elif text == 'sinθ':
        print("cal sin")
        answer = str(m.sin(m.radians(int(ex))))
    elif text == 'cosθ':
        answer = str(m.cos(m.radians(int(ex))))
    elif text == 'tanθ':
        answer = str(m.tan(m.radians(int(ex))))
    elif text == '√':
        print('sqrt')
        answer = m.sqrt(int(ex))
    elif text == '^':
        print('pow')
        base, pow = ex.split(',')
        print(base)
        print(pow)
        answer = m.pow(int(base), int(pow))
    textField.delete(0, END)
    textField.insert(0, answer)

#binding the remaining buttons
sqrtBtn.bind("<Button-1>", calculate)
powBtn.bind("<Button-1>", calculate)
factBtn.bind("<Button-1>",calculate)
radBtn.bind("<Button-1>", calculate)
degBtn.bind("<Button-1>", calculate)
sinBtn.bind("<Button-1>", calculate)
cosBtn.bind("<Button-1>", calculate)
tanBtn.bind("<Button-1>", calculate)
window.mainloop()
#end of code.

