import os
from pytube import YouTube, Playlist

# Solução do problema de restrição de idade
from pytube.innertube import _default_clients
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]
 
# Barra de Progresso de 0 a 100% (Não foi copiada da internet, eu juro, confia)
def on_progress(video_stream, total_size, bytes_remaining):
    total_size = video_stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    print("\r" + "▌" * int(percent) + " " * (100 - int(percent)) + " {}%".format(int(percent)), end='')
 
# "Interface"
def interface():
    print("\nQual tipo de Download?\n")
    print("1 - Mp4 (720p)")
    print("2 - Mp3")

# Inicio
print("\n-------------------------")
print("* Youtube Downloader *")
print("-------------------------\n")

# A unica coisa para mudar aqui dentro é o local de download, se não for definido os arquivos vão estar juntos do ytDownload.py, e a resolução dos videos se vc quiser
while True:

  # Definção se o link é um video ou uma playlist
  link = input("Link p/ baixar: ")
  ytvideo = "youtube.com/watch" 
  ytplaylist = "youtube.com/playlist"

  # Se for um Video normal
  if link.find(ytvideo) != -1:
    interface()
    opt = input("\nOpção: ")
    print("")

    # Variavel do Link e a adição da barra de progresso
    UmVideo = YouTube(link, on_progress_callback=on_progress)
    
    # Baixar em Mp4
    if opt == "1":
      try:
        print(UmVideo.title)
       
        # Como o download será feito, as opções são essas: 
        # res="1080p" | res="720p" | res="360p" | file_extension='mp4' | only_audio=True | .get_highest_resolution()
        VdDownload = UmVideo.streams.filter(res="720p").first()
       
        VdDownload.download()# AQUI VC TROCA O LOCAL DE DOWNLOAD EM ASPAS
        print("\n")
      except:
        print("\nO Link não pode ser baixado.\n")
        continue
      break

    # Baixar em Mp3
    elif opt == "2":
      try:
        print(UmVideo.title)
        VideoDownload = UmVideo.streams.filter(only_audio=True).first()
        ArquivoV = VideoDownload.download()# AQUI VC TROCA O LOCAL DE DOWNLOAD EM ASPAS
        print("\n")

        # Não é copiado da internet, confia
        # Mas aqui eu estou trocando o tipo de arquivo para .mp3
        base, ext = os.path.splitext(ArquivoV) 
        ArquivoN = base + ".mp3"
        os.rename(ArquivoV, ArquivoN)
      except:
        print("\nO Link não pode ser baixado.\n")
        continue
      break

  # Se for uma Playlist
  elif link.find(ytplaylist) != -1:
    interface()
    opt = input("\nOpção: ")
    print('')

    # Mesma coisa, só que a barra de progresso vai dentro do loop
    UmaPlaylist = Playlist(link)
 
    # Baixar em Mp4
    if opt == "1":
      try:
        # Vai rodar a playlist inteira, pegando video por video
        for v in UmaPlaylist:
          # Vou definir o link de cada um dos videos dnv para poder pegar o nome deles
          VideoNaPlaylist = YouTube(v, on_progress_callback=on_progress)

          print(VideoNaPlaylist.title)
          PlDownload = VideoNaPlaylist.streams.filter(res="720p").first()
          PlDownload.download()# AQUI VC TROCA O LOCAL DE DOWNLOAD EM ASPAS
          print("\n")

      except:
        print("\nO Link não pode ser baixado.\n")
        continue
      break

    # Baixar em Mp3
    elif opt == "2":
      try:
        for v in UmaPlaylist:
          VideoNaPlaylist = YouTube(v, on_progress_callback=on_progress)
          print(VideoNaPlaylist.title)
          PlDownload = VideoNaPlaylist.streams.filter(only_audio=True).first()
          ArquivoV = PlDownload.download()# AQUI VC TROCA O LOCAL DE DOWNLOAD EM ASPAS
          print("\n")

          base, ext = os.path.splitext(ArquivoV) 
          ArquivoN = base + ".mp3"
          os.rename(ArquivoV, ArquivoN)
      except:
        print("\nO Link não pode ser baixado.\n")
        continue
      break

  # Se não for nenhum
  else:
    print("\nLink inválido\n")
    continue
