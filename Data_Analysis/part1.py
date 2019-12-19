import pandas as pd # Our data manipulation library
import seaborn as sns # Used for graphing/plotting
import matplotlib.pyplot as plt # If we need any low level methods

# load the data
bb_players = pd.read_csv("basketball_players.csv")
print(bb_players.head())
print(bb_players.columns)

# Part 1

# find the mean and median points per season
print("Mean:")
print(bb_players.points.mean())
print("Median:")
print(bb_players.points.median())

# Part 2

# Find the highest number of points per season
# sorted the data set by points and showed the highest 5.
print(bb_players[["playerID", "year", "points"]].sort_values("points", ascending=False).head(5))

# Part 3

# Box plot of rebounds, points, and assists
sns.boxplot(data=bb_players[["rebounds", "points", "assists"]])
plt.show()


# Part 4

# grab the points and years and group by year, then find
# the median of points for each year
nba_grouped_year = bb_players[["points", "year"]].groupby("year").median()
# print it out to see how it looks
print(nba_grouped_year.head())
# reset the index
nba_grouped_year = nba_grouped_year.reset_index()
# checking it one more time
print(nba_grouped_year.head())

# scatter plot
sns.scatterplot(data = nba_grouped_year, x="year", y="points")
plt.show()