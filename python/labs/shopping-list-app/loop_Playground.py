print ("welcome")


myString = raw_input("Give me a string loop through: ")

letterNum = 1

for character in myString:
    print("This is letter%s" % (letterNum))
    letterNum =letterNum + 1
    print (character)
