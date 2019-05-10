class Music:
    def __init__(self, title, artist, album):
        self.__artist = artist
        self.__title = title
        self.__album = album
        self.__artist = ""
        self.__title = ""
        self.__album = ""
        self.__trackLength = 0
        self.__genre = ""
        self.__trackNumber = 0
        self.__size = 0
        self.__lyrics = ""
        self.__isFavourite = False

    def printDetails(self):
        print("Artist: ", self.__artist)
        print("Title: ", self.__title)
        print("Album: ", self.__album)
        print("genre: ", self.__genre)


    def play(self):
        print(self.__title, "is playing....")

    def getLyrics(self):
        print(self.__lyrics)

    def SetFavorite(self):
        self.__isFavourite = True

    def isFavourite(self):
        return self.isFavourite


m1 = Music("Thunder", "Imagine Dragons", "Evolve")
m2 = Music("Different World", "Alan Walker", "Different World")
m3 = Music("Leave Out All The Rest", "Linkin Park", "Minutes To Midnight")
m4 = Music("My Immortal", "Evanescence", "Fallen")

m2.play()
#print(m2.artist)
#print(m2.__artist)
m1.printDetails()
m3.SetFavorite()
print(m3.isFavourite)





