import tkinter as tk


window = tk.Tk()


frame_a = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
frame_b = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)

greeting = tk.Label(
    master=frame_a,
    text=f'Hello, Tkinter',
    fg='sky blue',
    bg='gray14',
    width=30,
    height=2
    )
greeting.pack()

button = tk.Button(
    master=frame_b,
    text='Click me!',
    width=25,
    height=5,
    bg='blue',
    fg='white'
)
button.pack()

frame_a.pack(side=tk.LEFT)
frame_b.pack(side=tk.RIGHT)

label = tk.Label(text='Name')
entry = tk.Entry(fg='white', bg='black', width=50)

label.pack()
entry.pack()

entry.get()

text_box = tk.Text()
text_box.pack()

window.mainloop()
