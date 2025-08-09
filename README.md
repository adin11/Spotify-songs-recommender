# 🎵 Spotify Songs Recommender  

## 📌Project Overview
A Python-based content-based recommender system that suggests similar songs from a dataset using **TF-IDF** and **cosine similarity**.  
Simply provide a song name, and get a list of recommendations based on **artist**, **album**, and **genre** similarity.  

---

## Features  
- Loads and cleans Spotify track dataset.  
- Removes duplicates and missing values.  
- Extracts meaningful features for similarity computation.  
- Uses **TF-IDF Vectorization** for text-based similarity.  
- Finds top **N most similar songs** using **cosine similarity**.  

---

## 🛠️ Tech Stack  
- **Python 3.x**  
- **Pandas** – Data handling  
- **NumPy** – Numerical processing  
- **scikit-learn** – TF-IDF & similarity calculations  
- **Matplotlib / Seaborn** – Data visualization (optional)  

---

## 📂 Project Structure  
- **dataset.csv** – The csv file consisting of the songs and its meta data
- **recommend.py** – Reproducable python script for generating recommendations
- **Readme.md** – Description of the project 

--- 

## Future Improvements
1. Get the latest data from Spotify Api
2. Train the recommender system on latest songs data
3. Dump the data and the tfidf matrix in .pkl format using joblib library
4. Build a UI using those dumped objects and deploy on any cloud platform


## Run the project locally
1. Clone the repository on your local machine by **git clone url**
2. Navigate to that repository using **cd repo name**
3. Run the recommender.py script
4. Input the song name in terminal
5. Get your similar songs matches based on the song you entered














