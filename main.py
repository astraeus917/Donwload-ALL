import os
import customtkinter as ctk
import yt_dlp


app_width = 700
app_height = 300


class MainFrame(ctk.CTkFrame):
    def __init__(self, master, width, height):
        super().__init__(master, width=width, height=height)


class Main(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações basicas
        self.title("Download-ALL")
        self.geometry(f'{app_width}x{app_height}')
        self.resizable(False, False)

        # Configuração de grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Frame principal
        self.main_frame = MainFrame(self, width=app_width, height=app_height)
        self.main_frame.grid(row=0, column=0, sticky='nsew')


if __name__ == '__main__':
    app = Main()
    app.mainloop()
