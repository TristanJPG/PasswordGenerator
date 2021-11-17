import random
from tkinter import *

root = Tk()
root.title("Password Generator") 
root.geometry("800x145") 
root.resizable(1,1)
#label info
text_font= ("Boulder", 40, 'bold')
background = "#716F81"
foreground= "#B97A95"
border_width = 450


label = Label(root, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)
label.place(relx = 0.5, rely = 0.5, anchor = 'center')


def shuffle(string):
    shuffled= list(string)
    random.shuffle(shuffled)
    return ''.join(shuffled)
def generator():
    uppercaseLetter01 = chr(random.randint(65, 90))
    uppercaseLetter02 = chr(random.randint(65, 90))
    uppercaseLetter03 = chr(random.randint(65, 90))
    uppercaseLetter04 = chr(random.randint(65, 90))
    lowercaseLetter01 = chr(random.randint(97, 122))
    lowercaseLetter02 = chr(random.randint(97, 122))
    lowercaseLetter03 = chr(random.randint(97, 122))
    number01 = chr(random.randint(48, 57)) 
    number02 = chr(random.randint(48, 57)) 
    number03 = chr(random.randint(48, 57)) 
    exclam = "!"

    password = uppercaseLetter01 + uppercaseLetter02 + uppercaseLetter03 + uppercaseLetter04 + lowercaseLetter01 + lowercaseLetter02 + lowercaseLetter03 + number01 + number02 + number03 + exclam
    shufflePass = shuffle(password)
    label.config(text=shufflePass)
    root.clipboard_clear()
    root.clipboard_append(shufflePass)
   

generator()
root.mainloop()




