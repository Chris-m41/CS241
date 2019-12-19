import pandas

census_data=pandas.read_csv("census.csv", header=None)

print(census_data[0].median())
