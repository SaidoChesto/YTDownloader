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
print("-------------------------")
print("* Youtube Downloader *")
print("-------------------------")
print("Qual tipo de Download?")
print("1 - Video")
print("2 - Music Playlist \n")

while True:
    opcao = int(input("Digite a opção: ")) # Seletor

    # Filtros: res="1080p" | res="720p" | res="360p" | file_extension='mp4' | only_audio=True | .get_highest_resolution()

    if opcao == 1:
        link = input("Link: ")
        print("\n")
        UmVideo = YouTube(link, on_progress_callback=on_progress)# Definindo o link e Adicionando a barra de progresso
        print(UmVideo.title)# Adicionando o titulo do video

        VideoDownload = UmVideo.streams.filter(res="720p").first()
        VideoDownload.download("/Users/diegu/OneDrive/Documentos/[Minhas Coisas]/[03] Midia/[07] Youtube Downloader/Videos")# Definindo o local de download, caso não tenha o local sera no msm do .py
        print("\n")
        break

    elif opcao == 2:
        link = input("Link: ")
        print("\n")
        pl = Playlist(link)

        for v in pl:
            print(v)
            yt = YouTube(v, on_progress_callback=on_progress)
            stream = yt.streams.filter(only_audio=True).first().download("/Users/diegu/OneDrive/Documentos/[Minhas Coisas]/[03] Midia/[07] Youtube Downloader/Musica")
            print("\n")
        break

    else: break
    