import re

def prompt_filename():
    fileName = input("Please enter the data file:")
    return fileName



def parse_file(fileName):
    count = 0
    with open(fileName) as f:

        # go through each line in the file, one by one
        for line in f:
            # split the line into words based on space (the default delimiter)
            words = line.split()
            print(line)

            # go through each word and see if it matches
            # (yes there are more clever ways to do this...)
            for word in words:
                if re.search("pride", word):
                    count += 1
    return count

def chooseWord(fileName, searchWord):
    count = 0
    with open(fileName) as f:

        # go through each line in the file, one by one
        for line in f:
            # split the line into words based on space (the default delimiter)
            words = line.split()
            print(line)

            # go through each word and see if it matches
            # (yes there are more clever ways to do this...)
            for word in words:
                if re.findall(searchWord, word):
                    count += 1
    return count


def main():
    fileName = prompt_filename()
    print("Opening file: {}\n".format(fileName))
    word = parse_file(fileName)
    print("The word pride occurs {} times in this file\n".format(word))
    searchWord = input("What word do you want to search for: ")
    count = chooseWord(fileName, searchWord)
    print("The word pride occurs {} times in this file".format(count))




if __name__ == "__main__":
   main()