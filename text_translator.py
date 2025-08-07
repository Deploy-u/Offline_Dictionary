# from tkinter import *
# from tkinter import ttk
# # python text_translator.py
# # from googletrans import Translator,LANGUAGES
# from deep_translator import GoogleTranslator


# # def change(text="type",src="English",dest="Hindi"):
# #     text1=text
# #     src1=src
# #     dest1=dest
# #     trans= Translator()
# #     trans1=trans.translate(text,src=src1,dest=dest1)
# #     return trans1.txt

# def change(text="type", src="english", dest="hindi"):
#     return GoogleTranslator(source=src, target=dest).translate(text)



# def data():
#     s=comb_sor.get()
#     d=comb_dest.get()
#     masg=Sor_txt.get(1.0,END)
#     textget=change(text=masg,src=s,dest=d)
#     dest_txt.delete(1.0,END)
#     dest_txt.insert(END,textget)





# root = Tk()
# root.title("TEXT TRANSLATOR")
# root.geometry("500x700")
# root.config(bg='SkyBlue')

# lab_txt=Label(root,text="TRANSLATOR", font=("Time New Roman",40,"bold"))
# lab_txt.place(x=100,y=40,height=50,width=300)

# # frame= Frame(root).pack(side=BOTTOM)
# frame = Frame(root)
# frame.pack(side=BOTTOM)


# lab_txt=Label(root,text="Source Text", font=("Time New Roman",20,"bold") ,fg="Black",bg="SkyBlue")
# lab_txt.place(x=100,y=100,height=20,width=300)

# Sor_txt = Text(frame,font=("Time New Roman",40,"bold"), wrap=WORD)
# Sor_txt.place(x=10,y=130,height=150,width=480)

# # list_text= list(LANGUAGES.values())


# list_text = [
#     "english", "hindi", "french", "german", "spanish", "chinese", "japanese",
#     "korean", "arabic", "russian", "portuguese", "bengali", "tamil", "telugu",
#     "italian", "urdu", "gujarati"
# ]

# comb_sor =ttk.Combobox(frame,value=list_text)
# comb_sor.place(x=10,y=300,height=40,width=150)
# comb_sor.set("english")


# button_change = Button(frame,text="Translate",relief=RAISED,command=data)
# button_change.place(x=170,y=300,height=40,width=150)

# comb_dest =ttk.Combobox(frame,value=list_text)
# comb_dest.place(x=330,y=300,height=40,width=150)
# comb_dest.set("english")


# lab_txt=Label(root,text="Dest Text", font=("Time New Roman",20,"bold") ,fg="Black",bg="SkyBlue")
# lab_txt.place(x=100,y=360,height=20,width=300)

# dest_txt = Text(frame,font=("Time New Roman",40,"bold"), wrap=WORD)
# dest_txt.place(x=10,y=400,height=150,width=480)




# root.mainloop()

















from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

# ✅ Function to perform translation
def change(text="type", src="english", dest="hindi"):
    return GoogleTranslator(source=src, target=dest).translate(text)

# ✅ Callback for Translate button
def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END).strip()
    if masg:
        try:
            textget = change(text=masg, src=s, dest=d)
            dest_txt.delete(1.0, END)
            dest_txt.insert(END, textget)
        except Exception as e:
            dest_txt.delete(1.0, END)
            dest_txt.insert(END, f"Error: {str(e)}")

# ✅ Clear button functionality
def clear_text():
    Sor_txt.delete(1.0, END)
    dest_txt.delete(1.0, END)

# ✅ Main Window
root = Tk()
root.title("TEXT TRANSLATOR")
root.geometry("520x750")
root.config(bg='SkyBlue')

# ✅ Heading
Label(root, text="TEXT TRANSLATOR", font=("Times New Roman", 28, "bold"), bg="SkyBlue").place(x=70, y=10)

# ✅ Source Text Label
Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="black", bg="SkyBlue").place(x=160, y=60)

# ✅ Source Text Box
Sor_txt = Text(root, font=("Times New Roman", 14), wrap=WORD)
Sor_txt.place(x=10, y=100, height=150, width=480)

# ✅ Languages list
list_text = [
    "english", "hindi", "french", "german", "spanish", "chinese", "japanese",
    "korean", "arabic", "russian", "portuguese", "bengali", "tamil", "telugu",
    "italian", "urdu", "gujarati"
]

# ✅ Language Selectors & Translate Button
comb_sor = ttk.Combobox(root, value=list_text)
comb_sor.place(x=10, y=270, height=40, width=150)
comb_sor.set("english")

button_change = Button(root, text="Translate", relief=RAISED, command=data)
button_change.place(x=180, y=270, height=40, width=150)

comb_dest = ttk.Combobox(root, value=list_text)
comb_dest.place(x=340, y=270, height=40, width=150)
comb_dest.set("hindi")

# ✅ Destination Text Label
Label(root, text="Dest Text", font=("Times New Roman", 20, "bold"), fg="black", bg="SkyBlue").place(x=180, y=330)

# ✅ Destination Text Box
# dest_txt = Text(root, font=("Times New Roman", 14), wrap=WORD)
# dest_txt.place(x=10, y=370, height=150, width=480)
# ✅ Destination Text Box with Scrollbar
dest_frame = Frame(root)
dest_frame.place(x=10, y=370, height=150, width=480)

scrollbar = Scrollbar(dest_frame)
scrollbar.pack(side=RIGHT, fill=Y)

# dest_txt = Text(dest_frame, font=("Times New Roman", 14), wrap=WORD, yscrollcommand=scrollbar.set)
dest_txt = Text(dest_frame, font=("Nirmala UI", 16), wrap=WORD, yscrollcommand=scrollbar.set)

dest_txt.pack(fill=BOTH, expand=True)

scrollbar.config(command=dest_txt.yview)

# ✅ Optional Clear Button
Button(root, text="Clear", command=clear_text).place(x=210, y=540, height=30, width=100)

# ✅ Start GUI
root.mainloop()
