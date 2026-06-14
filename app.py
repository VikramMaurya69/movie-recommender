import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_p(title):
    api_key = "6391fe0c"  # <--- PASTE YOUR KEY HERE
    # We are just using title here since extracting year from your pickle might be tricky
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        if data.get('Poster') and data.get('Poster') != 'N/A':
            return data['Poster']
    except Exception as e:
        print(e)

    # Fallback image if OMDb fails or doesn't have the poster
    return "https://via.placeholder.com/500x750?text=No+Poster"





def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies =[]
    recommended_movies_posters = []
    for i in distances[1:6]:
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movie_title)
        recommended_movies_posters.append(fetch_p(movie_title))
    return recommended_movies, recommended_movies_posters


import streamlit as st
import gdown, pickle, os

file_id = "1mbLJK48tcupYmtZuT8kwd8i1I-fnl3y0"
url = f"https://drive.google.com/uc?id={file_id}"
output = "similarity.pkl"

# Show progress bar while downloading
if not os.path.exists(output):
    st.info("Downloading similarity model... please wait ⏳")
    progress = st.progress(0)
    gdown.download(url, output, quiet=False)
    progress.progress(100)
    st.success("Download complete ✅")

similarity = pickle.load(open(output, "rb"))







import streamlit as st

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://drive.google.com/file/d/1mtmDoHbsYtC141xchKFBzzBbcHMZXX30/view?usp=sharing");
    background-size: cover;
    background-position: center;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"] {
    right: 2rem;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)




















movie_dict =pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    "ENTER A MOVIE HERE",
    movies['title'].values,
)
st.write("You selected:", selected_movie_name)




if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    # Create 5 columns to display movies side-by-side
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
