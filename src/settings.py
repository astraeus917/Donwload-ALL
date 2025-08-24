import os
import customtkinter as ctk
from .functions import *


# Globais, informações do app
app_title="Download-ALL"
app_width=700
app_height=300

# Cores e estilização
error_color="#A50000"
success_color="#059C00"
info_color="#0047CC"

# Lista de codecs de audio
audio_codec = [
    'mp3',
    'm4a',
    'aac',
    'flac',
    'opus',
    'vorbis',
    'wav',
]

audio_quality = [
    '48',
    '64',
    '96',
    '128',
    '160',
    '192',
    '256',
    '320',
]

video_format = [
    'mp4',
    'mkv',
    'flv',
    'webm',
    'mov',
    'avi',
]

