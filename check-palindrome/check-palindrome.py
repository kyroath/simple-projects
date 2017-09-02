"""

Check if Palindrome - Checks if the string entered by the user is a palindrome. That is that it reads the same
forwards as backwards like “racecar”

"""

palindromes = []

checked_file = open("checked.txt", "a+")
checked_file.seek(0)

while True:
    word = input("Please enter a word: ")
    if not word.isalpha():
        print("This is not a word!")
        continue

    flag = True

    for i in palindromes:
        if word == i:
            print("Palindrome")
            flag = False
            break

    if not flag:
        break

    del flag

    if word == word[::-1]:
        print("Palindrome")
        checked_file.write(word + '\n')

    else:
        print("Not Palindrome")
    break
