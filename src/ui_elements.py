from .settings import *

def toplevel_alert_position(master):
    # Define o tamanho padrão
    width = 500
    height = 100

    # Pegar posição e tamanho da janela principal (root)
    master.update_idletasks()
    root_x = master.winfo_x()
    root_y = master.winfo_y()
    root_width = master.winfo_width()
    root_height = master.winfo_height()

    # Calcular posição para centralizar
    x = root_x + (root_width // 2) - (width // 2)
    y = root_y + (root_height // 2) - (height // 2)

    return width, height, x, y


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
    def __init__(self, master, text, error_text, **kwargs):
        super().__init__(master, **kwargs)
        self.title('Messagem do Download-ALL')

        self.overrideredirect(True)   # cria sem decorações (não pisca)
        self.withdraw()               # ainda oculta

        width, height, x, y = toplevel_alert_position(master)

        # Aplicar geometry
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()


        self.text = DrawLabel(
            self,
            text=text,
            font=('Arial', 20),
        )
        self.text.pack(pady=(10, 5))

        # Mostra no alerta o tipo de erro
        # self.error_text = DrawLabel(
        #     self,
        #     text=error_text,
        #     font=('Arial', 10),
        # )
        # self.error_text.pack(pady=(10, 5))

        self.ok_button = DrawButton(self, text='OK', command=self.destroy)
        self.ok_button.pack(pady=(5, 10))

