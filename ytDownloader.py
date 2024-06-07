from pytube import YouTube, Playlist
from pytube.innertube import _default_clients #                                 Solução do problema de restrição de idade
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]#        Mesma coisa

def on_progress(video_stream, total_size, bytes_remaining):
    total_size = video_stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    print("\r" + "▌" * int(percent) + " " * (100 - int(percent)) + " {}%".format(int(percent)), end='')

print("-------------------------")
print("* Youtube Downloader *")
print("-------------------------")
print("Select:" )
print("1 - Video")
print("2 - Music Playlist \n")

while True:
    opcao = int(input("Digite a opção: "))

    # Filtros: res="1080p" | res="720p" | res="360p" | file_extension='mp4' | only_audio=True | .get_highest_resolution()

    if opcao == 1:
        link = input("Link: ")
        print("\n")
        videosingular = YouTube(link, on_progress_callback=on_progress)
        print(videosingular.title)

        videodownload = videosingular.streams.filter(res="720p").first()
        videodownload.download("/Users/diegu/OneDrive/Documentos/[Minhas Coisas]/[03] Midia/[07] Youtube Downloader/Videos")
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
    