import pandas as pd
import pandas
import seaborn as sns
import matplotlib.pyplot as plt

# Display more columns in the shell
pandas.set_option('display.max_columns', 10)

# Part 1

# Load data
players = pd.read_csv("basketball_players.csv")
# The "master" data (basketball_master.csv) has names, biographical information, etc.
master = pd.read_csv("basketball_master.csv")

#  Merging the two data sets
players = pd.merge(players, master, how="left", left_on="playerID", right_on="bioID")
print(players.columns)

# Create the throw success rates
players["fgSuccessPercent"] = players["fgMade"] / players["fgAttempted"]
players = players[(players.fgAttempted > 0) & (players.fgSuccessPercent <= 1)]
players["ftSuccessPercent"] = players["ftMade"] / players["ftAttempted"]
players = players[(players.ftAttempted > 0) & (players.ftSuccessPercent <= 1)]
players["threeSuccessPercent"] = players["threeMade"] / players["threeAttempted"]
players = players[(players.threeAttempted > 0) & (players.threeSuccessPercent <= 1)]

"""
    THE GOAT needs to have scored a lot of points.
    He needs great accuracy
    He needs to be a team player, so
    he needs assists, rebounds blocks, and steals
    I am looking for the best well rounded player.
"""

newdat = players[(players.points > 2000) & (players.assists > 400) & (players.steals > 200)]
newdat = newdat[newdat.fgSuccessPercent > .5]
print(newdat[["playerID", "firstName", "lastName", "points", "assists", "steals", "blocks", "fgSuccessPercent", "ftSuccessPercent", "threeSuccessPercent"]].sort_values("points", ascending=False))

# Part 2

# this more exploratory than anything.
# I first found how many players are from each state
print(players["birthState"].value_counts())

# then I looked at california cities
CAdat = players[players.birthState == "CA"]
print(CAdat["birthCity"].value_counts())

# there was a lot from Los Angeles
LAdat = players[players.birthCity == "Los Angeles"]
# I don't see much of a correlation
print(LAdat[["firstName", "lastName", "points", "assists", "steals", "blocks", "fgSuccessPercent", "ftSuccessPercent", "threeSuccessPercent"]].sort_values("points", ascending=False))

# looking a little deeper at LA's data
LAdat = players[players.birthCity == "Los Angeles"]
print(LAdat[["firstName", "lastName", "points", "assists", "steals", "blocks", "fgSuccessPercent", "ftSuccessPercent", "threeSuccessPercent"]].sort_values("points", ascending=False))

# Part 3

# Correlation between points and time
newdat = players[players.minutes >= 0]
sns.relplot(data=newdat, x="minutes", y="points", hue = "GP")
plt.show()

