import tkinter as tk


def key_handler(event=None):
    if event and event.keysym in ('s', 'p'):
        'do something'


r = tk.Tk()
t = tk.Text()
t.pack()
r.bind('<Key>', key_handler)
r.mainloop()
