#a biblioteca gtts serve para criar um arquivo de áudio mp3 e transcrever o texto para áudio.
#para instalar a gtts: pip install gtts
from gtts import gTTS
texto = "A lua tem inveja do seu brilho, a aurora deseja seu colorido e eu desejo os seus beijos"
lingua = "pt"
tts = gTTS(texto, lang=lingua)
tts.save("audio.mp3")
#abaixo um código para importar "os" caso tenha instalado o ffmpeg
import os
os.system('ffplay -autoexit -nodisp audio.mp3')