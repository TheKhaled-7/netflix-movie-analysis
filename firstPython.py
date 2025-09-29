import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Load the dataset
netflix_df = pd.read_csv("netflix_data.csv")

# Filter only movies released in the 1990s (1990–1999)
movies_90s = netflix_df[
    (netflix_df['type'] == 'Movie') &
    (netflix_df['release_year'] >= 1990) &
    (netflix_df['release_year'] <= 1999)
]

# Count how many movies were released in the 1990s
movies_count_90s = movies_90s.shape[0]

# Find the most frequent movie duration in the 1990s
duration_count = movies_90s['duration'].value_counts()
duration = int(duration_count.idxmax())  # save as integer

# Filter short action movies (duration < 90 minutes)
short_action_movies = movies_90s[
    (movies_90s['genre'].str.contains("Action", case=False, na=False)) &
    (movies_90s['duration'] < 90)
]
short_movie_count = short_action_movies.shape[0]

# Print the results
if movies_90s.empty:
    print("No movies found in the 1990s.")
else:
    print(f"Movies in the 1990s: {movies_count_90s}")
    print(f"Most frequent movie duration: {duration} minutes")
    print(f"Number of short action movies (<90 min): {short_movie_count}")

# Plot histogram of movie durations
plt.hist(movies_90s['duration'], bins=20, color='blue', edgecolor='black')
plt.ylabel("Frequency")
plt.xlabel("Duration (minutes)")
plt.title("Distribution of Movie Durations in the 1990s")
plt.grid(True)
plt.show()
