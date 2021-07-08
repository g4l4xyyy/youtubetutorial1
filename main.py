from tkinter import *
import tkinter
#Εισαγωγή Modules


app= tkinter.Tk() #**Μπορείς να αλλάξεις το app με ότι θες, αλλα θα πρεπει να αλλαχτει παντού**
app.title ('Sub') #Τίτλος
app.geometry ('750x750')#Μεγεθος
#Customize



c1 = Canvas(app, bg= 'black', cursor= 'circle')
c1.pack()
#Βασικός Κώδικας Σχημάτων

l1 = Label(app, text= 'Thank you for clicking me')
#κωδικας text

b1 = Button(app, text= 'Click Me', command= l1.pack)
b1.pack()
#Κώδικας Κουμπιού


e1 = Entry(app)
e1.pack()
#Κώδικας Text Entry

b2 = Button(app, text= 'Clear text entry', command= e1.pack_forget)
b2.pack()


app.mainloop()