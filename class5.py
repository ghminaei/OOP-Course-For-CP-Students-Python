class Music:

    def __init__(self, title, artist, album):
        self.artist = artist
        self.title = title
        self.album = album
        self.trackLength = 0
        self.genre = ""
        self.trackNumber = 0
        self.size = 0
        self.lyrics = ""
        self.isFavourite = False

    def play(self):
        print(self.title, "is playing....")

    def getLyrics(self):
        print(self.lyrics)
    
    def getTitle(self):
        print(self.title)

    def setFavorite(self):
        self.isFavourite = True

    def setGenre(self, g):
        self.genre = g
        #information hiding

    def getGenre(self):
        return self.genre
        #information hiding


m1 = Music("Thunder", "Imagine Dragons", "Evolve")
m2 = Music("Different World", "Alan Walker", "Different World")
m3 = Music("Leave Out All The Rest", "Linkin Park", "Minutes To Midnight")
m4 = Music("My Immortal", "Evanescence", "Fallen")

m1.play()
print(m2.artist)
m3.setFavorite()
print(m3.title, end = ': ')
print(m3.isFavourite)
print(m4.title, end = ': ')
print(m4.isFavourite)




