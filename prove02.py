import csv

def getFileName():
    fileName = input("Please enter the data file:")
    return fileName

def readFile(fileName):
     with open(fileName, newline='') as csvfile:
        comm_rate = []
        zipData = []
        state = []
        name = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            comm_rate.append(float(row['comm_rate']))
            zipData.append(int(row['zip']))
            state.append(row['state'])
            name.append(row['utility_name'])

        return (comm_rate,zipData,state,name)


def averageRates(comm_rate):
        Sum = float(sum(comm_rate))
        average = Sum / float(len(comm_rate))
        print("The average commercial rate is: ${}\n".format(str(average)))

def findHighestRate(comm_rate, zipData, state, name):
    length = len(comm_rate)
    a = comm_rate
    max_value = max(a[-length:])
    index = a.index(max_value)
    print("The highest rate is:")
    print("{} ({}, {}) - ${}\n".format(name[index], zipData[index], state[index], max_value))


def findLowestRate(comm_rate, zipData, state, name):
    length = len(comm_rate)
    a = comm_rate
    b = a[-length:]
    min_value = min(b[-length:])
    index = a.index(min_value)
    print("The lowest rate is:")
    print("{} ({}, {}) - ${}".format(name[index], zipData[index], state[index], min_value))



def main():
    fileName = getFileName()
    (comm_rate, zipData, state, name) = readFile(fileName)
    averageRates(comm_rate)
    findHighestRate(comm_rate,zipData,state,name)
    findLowestRate(comm_rate,zipData,state,name)


if __name__ == "__main__":
    main()