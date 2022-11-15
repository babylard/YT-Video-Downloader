from pytube import YouTube
class Download:
    def DownloadHigh(link):
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download()
        except:
            print("An error has occurred")
        print("Download has completed successfully.")

    def DownloadLow(link):
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_lowest_resolution()
        try:
            youtubeObject.download()
        except:
            print("An error has occurred")
        print("Download has completed successfully.")

    def DownloadAudio(link):
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_lowest_resolution()
        try:
            youtubeObject.download()
        except:
            print("An error has occurred")
        print("Download has completed successfully.")


    question = input("What resolution do you want? (audioonly/highres/lowres): ")

    if question == 'highres':
        link = input("Video URL: ")
        DownloadHigh(link)
    elif question == 'lowres':
        link = input("Video URL: ")
        DownloadLow(link)
    else:
        link = input("Video URL: ")
        DownloadAudio(link)
        
    


