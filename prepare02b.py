def getFileName():
    filename = input("Enter file: ")
    return filename


def readFile(filename):
    numOfLines = 0
    numOfWords = 0
    with open(filename, "r") as file_in:
        for line in file_in:
            numOfLines += 1
            words = line.split()
            numOfWords += len(words)
    return numOfLines, numOfWords


def main():
    filename = getFileName()
    (numOfLines, numOfWords) = readFile(filename)
    print("The file contains {} lines and {} words.".format(numOfLines, numOfWords))


if __name__ == "__main__":
    main()
