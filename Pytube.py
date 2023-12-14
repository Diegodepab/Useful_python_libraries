# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:17:26 2023

@author: DiegoDePab
$ pip install pytubefix 
"""
#Funciones
from pytube import YouTube
import os


def solo_audio(url: str, folder_path: str):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=folder_path, filename=f"{yt.title}.mp4")

def pasa_a_segundos(time_str):
    m, s = map(int, time_str.split(':'))
    return  m * 60 + s #h * 3600 +

#////////////////////////////////////////////////////////////////////////////

#1)Descargar un video de youtube:
# Crear un objeto youtube a través del URL del video
yt = YouTube('https://www.youtube.com/watch?v=YxjY_YTksKM')
# podemos controlar la calidad del video a través de los distintos metodos
stream = yt.streams.get_highest_resolution()
# descargar
stream.download()

#2) Descargar en formato mp4 (solo audio)
#yt=Youtube(Url)    
audio_stream = yt.streams.filter(only_audio=True).first()
audio_stream.download()


#3) Descargar el audio dado un URL de youtube en una carpeta especificada
#solo_audio('url','direccion_de_carpeta')
solo_audio('https://www.youtube.com/watch?v=nJtiYPe9nv4', 'C:\\Users\\Diegodepab\\Music\\Playlists')

#4) Descargar solamente un fragmento de una canción //posible ERROR
yt = YouTube('https://www.youtube.com/watch?v=_aiO6cwPnhg') #url del video
inicio=pasa_a_segundos("11:05") #inicio en minutos (puedes poner segundos directamente)
fin=pasa_a_segundos("13:05")#final en minutos
# obtener la primera secuencia de video con resolución 480p y 30 fps
stream = yt.streams.get_highest_resolution()
# descargar solo los primeros 10 segundos del video
stream.download(filename='video.mp4', skip_existing=False, start_time=inicio, end_time=fin)
# a veces start y end dan problemas mejor usar el propio recorte de youtube

#5) Algunos datos que se pueden obtener del video:
yt= YouTube('https://www.youtube.com/watch?v=r159RLBXaHo')
print(yt.metadata)
print("fin del programa")

#6 subtitulos: (metodo ERRONEO, no encuentro como implementarlo como quiero)
yt=YouTube('https://www.youtube.com/watch?v=yhB3BgJyGl8')
caption = yt.captions.get_by_language_code('en')
print(caption.generate_srt_captions())

'''
invito a colaboracion para ver si con esta biblioteca puede obtenerse subtitulos
'''











