import streamlit as st
import pandas as pd
import pickle
import requests

# Load data

# final(Best)
games_list = pickle.load(open('games_dict(final).pkl', 'rb'))
games = pd.DataFrame(games_list)
similarity = pickle.load(open('similarity(final).pkl', 'rb'))

# games
# games_list = pickle.load(open('games_dict(games).pkl', 'rb'))
# games = pd.DataFrame(games_list)
# similarity = pickle.load(open('similarity(games).pkl', 'rb'))

## function for fetching the posters of the games
def fetch_poster(game_id):
    response = requests.get('https://api.rawg.io/api/games/{}?key=54476e262ea442878dec3dc702181981'.format(game_id))
    data = response.json()
    return data['background_image'] 



# Recommend function
def recommend(game):
    games.reset_index(drop=True, inplace=True)
    game_index = games[games['name'] == game].index[0]
    distances = similarity[game_index]

    game_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:8]

    recommended_games = []
    recommended_games_poster = []

    for i in game_indices:
        games_id = games.iloc[i[0]]['id']
        recommended_games.append(games.iloc[i[0]]['name'])
        recommended_games_poster.append(fetch_poster(games_id))
    return recommended_games,recommended_games_poster

# Streamlit UI 
st.title("🎮 Game Recommendation System")

selected_game_name = st.selectbox("Select a game to get recommendations:", games['name'].values)

if st.button("Recommend"):
    names ,posters = recommend(selected_game_name)
    st.subheader("Recommended Games:")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0] ,width='content')
    with col2:
        st.text(names[1])
        st.image(posters[1],width='content')
    with col3:
        st.text(names[2])
        st.image(posters[2],width='content')
    with col4:
        st.text(names[3])
        st.image(posters[3],width='content')
    with col5:
        st.text(names[4])
        st.image(posters[4],width='content')

