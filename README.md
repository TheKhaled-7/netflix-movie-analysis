# 🎬 Netflix Movies Analysis (1990s) - Python Project

![Histogram of Movie Durations](images/duration_distribution.png)
![Netflix movie data visualization](https://github.com/user-attachments/assets/b7f946a9-771d-4bec-a448-c4b710c61fc4)

## 📌 Project Objectives
This project addresses the main questions about Netflix movies from the nineties:
1. Extraction of films produced in the nineties 
2. extracting the most movie duration that was repeated in this period 
3. Number of short action films (<90 minutes)

## 🔍 Key Findings
| Metric | Value | Insight |
|--------|-------|---------|
| **Total 1990s Movies Analyzed** | `len(theMoviesIn90s)` | Complete dataset of 1990s films |
| **Most Frequent Duration** | 94 mins | Peak in histogram (Mode) |
| **Short Action Movies (<90 mins)** | 15 | 12% of all action films |

## 🛠️ Technical Implementation
### Data Processing
```python
# Cleaned and filtered 1990s movies
movies_90s = df[
    (df['type'] == 'Movie') & 
    (df['release_year'].between(1990, 1999))
]

Statistical Analysis
# Calculated mode of durations
duration_mode = movies_90s['duration'].mode()[0]

# Counted short action films
short_actions = action_movies[action_movies['duration'] < 90].shape[0]

Visualization
plt.hist(movies_90s['duration'], bins=20)
plt.title('1990s Netflix Movies Duration Distribution')

