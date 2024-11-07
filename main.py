import tkinter


def button_clicked():
    name = name_entry.get()
    output_display.delete(0.0, tkinter.END)
    output_display.insert(tkinter.END, f'Your name is {name}.')



window = tkinter.Tk()
window.title("Dungeons and Dragons")

tkinter.Label(window, text="Avoid the Dragons").grid(row=0, column=0, sticky=tkinter.W)
tkinter.Label(window, text="Enter your name: ").grid(row=0, column=0, sticky=tkinter.W)

name_entry = tkinter.Entry(window, width=20, bg="light blue")
name_entry.grid(row=1, column=0, sticky=tkinter.W)

output_display = tkinter.Text(window, width=75, height=6, wrap=tkinter.WORD, background="light blue")

enter_button = tkinter.Button(window,text="Submit", command=button_clicked()))
enter_button.grid(row=2, column=0, sticky=tkinter.W)

output_display.grid(row=3, column=0, columnspan=2, sticky=tkinter.W)
output_display.insert(tkinter.END, "Hello")

window.mainloop()




