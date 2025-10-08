import streamlit as st
import pandas as pd
import pickle

# Load data

# final(Best)
games_list = pickle.load(open('games_dict(final).pkl', 'rb'))
games = pd.DataFrame(games_list)
similarity = pickle.load(open('similarity(final).pkl', 'rb'))

# games
# games_list = pickle.load(open('games_dict(games).pkl', 'rb'))
# games = pd.DataFrame(games_list)
# similarity = pickle.load(open('similarity(games).pkl', 'rb'))

# Recommend function
def recommend(game):
    games.reset_index(drop=True, inplace=True)
    game_index = games[games['name'] == game].index[0]
    distances = similarity[game_index]

    game_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:8]

    recommended_games = []
    for i in game_indices:
        recommended_games.append(games.iloc[i[0]]['name'])
    return recommended_games

# Streamlit UI
st.title("🎮 Game Recommendation System")

selected_game_name = st.selectbox("Select a game to get recommendations:", games['name'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_game_name)
    st.subheader("Recommended Games:")
    for game in recommendations:
        st.write(game)
