print("Welcome to my calcutor")


def count_vowels(s):
    numA = s.count("a")
    numE = s.count("e")
    numI = s.count("i")
    numO = s.count("o")
    numU = s.count("u")
    numY = s.count("y")
    sumVowels = numA + numE + numI + numO + numU + numY
    return sumVowels

def count_total(s):
    return

print(count_vowels("Hello there, you exist"))

countNum = count_vowels("Hello there, you exist")
print(countNum)
