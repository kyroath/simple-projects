"""

Check if Palindrome - Checks if the string entered by the user is a palindrome. That is that it reads the same
forwards as backwards like “racecar”

"""

while True:
    word = input("Please enter a word: ")
    if not word.isalpha():
        print("This is not a word!")
        continue
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
    break
