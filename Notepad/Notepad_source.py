from tkinter import *
from tkinter.filedialog import askopenfilename


def File(root, window_note, brower_text):
    global name_file
    name_file = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    with open(name_file, 'r',encoding='utf8') as file:
        data = file.read()
        brower_text.delete("1.0",END)
        window_note.delete("1.0",END)
        brower_text.insert(END, name_file)
        window_note.insert(END, data)


def Claer(messagebox,window_note, brower_text):
    MsgBox = messagebox.askquestion ('Claer all screen','Are you sure you want to claer the application',icon = 'warning')
    if MsgBox == 'yes':
        brower_text.delete("1.0",END)
        window_note.delete("1.0",END)
    else:
        messagebox.showinfo('Return','You will now return to the application screen')


def saves(messagebox,window_note, brower_text):
    MsgBox = messagebox.askquestion ('Save File','Are you sure you want to Save File')
    if MsgBox == 'yes':
        if brower_text.get('1.0',END) == '\n':
            messagebox.showinfo('Nor Save File','Save Error Check the file name ')
        else:
            texts = brower_text.get('1.0',END).replace('\n', '')
            messagebox.showinfo('save File','Save Successfully {0}'.format(brower_text.get('1.0',END)))
            with open(texts, 'w') as files:
                files.write(window_note.get('1.0',END))
    else:
        messagebox.showinfo('Return','You will now return to the application screen')



