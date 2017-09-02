"""
Count Words in a String - Counts the number of individual words in a string.
For added complexity read these strings in from a text file and generate a summary.

"""

from collections import Counter

ind_words = []

while True:

    input_type = input("Do you want to enter the string by hand or from a txt file? \n 'hand' or 'txt':")

    if input_type == "hand":
        string = input("Please enter your string: ")
        break
    elif input_type == "txt":
        print("Important! The txt file should be in the same directory!")

        while True:
            try:
                file_name = input("Please enter the name of your txt file(like file.txt)")
                file = open(file_name, "r")
                break
            except FileNotFoundError:
                print("The file is not in the same directory!")

        string = file.read()
        break
    else:
        print("Please enter a valid input!")

string += " "
word_filled = ""

for i in string:
    if not i.isalpha():
        if word_filled == '':
            continue
        ind_words.append(word_filled)
        word_filled = ""
        continue
    word_filled += i.lower()

word_dict = Counter(ind_words)

result_file = open('results.txt', 'w')

for i in word_dict.most_common():
    print("The word '%s' is used '%d' times." % (i[0], i[1]))
    result_file.write("The word '%s' is used '%d' times.\n" % (i[0], i[1]))

print("The results can also be found in results.txt file!")
