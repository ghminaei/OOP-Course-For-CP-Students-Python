class Snake:
    name = None
    color = None
    length = 10

s1 = Snake()
s1.name = "python"
s1.color = "Green"
print(s1.name)
print(id(s1))
s2 = Snake()
s2.name = "anaconda"
s2.color = "Red"
print(id(s2))
print(s2.color)
s2.length = 9
print(s1.length)
print(s2.length)