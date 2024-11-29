Movie Recommendation System

This is a Movie Recommendation System built using Python, Streamlit, and machine learning algorithms. The app recommends movies based on the user's input (favorite movie name) using the TMDB (The Movie Database) API. The system utilizes pre-trained movie similarity data and the TMDB API to fetch movie posters and display recommended movies.

Table of Contents
Project Description
Technologies Used
Installation
How to Use
License
Project Description
This project is a simple movie recommendation system that takes the user's favorite movie as input and recommends 5 similar movies. The recommendations are based on movie similarity scores precomputed using collaborative filtering techniques.

The app uses Streamlit for the user interface and integrates with the TMDB API to fetch movie posters dynamically. The app fetches the movie posters based on the movie's unique ID, which is obtained from the TMDB API.

Technologies Used
Streamlit - For building the web application.
Pandas - For data manipulation and analysis.
Scikit-learn - For machine learning algorithms used in computing movie similarities.
TMDB API - For fetching movie details and posters.
Pickle - For loading pre-trained models and movie data.

Installation
Follow the instructions below to set up and run the movie recommendation system on your local machine.

Prerequisites
Python 3.x
A TMDB API Key (You can get it from here)
Steps to Install
Clone the repository:

git clone https://github.com/gfoc/moviesrecommendations.git
cd movie-recommendation-system
Install dependencies:

You can install the required dependencies using pip. Create a virtual environment (optional) and install the following:

pip install -r requirements.txt
If the requirements.txt file is not present, manually install the necessary packages:

pip install streamlit pandas scikit-learn requests
Obtain a TMDB API Key:

Go to the TMDB website.
Create an account and generate your API key.
Replace the api_key in the fetch_poster() function inside the app.py file with your TMDB API key.
Download movie data:

You will need the movies_dict.pkl and similarity.pkl files. These should be pre-generated from the data and similarity model. You can follow the steps below to generate them:

Load your movie data and generate a movie similarity matrix.
Save the data using pickle:
import pickle
pickle.dump(movies_dict, open('movies_dict.pkl', 'wb'))
pickle.dump(similarity_matrix, open('similarity.pkl', 'wb'))
Ensure the dataset contains the required fields like movie_id and title for the movies.

How to Use
After setting up the environment, you can run the Streamlit app using the following command:

streamlit run app.py
The app will open in your default web browser, where you can:

Select a movie from the drop-down list.
Click on the "Recommend" button to see 5 similar movies along with their posters.
You will receive movie recommendations based on the movie you select. Each recommended movie will be displayed along with its poster.

Example
Enter your favorite movie in the input box.
Click the "Recommend" button to see similar movie recommendations.
