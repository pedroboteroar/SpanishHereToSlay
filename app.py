import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


# Create a class App, which inherits from tk.Tk
# This App has a main window, which is the root of the application and includes an image located in the assets folder,
# a title and two buttons.
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        self.geometry("600x400")
        # Change the window to white background
        self.config(bg="white")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        image = Image.open("./assets/logo.png")
        image = image.resize((200, 200))
        self.img = ImageTk.PhotoImage(image)
        self.img_label = ttk.Label(self, image=self.img)
        self.img_label.pack(pady=10)

        self.label = ttk.Label(self, text="Here To Slay")
        self.label.pack(pady=10)

        self.button = ttk.Button(
            self, text="Manual de Juego", command=self.clicked_manual
        )
        self.button.pack(pady=10)

        self.button2 = ttk.Button(
            self, text="Cartas y Personajes", command=self.clicked_cartas
        )
        self.button2.pack(pady=10)

    def clicked_manual(self):
        self.label.config(text="You clicked the button!")

    def clicked_cartas(self):
        self.label.config(text="You clicked the button 2!")


if __name__ == "__main__":
    app = App()
    app.mainloop()
