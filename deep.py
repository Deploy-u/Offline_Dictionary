from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

def change(text="type", src="english", dest="hindi"):
    return GoogleTranslator(source=src, target=dest).translate(text)

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0, END)
    try:
        translated = change(text=msg, src=s, dest=d)
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, translated)
    except Exception as e:
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, f"Error: {e}")

# UI
root = Tk()
root.title("TEXT TRANSLATOR")
root.geometry("500x700")
root.config(bg='SkyBlue')

Label(root, text="TRANSLATOR", font=("Times New Roman", 40, "bold")).place(x=100, y=40, height=50, width=300)
Frame(root).pack(side=BOTTOM)

Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="SkyBlue").place(x=100, y=100, height=20, width=300)
Sor_txt = Text(root, font=("Times New Roman", 14), wrap=WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)

lang_list = ["english", "hindi", "french", "german", "spanish", "chinese", "arabic", "japanese", "korean", "russian", "portuguese", "bengali", "tamil", "telugu"]

comb_sor = ttk.Combobox(root, value=lang_list)
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("english")

Button(root, text="Translate", relief=RAISED, command=data).place(x=170, y=300, height=40, width=150)

comb_dest = ttk.Combobox(root, value=lang_list)
comb_dest.place(x=330, y=300, height=40, width=150)
comb_dest.set("hindi")

Label(root, text="Translated Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="SkyBlue").place(x=100, y=360, height=20, width=300)
dest_txt = Text(root, font=("Times New Roman", 14), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()
