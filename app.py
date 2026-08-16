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
@st.cache_data
def fetch_poster(game_name):
    # --- Code for fetching by game_id (commented out) ---
    # url = f'https://www.cheapshark.com/api/1.0/games?id={game_id}'
    # try:
    #     response = requests.get(url, headers=headers, timeout=5)
    #     if response.status_code == 200:
    #         data = response.json()
    #         if isinstance(data, dict) and data.get('info', {}).get('thumb'):
    #             return data['info']['thumb']
    # except Exception:
    #     pass

    # --- Fetching poster by game_name ---
    url = 'https://www.cheapshark.com/api/1.0/games'
    params = {'title': game_name}
    headers = {
        'User-Agent': 'GameRecommender/1.0 (Mozilla/5.0)'
    }
    fallback_poster = 'https://placehold.co/400x500/1e1e24/ffffff.png?text=No+Poster+Available'
    try:
        response = requests.get(url, params=params, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # CheapShark title search returns a list of matching games
            if isinstance(data, list) and len(data) > 0 and data[0].get('thumb'):
                return data[0]['thumb']
            elif isinstance(data, dict) and data.get('info', {}).get('thumb'):
                return data['info']['thumb']
    except Exception:
        pass
    return fallback_poster



# Recommend function
def recommend(game):
    games.reset_index(drop=True, inplace=True)
    game_index = games[games['name'] == game].index[0]
    distances = similarity[game_index]

    game_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_games = []
    recommended_games_poster = []

    for i in game_indices:
        game_name = games.iloc[i[0]]['name']
        recommended_games.append(game_name)
        
        # Code for game_id (commented out)
        # games_id = games.iloc[i[0]]['id']
        # recommended_games_poster.append(fetch_poster(games_id))

        # Fetch poster using game_name
        recommended_games_poster.append(fetch_poster(game_name))

    return recommended_games, recommended_games_poster

# Streamlit UI 
st.title("🎮 Game Recommendation System")

selected_game_name = st.selectbox("Select a game to get recommendations:", games['name'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_game_name)
    st.subheader("Recommended Games:")
    cols = st.columns(5)

    for i, col in enumerate(cols):
        with col:
            st.text(names[i])
            st.image(posters[i])


