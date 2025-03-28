import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
file_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'netflix_data.csv')
Netflix_Shows = pd.read_csv(file_path, index_col=0)
Netflix_Shows_df = pd.DataFrame(Netflix_Shows)

# filter the data for movies released in the 90's
theMoviesIn90s = Netflix_Shows_df[(Netflix_Shows_df['type'] == 'Movie') &
                                  (Netflix_Shows_df['release_year'] >= 1990) &
                                  (Netflix_Shows_df['release_year'] <= 1999)]

# find the most frequent movie duration
duration_count = theMoviesIn90s['duration'].value_counts()
MostCommonDuration = duration_count.idxmax()
if theMoviesIn90s.empty:
    print("No movies found in 90's.")
else:
    print("Movies found in 90's : ")
    print(theMoviesIn90s[['duration']].head())
    print(f"The most frequent movie duration in the 90's is {MostCommonDuration} minutes")
plt.hist(theMoviesIn90s['duration'], bins=20, color='blue',  edgecolor='black')
plt.ylabel("Frequency")
plt.xlabel("Duration in minutes")
plt.title("Distribution of Movie Durations in the 90's")
plt.grid(True)
plt.show()

# count the number of short action movies from the 90's
action_movie_in90s = Netflix_Shows_df[(Netflix_Shows_df['type'] == 'Movie') & 
                                  (Netflix_Shows_df['release_year'] >= 1990) & 
                                  (Netflix_Shows_df['release_year'] <= 1999) & 
                                  (Netflix_Shows_df['genre'].str.contains('Action', case =False))]
short_action_movie_in90s = action_movie_in90s[action_movie_in90s['duration'] < 90].shape[0]
print(f"Number of short action movies in the 90's: {short_action_movie_in90s}")