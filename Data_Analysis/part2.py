import pandas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# allows the shell to display more columns
pandas.set_option('display.max_columns', 10)

# Part 1
# read in csv file
players = pd.read_csv("basketball_players.csv")
print(players.columns)

# find field goal success rate
players["fgSuccessPercent"] = players["fgMade"] / players["fgAttempted"]
# find players who have attempted more then 0 shots
players = players[(players.fgAttempted > 0) & (players.fgSuccessPercent <= 1)]

# find free throw success rate
players["ftSuccessPercent"] = players["ftMade"] / players["ftAttempted"]
players = players[(players.ftAttempted > 0) & (players.ftSuccessPercent <= 1)]

# find three throw success rate
players["threeSuccessPercent"] = players["threeMade"] / players["threeAttempted"]
players = players[(players.threeAttempted > 0) & (players.threeSuccessPercent <= 1)]

# The box plot should show the distribution of the rates
sns.boxplot(data=players[["fgSuccessPercent", "ftSuccessPercent", "threeSuccessPercent"]])
plt.show()

# 2 Part

# Players need to have shot over 150 points per season
newdat = players[(players.points > 150)]

# Players need a high shot rate, assists and rebounds

newdat = players[(players.ftSuccessPercent > .6) & (players.fgSuccessPercent > .6) & (players.threeSuccessPercent > .6)]
print(newdat[["playerID", "fgSuccessPercent", "ftSuccessPercent", "threeSuccessPercent", "assists", "rebounds"]])

# Part 3

# make a group by year
grouped = players.groupby('year')
# find the mean and median for each of those years
three_stats = grouped['threeMade'].agg([np.mean, np.median])
# reset index
three_stats = three_stats.reset_index()
# melt the data so that its in long format
three_stats = pd.melt(three_stats, id_vars=["year"], var_name="stat")
# lets check it
print(three_stats)

# This first plot is to show the main distribution across the different leagues.
sns.relplot(data=players, x="year", y="threeMade", hue="lgID")
plt.show()

# This plot helps to show a more general trend and the distribution with  the mean and median.
sns.relplot(data=three_stats, x="year", y="value", hue="stat")
plt.show()
