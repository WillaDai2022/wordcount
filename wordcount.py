"""Count words in file."""

# create a function

# open the test.txt file

# for loop to access each line

# tokenized each line to make a list of words (use .split separator " ")

# create an empty dictionary outside loop

# for loop to loop tokenized list

# dict["key"] = dict.get("key", 0) + 1

# use .get() return dictionary
import sys
def word_count():
    filename = sys.argv[1]
    a_file = open(filename)
    a_dict = {}

    for line in a_file:
        line = line.rstrip()
        word_token = line.split(" ")
        for word in word_token:
            a_dict[word] = a_dict.get(word, 0) + 1
    a_file.close()

    for word, count in a_dict.items():
        print(word, count)

    return a_dict

word_count()

# result = word_count('test.txt')

# for info in result:
#     print(f"{info} {result[info]}")

# for word, count in result.items():
#     print(word, count)

# import sys
# filename = sys.argv[1]
# #gives you the flexibility to name your input file when you execute your .py file from
# the command line, rather than hardcoding the name into your program.
# file = open(filename, 'r') #instead of file = open("Data6.txt",'r')
# #for future reference, if you want a file to write to, use 'w'
# lines = file.readlines()
# #returns a list, every line in the file becomes an entry in the list.
# #annoying: newlines are not removed
# for line in lines:
# line.strip() # removes "\n" 