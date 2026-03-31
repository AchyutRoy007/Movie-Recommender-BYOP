# 🎥MOVIE Recommender


## Overview
This is my BYOP (Bring Your Own Project) capstone for the "Fundamentals of AI and ML" course. Instead of using standard numerical data, I wanted to work with Natural Language Processing (NLP). This is a machine learning-powered recommendation engine that suggests movies based on their actual *content*—like the plot, genres, and director—rather than just relying on what is currently trending.

## The Problem I Wanted to Solve
Mainstream streaming platforms are heavily biased toward generic blockbusters. If you are looking for something specific—like gritty regional cinema, a specific director's universe , or a very niche sub-genre—standard recommendation algorithms usually fail because they suffer from the "Cold Start" problem. 

I built this system to actually "read" what a movie is about and find mathematically similar films, making it much easier to discover hidden gems.

## How the Math Works (Content-Based Filtering)
1. **Text Vectorization:** First, I take all the important metadata for a movie (its genres, cast, crew, and plot summary) and mash it together into one giant text "tag". Then, I use `scikit-learn`'s `CountVectorizer` to convert those English words into a massive mathematical matrix.
2. **Cosine Similarity:** To find out if two movies are similar, the engine calculates the angle between their vectors in that matrix. A smaller angle (a cosine score closer to 1.0) means the movies share a lot of the same themes, actors, or directorial styles.
3. **The Web Interface:** I wrapped the whole machine learning pipeline in a lightweight `Streamlit` web app so users can just select a movie from a dropdown and instantly get the top 5 matches.

## A Note on the Development Journey
Building the ML model was only half the challenge of this capstone; the other half was learning proper version control and repository management. Transitioning from simple Python scripts to a structured pipeline came with a real learning curve. 

For instance, I initially struggled with Git tracking when Windows secretly added a `.txt` extension to my `.gitignore` file, almost causing me to push gigabytes of raw CSV data to GitHub! I also had to learn how to properly set up virtual environments inside Jupyter Notebooks just to get `pandas` to load so I could test my vectorization math before deploying the final app. Building this project taught me as much about debugging and standard software engineering practices as it did about AI.

## Repository Structure
* `app.py`: The main Streamlit application and ML pipeline.
* `notebooks/EDA_and_Testing.ipynb`: My rough work and interactive math testing.
* `requirements.txt`: The library dependencies.

*(Note: The full dataset is too massive for GitHub version control. You can download the raw TMDB 5000 movie dataset directly from [Kaggle here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?resource=download)).*

## How to Run This Locally
1. Clone this repository to your machine.
2. Install the required libraries by running: `pip install -r requirements.txt`
3. Launch the web app by running: `streamlit run app.py`
