from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Da ist ein Fehler aufgetreten beim Downloaden von deinem Video")
    print("Der Download ist abgeschlossen")

link = input("Füge deinen YouTube Link ein!! URL: ")
Download(link)