"""

Count Vowels - Enter a string and the program counts the number of vowels in the text. For added complexity have it
report a sum of each vowel found.

"""

vowels = ['a', 'e', 'i', 'o', 'u']

vowel_count = 0

file = open('count-vowels.txt','a+')

while True:
    word = input("Please enter a word: ")
    if not word.isalpha():
        print("This is not a word!")
        continue
    for i in vowels:
        for j in word:
            if i == j:
                vowel_count += 1
    file.write("The vowel count of '%s' is '%d'\n" % (word, vowel_count))
    print("Vowel count is:", vowel_count)
    break

file.close()