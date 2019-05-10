class Snake:
    name = None
    color = None
    length = 10

    def talk(self):
        print("Hiii!")
    
    def whatIsYourName(self):
        print("My name is", self.name)

s1 = Snake()
s1.name = "python"
s1.color = "Green"
s1.talk()
s1.whatIsYourName()
