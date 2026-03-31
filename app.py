import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load the Data
@st.cache_data 
def load_data():
    
    df = pd.read_csv('dataset.csv')
    
    df['tags'] = df['genres'] + " " + df['production_companies'] + " " + df['tagline']
    return df

df = load_data()

# 2. The Math 
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(df['tags'].fillna('')).toarray()
similarity = cosine_similarity(vectors)

# 3. The Recommendation Function
def recommend(movie_title):
    
    movie_index = df[df['title'] == movie_title].index[0]
    distances = similarity[movie_index]
    
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(df.iloc[i[0]]['title'])
    return recommended_movies

# 4. The User Interface (Streamlit)
st.title("movie recommender 🎥")

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    df['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)