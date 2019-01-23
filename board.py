import Tkinter as tk
from PIL import Image, ImageTk

class Board:

    def __init__(self):
        window = tk.Tk()
        window.resizable(width=False, height=False)
        window.geometry('{}x{}'.format(460, 350))
#        frame = tk.Frame(window, height=5000, width=5000)

        window.title('Euchre')

        button1 = tk.Button(window, text='Play', command=play)
        button1.place(relx=0.3, rely=0.9)

        button2 = tk.Button(window, text='Play', command=play)
        button2.place(relx=0.4, rely=0.9)

        button3 = tk.Button(window, text='Play', command=play)
        button3.place(relx=0.5, rely=0.9)

        button4 = tk.Button(window, text='Play', command=play)
        button4.place(relx=0.6, rely=0.9)

        button5 = tk.Button(window, text='Play', command=play)
        button5.place(relx=0.7, rely=0.9)

        image = Image.open("img/Hand_one.jpg")
        photo = ImageTk.PhotoImage(image)

        for i in range(0, 5):
            label = tk.Label(image=photo)
            label.image = photo  # keep a reference!
            label.place(relx=(0.2 + i/10.0 + 0.075), rely=0.05)

        image.rotate(60)
        photo2 = ImageTk.PhotoImage(image)
        label2 = tk.Label(image=photo2)
        label2.place(relx=0.5, rely=0.5)

        window.mainloop()


def play():
    print 'PRESSED'
