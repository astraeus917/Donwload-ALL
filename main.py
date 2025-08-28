from src.ui_elements import *

# Função para configurar o peso de row e column
def configure_weight(self, row, column, weight):
    self.grid_propagate(False)
    self.grid_rowconfigure(row, weight=weight)
    self.grid_columnconfigure(column, weight=weight)


class MainFrame(ctk.CTkFrame):
    def __init__(self, master, width, height):
        super().__init__(master, width=width, height=height, fg_color="#181818")

        # Chama os widgets e elementos do app.
        self.draw_header()
        self.draw_body()


    def draw_header(self): # Cabeçalho do app
        self.header_frame = DrawFrame(
            self,
            width=app_width,
            height=70,
            fg_color="#151515",
        )
        self.header_frame.grid(row=0, column=0, sticky='nsew')
        configure_weight(self.header_frame, 0, 0, 1)

        self.title_label = DrawLabel( # Titulo do app
            self.header_frame,
            text=app_title,
            anchor='center',
            font=('Impact', 40),
            fg_color='transparent',
            text_color="#FF0000",
        )
        self.title_label.grid(row=0, column=0, sticky='nsew', pady=(10, 0))

        self.credit_label = DrawLabel( # Credito do desenvolvedor
            self.header_frame,
            text="by Astraeus",
            anchor='e',
            font=('Arial', 18),
            fg_color='transparent',
            text_color="#2C2C2C",
        )
        self.credit_label.grid(row=1, column=0, sticky='ew', padx=(0, 10))

    def draw_body(self): # Onde vai ficar o menu, botões e inputs
        self.body = DrawFrame(
            self,
            width=(app_width - 20),
            height=80,
            fg_color="#3A3A3A",
        )
        self.body.grid(row=1, column=0)

        self.input_url = DrawEntry( # Para informar a url ou link
            self.body,
            placeholder_text='Digite a URL/Link',
        )
        self.input_url.grid(row=0, column=0)

        self.submit = DrawButton( # Botão para executar o download com base no url ou link
            self,
            text="Baixar",
            command=self.get_input
        )
        self.submit.grid(row=2, column=0)

    def get_input(self):
        url = self.input_url.get()

        def finished(success, error):
            if success:
                self.alert_top_level = DrawAlert(
                    self.master,
                    text=f"Download concluído com sucesso!",
                    fg_color=error_color,
                    error_text=error,
                )
            else:
                self.alert_top_level = DrawAlert(
                    self.master,
                    text=f"Você informou uma url ou link invalido!",
                    fg_color=error_color,
                    error_text=error,
                )

        yt_dlp_download(url, callback=finished)


class Main(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações basicas
        self.title(app_title)
        self.geometry(f'{app_width}x{app_height}')
        self.resizable(False, False)

        # Configuração do grid
        configure_weight(self, 0, 0, 1)

        # Frame principal
        self.main_frame = MainFrame(self, width=app_width, height=app_height)
        self.main_frame.grid(row=0, column=0, sticky='nsew')


if __name__ == '__main__':
    app = Main()
    app.mainloop()
