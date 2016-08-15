"""
Mandeep FalFair
"""

name = input("Enter a name")
while len(name)== 0:
    name = input ("Enter a name")

for i in range (0, len(name), 2):
    print (name[i], end= '')


