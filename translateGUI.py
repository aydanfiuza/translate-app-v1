from tkinter import *
import nlpcloud

client = nlpcloud.Client("nllb-200-3-3b", "3c1bbe039a3df4fc8ebc3025dfd5aabd63767091")

window = Tk()
window.title("Translate")
window.geometry("800x600")

label = Label(window, text="Insira seu texto abaixo para ser traduzido")
label.pack()

input = Entry(window, width=40)
input.focus_set()
input.pack()

def entry_input():
    input_text = input.get()
    response = client.translation(input_text, source='por_Latn', target='eng_Latn')
    for value in response.values():
        string = str(value)
    new_label = Label(window, text=string)
    new_label.pack()

button = Button(window, text="Enviar", command=entry_input)
button.pack()

window.mainloop()