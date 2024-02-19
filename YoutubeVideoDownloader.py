from tkinter import *
from pytube import YouTube
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import simpledialog
youtube_video_url = ''
l=''

def url():
    global youtube_video_url,l
    youtube_video_url= simpledialog.askstring(title="Enter URL",
                                  prompt="Enter URL of video to download: ")
    b= simpledialog.askstring(title="Name",
                                  prompt="Enter name to save video: ")
    c= simpledialog.askstring(title="Enter path",
                                  prompt="Enter path to save video: ")
    l = Label(root, text="Your Video Is Downloading....\n You Will be promted once done")
    l.config(font=("Courier", 24))
    l.place(x=0, y=200)
    root.update()
    try:

        yt_obj = YouTube(youtube_video_url)

        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

        # download the highest quality video
        filters.get_highest_resolution().download(output_path=c, filename=b)

        showinfo("Installer", "Your Video Is Downloaded")
        l.destroy()

    except Exception as e:
        print(e)
        l = Label(root, text="")
        l.config(font=("Courier", 24))
        l.place(x=0, y=200)
        root.update()
        l = Label(root, text="Error while downloading")
        l.config(font=("Courier", 24))
        l.place(x=0, y=200)


root = Tk()

root.title("Youtube Video Downloader-DakshIndustries")
root.geometry("500x300")
root.configure(background='yellow')
a=Button(text='Enter URL to install',command=url,bg='blue')
a.pack(anchor='center')
root.resizable(width=False, height=False)
root.mainloop()
