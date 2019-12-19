degrees = dict()

with open("census.csv", "r") as file_in:
    for line in file_in:
        fields = line.split(", ")
        degree = fields[3]
        if degree in degrees:
            degrees[degree] += 1
        else:
            degrees[degree] = 1

    for degree, count in degrees.items():
        print("{:5} -- {}".format(count,degree))


