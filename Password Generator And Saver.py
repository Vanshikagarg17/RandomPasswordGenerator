from tkinter import *
import random


list_num = ['1','2','3','4','5','6','7','8','9']


list_cap = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



list_small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


list_symbols = ['!','@','#','$','%','^','&','*','?','<','>','/','|']


rand_pass = []
def random_num():
    random_num = random.choice(list_num)
    rand_pass.append(random_num)


def random_smalls():
    random_short = random.choice(list_small)
    rand_pass.append(random_short)


def random_symbol():
    random_sym = random.choice(list_symbols)
    rand_pass.append(random_sym)


def random_caps():
    random_cap = random.choice(list_cap)
    rand_pass.append(random_cap)

y = 0
while y<3:
    random_caps()
    random_smalls()
    random_symbol()
    random_num()
    y += 1



random.shuffle(rand_pass)



final_pass = "".join(rand_pass)

def generate_pass():
    l2.grid(row=3,column=4,pady = 15)
    l3.grid(row=4,column=4)
    b2.grid(row=5,column=4,pady=15,padx=10)

o = open('Passwords.txt','a+')

def foraccount():
    i = web_value.get()
    o.write(i + ' '+':'+' '+ final_pass+'\n')

def save_pass():
    foraccount()

    o.seek(0)
    o.read()
    o.close()
    l4.grid(row=6,column=4,pady = 15)

root = Tk()

root.geometry('280x350')
root.configure(bg = 'orange')
root.title('Password Generator')


l1 = Label(root, text = 'Website :')
l2 = Label(root,text='Generated Password')
l3 = Label(root, bg='white',fg='black',text ='{}'.format(final_pass))
l4 = Label(root,text='Password Saved'+'\n'+'Rerun to add other password',font='bold')

l1.grid(row=0,column=4,pady=15,padx=110)


b1 = Button(root, fg='red', text = 'Generate Password',command=generate_pass)
b2 = Button(root, fg= 'blue',text='Save',command=save_pass)


b1.grid(row=2,column=4,pady= 15)


web = StringVar()

web_value = Entry(root,textvariable = web)
web_value.grid(row=1,column=4)


root.mainloop()
