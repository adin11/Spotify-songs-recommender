import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    df = pd.read_csv('dataset.csv')
    print("Rows and columns" ,df.shape)
    return df

def drop_values(df):
    df = df.dropna()
    df = df.drop_duplicates(subset=['track_name'])
    print("Rows and columns after dropping invalid entries",df.shape)
    return df

def preprocess_data(df):
    df = df[['track_name', 'artists', 'album_name', 'track_genre']].copy()  # keeping only relevant columns
    df['data'] = df['artists'] + df['album_name'] + df['track_genre']
    df = df.drop(columns=['artists', 'album_name', 'track_genre'])

    return df

def vectorizer(df):
    from sklearn.feature_extraction.text import TfidfVectorizer

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['data'])
    print(df.shape)
    print("TFIDF Matrix", tfidf_matrix.shape)

    return df, tfidf_matrix
    
def recommend_song(df,song_name,tfidf_matrix,top_n=5):
    from sklearn.metrics.pairwise import cosine_similarity

    index = df[df['track_name'] == song_name].index[0]
    sim_scores = cosine_similarity(tfidf_matrix[index],tfidf_matrix).flatten()
    similar_indices = sim_scores.argsort()[::-1][1:top_n+1]
    similar_songs = df.iloc[similar_indices]['track_name']

    return similar_songs

# Main function    
def main():

    df = load_data()
    df = drop_values(df)
    df = preprocess_data(df)
    df,tfidf_matrix = vectorizer(df)
      
    song_name = input("Enter the song name: ")
    if song_name in df['track_name'].values:
        similar_songs = recommend_song(df,song_name,tfidf_matrix)
        print(f"Here are your suggestions for this song '{song_name}': ")
        print(similar_songs)

    else:
        print("Unaware of the song: Give correct song name and try again")
   
if __name__ == "__main__":
    main() 
    


































