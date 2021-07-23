from tkinter import *
from tkinter.ttk import *
from pytube import YouTube
import lxml
from lxml import etree

class YoutubeDL(Tk):
    def __init__(self):
        super().__init__()
        self.title("Download Youtube Video")
        self.geometry("400x200")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.url_label = Label()
        self.url_var = StringVar()
        self.progress_label = Label()

        self.create_widgets()

    def create_widgets(self):
        padding = {'padx':1, 'pady':1}
        self.url_label.grid(column=0, row=0, **padding)
        self.url_label.config(text='URL')
        
        url_text = Entry(self, textvariable=self.url_var)
        url_text.grid(column=1, row=0, **padding)

        self.progress_label.grid(column=0, row=1, columnspan=2, **padding)

        Style().configure("TButton", foreground="red", background="white")
        download_button = Button(self, text='Download', command=self.download, style='TButton').grid(column=0, row=2, **padding)
        close_button = Button(self, text='Close', command=self.close, style='TButton').grid(column=1, row=2, **padding)


    def close(self):
        self.destroy()

    def get_video_title(self, link):
        youtube = etree.HTML(urllib.urlopen(link).read())
        video_title = youtube.xpath("//span[@id='eow-title']/@title") #get xpath using firepath firefox addon
        return ''.join(video_title)

    def progress_function(self, chunk, file_handle, bytes_remaining):
        global filesize
        current = ((filesize - bytes_remaining)/filesize)
        percent = ('{0:.1f}').format(current*100)
        progress = int(50*current)
        status = '█' * progress + '-' * (50 - progress)
        load = ' |' + str(status)+ '| ' + str(percent)
        self.progress_label.config(text=load)
    
    def download(self):
        link = self.url_var.get()
        save_path = '~/Download/'
        print(link)
        try: 
            # object creation using YouTube
            # which was imported in the beginning 
            yt = YouTube(link) 
        except: 
            print("Connection Error") #to handle exception 

        # filters out all the files with "mp4" extension 
        video = yt.streams.filter("mp4")
  
        #to set the name of the file
        yt.set_filename(get_video_title(link))  
  
        # get the video with the extension and
        # resolution passed in the get() function 
        video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
        try: 
            # downloading the video 
            video.download(save_path) 
        except: 
            print("Some Error!") 
        print('Task Completed!')

        
        
        
if __name__ == "__main__":
    app = YoutubeDL()
    app.mainloop()
