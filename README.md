# 🎥 MOVIE Recommender

## Overview
This project is a Machine Learning-powered movie recommendation engine built for the "Fundamentals of AI and ML" BYOP capstone. It uses Natural Language Processing (NLP) and vector mathematics to recommend movies based on their core content (genres, plot, and director) rather than user ratings. 

## The Problem
Mainstream streaming platforms often push generic blockbusters. Finding specific, type films—such as regional cinema, specific director filmographies , or tailored sub-genres—requires a system that understands the *content* of the movie, not just its popularity.

## How It Works
The system uses a **Content-Based Filtering** approach:
1. **Text Vectorization:** Movie metadata (genres, cast, crew, and plot summaries) are combined into a single text "tag". This text is converted into a mathematical matrix using `CountVectorizer`.
2. **Cosine Similarity:** The engine calculates the angle between movie vectors. A smaller angle (cosine score closer to 1) means the movies share similar themes and attributes.
3. **Streamlit UI:** A lightweight web interface allows users to select a movie and instantly view the top 5 closest mathematical matches.

Dataset sourced from Kaggle:https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?resource=download
