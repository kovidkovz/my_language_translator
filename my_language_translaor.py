# To create a translator we will import the googletrans module
from googletrans import Translator,LANGUAGES
# We have called the two classes Translator and languages, Languages have been imported successfully.

# we will create a function and call the class translator

def convert_lang(text,destination,source):
    translator=Translator()
    trans=translator.translate(text,destination,source)
    return trans

# how to get the data
# create a function called data

def data():
    msg= source_txt.get(1.0,END)
    textget=convert_lang(msg,source=combo_source.get(),destination=combo_dest.get())
    destination_txt.delete(1.0,END)
    destination_txt.insert(END,textget)






# Tkinter is a library used in python, which is used to create GUI(Graphical User Interface)
from tkinter import *
# In the next line, the class ttk helps bring a combo box 
from tkinter import ttk

# Now we will create an object known as root, in which we will call the Tk class
# This will create an interface box of the graphic we will need to create our project.
# Then, we will keep adding attributes to the box that we have created using the Tk class
root=Tk()
root.title("Language-Translator")    # this will give a title to our box
root.geometry("500x700")    # this will decide the geometry(length and width) of the box
root.config(bg='lightblue') # color of the box that we have created.

# Tkinter Label is a widget that is used to implement display boxes where you can place text or images.
# text: decides the name of the display box.
# font: to decide the font of the box created.
# bg: decides the color of the new box created.
# place: the position of the box created is managed by .place(x,y,height, width)

labl_txt=Label(root,text="Translator",font=("Time 40 italic bold"),bg='Yellow').place(x=100,y=40,height=50,width=300)

# we will now be creating a text box, where we can write text.
# For creating a text box, first we need to create a frame.

frame=Frame(root).pack(side=BOTTOM)          # .pack() is used for the placement of the text box.

# Now we have created a frame, its time to create a text box now
# we will now use text box to create a text box.
# we will be creating two text boxes, one for source and another for destination.

# label of the source text is written below
labl_txt=Label(root,text="Source Text",font=("Time 20 roman bold"),bg='lightblue',fg="black").place(x=100,y=120,height=20,width=300)

# Source text, we will be using the Text method to create a text box.
# text wrap module is used to generate or format plain text inside the text box.
source_txt= Text(frame,font=("Time 20 italic bold"),wrap=WORD)
source_txt.place(x=10,y=150,height=200,width=480)

# For source text we will be creating a combo box.
# A combo box is used in graphical user interfaces, it is a text box or a type of a drop box that contains a list of things.

# This combo box will contain a list of languages. Below is the list of languages.
list_text=list(LANGUAGES.values())

# Our first combo box is given below, which is the combo box of our source
# we had already called a module at the starting of this code as ttk for combo box.
# Inside the Comboboc we will call frame and then the value of the list we have created.
combo_source=ttk.Combobox(frame,value=list_text)
combo_source.place(x=10,y=360,height=40,width=150)
# we will use combobox.set("English") method to set english as our default language in the combobox.
combo_source.set("english")

# Create a button to change languages using the button method
button_1=Button(frame, text="Translate",relief=RAISED,command=data)
# relief=RAISED will give the button a 3-d look
button_1.place(x=170,y=360,height=40,width=150)

# create a combobox for destination
combo_dest=ttk.Combobox(frame,value=list_text)
combo_dest.place(x=330,y=360,height=40,width=150)
combo_dest.set("hindi")


# Now we will create a text box for the destination similar to the text box of the source.

destination_txt= Text(frame,font=("Time 20 italic bold"),wrap=WORD)
destination_txt.place(x=10,y=450,height=200,width=480)

# we will now create a destination label similar to the source label
labl_txt=Label(root,text="Destination Text",font=("Time 20 roman bold"),bg='lightblue',fg="black").place(x=100,y=420,height=20,width=300)





root.mainloop()  # this will finally print or make the box visible to us.

