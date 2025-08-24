from .settings import *

# Denha frames
class DrawFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class DrawLabel(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class DrawEntry(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class DrawButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class DrawAlert(ctk.CTkToplevel):
    def __init__(self, master, text, **kwargs):
        super().__init__(master, **kwargs)
        self.title('Messagem do Download-ALL')
        self.geometry('500x80')

        self.text = DrawLabel(
            self,
            text=text,
        )
        self.text.pack(padx=20, pady=20)
