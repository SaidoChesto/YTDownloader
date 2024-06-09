import os
from pytube import YouTube, Playlist
from pytube.innertube import _default_clients #     Solução do problema de restrição de idade
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]#    Solução parte dois
 
#   Barra de Progresso de 0 a 100% (Não foi copiada da internet, eu juro, confia)
def on_progress(video_stream, total_size, bytes_remaining):
    total_size = video_stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    print("\r" + "▌" * int(percent) + " " * (100 - int(percent)) + " {}%".format(int(percent)), end='')
 
# "Interface"
print("\n-------------------------")
print("* Youtube Downloader *")
print("-------------------------\n")

while True:
  link = input("Link do que você gostaria de baixar: ")
  ytvideo = "youtube.com/watch" # Encontrar uma forma disso funcionar: ytvideo = ["youtube.com/watch", "youtu.be/", "youtube.com/shorts/"]
  ytplaylist = "youtube.com/playlist"

  if link.find(ytvideo) != -1:
    print("\nQual tipo de Download?\n")
    print("1 - Video")
    print("2 - Musica")
    opt = input("\nOpção: ")
    print('')

    if opt == "1":
      try:
        UmVideo = YouTube(link, on_progress_callback=on_progress)# Definindo o link e Adicionando a barra de progresso
        print(UmVideo.title)# Adicionando o titulo do video

        VideoDownload = UmVideo.streams.filter(res="720p").first()
        VideoDownload.download("/Users/diegu/OneDrive/Documentos/[Minhas Coisas]/[03] Midia/[07] Youtube Downloader/Videos")# Definindo o local de download, caso não tenha o local sera no msm do .py
        print("\n")
      except:
        print("\nO Link não pode ser baixado.\n")
        continue
      break
    elif opt == "2":
      try:
        UmVideo = YouTube(link, on_progress_callback=on_progress)
        print(UmVideo.title)

        VideoDownload = UmVideo.streams.filter(only_audio=True).first()
        out_file = VideoDownload.download("/Users/diegu/OneDrive/Documentos/[Minhas Coisas]/[03] Midia/[07] Youtube Downloader/Musica")
        print("\n")

        base, ext = os.path.splitext(out_file) 
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
      except:
        print("\nO Link não pode ser baixado.\n")
        continue
      break

  elif link.find(ytplaylist) != -1:
    print("\nQual tipo de Download?\n")
    print("1 - Videos")
    print("2 - Musicas")
    opt = input("\nOpção: ")
    print('')
 
    if opt == "1":
      try:
        pl = Playlist(link)
        for v in pl:
          print(v)
          yt = YouTube(v, on_progress_callback=on_progress)
          stream = yt.streams.filter(res="720p").first().download("/Users/diegu/OneDrive/Documentos/[Minhas Coisas]/[03] Midia/[07] Youtube Downloader/Videos")
      except:
        print("\nO Link não pode ser baixado.\n")
        continue
      break
    elif opt == "2":
      try:
        pl = Playlist(link)
        for v in pl:
          print(v)
          yt = YouTube(v, on_progress_callback=on_progress)
          stream = yt.streams.filter(only_audio=True).first()
          out_file = stream.download("/Users/diegu/OneDrive/Documentos/[Minhas Coisas]/[03] Midia/[07] Youtube Downloader/Musica")
          print("\n")

          base, ext = os.path.splitext(out_file) 
          new_file = base + '.mp3'
          os.rename(out_file, new_file)
      except:
        print("\nO Link não pode ser baixado.\n")
        continue
      break

  else:
    print("\nLink inválido\n")
    continue