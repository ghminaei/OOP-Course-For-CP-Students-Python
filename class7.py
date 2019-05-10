class Music:
    __artist = ""
    __title = ""
    __album = ""
    __trackLength = 0
    __genre = ""
    __trackNumber = 0
    __size = 0
    __lyrics = ""
    __isFavourite = False

    def __init__(self, title, artist, album):
        self.__artist = artist
        self.__title = title
        self.__album = album

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
        return self.__isFavourite

    def __str__(self):
        return self.__title


class PlayList:
    __name = ""
    __trackCounts = 0
    __musics = None

    def __init__(self, name):
        self.__name = name
        self.__musics = []

    def addToPlayList(self, newMusic):
        self.__musics.append(newMusic)

    def delFromPlayList(self, delMusic):
        self.__musics.remove(delMusic)

    def printMusicList(self):
        print("** ", self.__name, " **")
        for m in self.__musics:
            print(m)


m1 = Music("Thunder", "Imagine Dragons", "Evolve")
m2 = Music("Different World", "Alan Walker", "Different World")
m3 = Music("Leave Out All The Rest", "Linkin Park", "Minutes To Midnight")
m4 = Music("My Immortal", "Evanescence", "Fallen")
m5 = Music("Halo", "Beyonce", "I Am...")
m6 = Music("Hey Hey Hey", "Katy Perry", "Witness")
m7 = Music("Believer", "Imagine Dragons", "Evolve")
m8 = Music("Head Above Water", "Avril", "Head Above Water")
m9 = Music("Magic", "Coldplay", "Ghost Stories")
m10 = Music("Truth Is A Beautiful Thing", "London Grammar", "Truth Is A Beautiful Thing")
m11 = Music("Never Give Up", "Sia", "Lion")

myPlayList1 = PlayList("Cool!")
myPlayList1.addToPlayList(m1)
myPlayList1.addToPlayList(m3)
myPlayList1.addToPlayList(m7)
myPlayList1.addToPlayList(m8)

myPlayList2 = PlayList("coding!")
myPlayList2.addToPlayList(m7)
myPlayList2.addToPlayList(m9)
myPlayList2.addToPlayList(m6)
myPlayList2.addToPlayList(m10)
myPlayList2.addToPlayList(m8)

myPlayList1.printMusicList()
print()
myPlayList2.printMusicList()

myPlayList2.delFromPlayList(m10)
print()
myPlayList2.printMusicList()





