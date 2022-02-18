from pytube import YouTube

# yt.streams.filter(only_audio=True,abr="160kbps")[0].download()
# yt.streams.filter(only_video=True,resolution="1080p")[0].download()

while True:
    url = input("Enter a URL: ")
    if url == "q":
        break
    else:
        try:
            yt = YouTube(url)
            yt.streams.filter(progressive=True)[0].download()
        except:
            print("Enter a valid URl!")



