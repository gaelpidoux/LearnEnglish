import tkinter
import tkinter.messagebox

def matter_button_click():
    tkinter.messagebox.showinfo(
        'Résultat'

    )

    print(test_entry.get())


fenetre = tkinter.Tk()
fenetre.title('GPCorporation')

tkinter.Label(text="Default question ?").pack()
test_entry = tkinter.Entry()
test_entry.pack()
tkinter.Button(text="I'm sur", command= matter_button_click).pack()

fenetre.mainloop()

