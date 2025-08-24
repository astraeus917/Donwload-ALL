import yt_dlp


# Função para configurar o peso de row e column
def configure_weight(self, row, column, weight):
    self.grid_propagate(False)
    self.grid_rowconfigure(row, weight=weight)
    self.grid_columnconfigure(column, weight=weight)


def yt_dlp_download(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'bin/output/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': 'bin/ffmpeg',
    }

    # ydl_opts = {
    #     'format': 'bestvideo+bestaudio/best',
    #     'outtmpl': 'bin/output/%(title)s.%(ext)s',
    #     'merge_output_format': 'mp3',
    #     'postprocessors': [{
    #         'key': 'FFmpegVideoConvertor',
    #         'preferedformat': 'mp3',
    #     }],
    #     'ffmpeg_location': 'bin/ffmpeg/',
    # }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print('Baixando')
            return True

        except Exception as error:
            print(error)
            return False




