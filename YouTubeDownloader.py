from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

import pytube
from pytube import Playlist

root = Tk()
urlEntry = IntVar()
setResolutionEntry = IntVar()
chooseContent = IntVar()

def downloadAction():

  url = urlEntry.get()
  resolution = setResolutionEntry.get()

  #You need to set the path to directory using this format(for now).
  pathToDirectory = "C:\\Users\\Cesar\\Videos\\Downloaded Videos"

  if (int(chooseContent.get()) == 0):
    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(res = resolution).first().download(pathToDirectory)
  
  if (int(chooseContent.get()) == 1):

    playlistUrl = Playlist(url)

    for video in playlistUrl.videos:
      video.streams.filter(res = resolution).first().download(pathToDirectory)


# # GUI # #
#Head of GUI window.
root.title("YouTube Downloader")

downloadButton = Button(root, text = "Download", command = downloadAction)
downloadButton.grid(row = 2, column = 2)

#Container for URL.
urlLabel = Label(root, text = "Video URL", font = 'Roboto')
urlLabel.grid(row = 0, column = 0)
urlEntry = Entry(root, font = 'Roboto')
urlEntry.grid(row = 0, column = 1, ipadx = 200)

#Container to set resolution.
setResolutionLabel = Label(root, text = "Resolution", font = 'Roboto')
setResolutionLabel.grid(row = 1, column = 0)

combo = ttk.Combobox(root, font = 'Roboto',values=["240p", "360p", "480p", "720p", "1080p", "1440p", "2160p"])
combo.current(1)
combo.grid(column = 1, row = 1)

#Container to choose between downloading Videos or Playlists
chooseVideoButton = Radiobutton(root, text = "Download a video", variable = chooseContent, value = 0)
chooseVideoButton.grid(row = 2, column = 0)
choosePlaylistButton = Radiobutton(root, text = "Download a playlist", variable = chooseContent, value = 1)
choosePlaylistButton.grid(row = 2, column = 1)


root.resizable(False, False)
root.mainloop()