class Snake:

    def __init__(self, n, c, l = 10):
        self.name = n
        self.color = c
        self.length = l

    def talk(self):
        print("Hiii!")
    
    def whatIsYourName(self):
        print("My name is", self.name)
    
    def introduceYourself(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("length:", self.length)

s1 = Snake("python", "Green")
s1.talk()
s1.introduceYourself()

s1 = Snake("anaconda", "Red", 9)
s1.talk()
s1.introduceYourself()