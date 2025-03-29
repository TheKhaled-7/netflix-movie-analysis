# 🎬 Netflix Movies Analysis (1990s) - Python Project

![Netflix movie data visualization](https://github.com/user-attachments/assets/b7f946a9-771d-4bec-a448-c4b710c61fc4)

## 📌 Project Objectives
This project addresses the main questions about Netflix movies from the nineties:
1. Extraction of films produced in the nineties 
2. extracting the most movie duration that was repeated in this period 
3. Number of short action films (<90 minutes)

## 🔍 Key Findings
| Metric | Value | Insight |
|--------|-------|---------|
| **Total 1990s Movies Analyzed** | 183 Movie | Complete dataset of 1990s films |
| **Most Frequent Duration** | 94 mins | Peak in histogram (Mode) |
| **Short Action Movies (<90 mins)** | 15 | 12% of all action films |

## 🛠️ Technical Implementation
### Data Processing
```python
# Cleaned and filtered 1990s movies
theMoviesIn90s = Netflix_Shows_df[
(Netflix_Shows_df['type'] == 'Movie') &
(Netflix_Shows_df['release_year'] >= 1990) &
(Netflix_Shows_df['release_year'] <= 1999)
]

Statistical Analysis
# Calculated mode of durations
duration_count = theMoviesIn90s['duration'].value_counts()
MostCommonDuration = duration_count.idxmax()

# Counted short action films
short_action_movie_in90s = action_movie_in90s[action_movie_in90s['duration'] < 90].shape[0]

Visualization
plt.hist(theMoviesIn90s['duration'], bins=20, color='blue',  edgecolor='black')
plt.ylabel("Frequency")
plt.xlabel("Duration in minutes")
plt.title("Distribution of Movie Durations in the 90's")
plt.grid(True)


