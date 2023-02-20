# Importing the libraries
import streamlit as st
import pandas as pd

# %%
# Importing the data
cleaned_data = pd.read_csv('../data/interim/all_players_data_withoutDuplicates.csv', index_col=0)
similarity_df = pd.read_csv('../similarity_results/similarity_df.csv', index_col=0)
# %%
# Getting the team and Player name
team = st.sidebar.selectbox('Pick a team:', options=cleaned_data.Squad.drop_duplicates())
player_name = st.sidebar.selectbox('Select a player:',
                                   options=cleaned_data.query(f"Squad == '{team}'").Player.drop_duplicates())

# Getting the amount of recommendations
rec_qtd = st.sidebar.selectbox('Choose the number of recommendations:', options=(5, 10, 15, 20, 25, 30))

# Creating the sidebar
st.sidebar.write(":warning: The further down the table, the more precise the recommendation is.")
# %%
# Fetching the player id
id_player = cleaned_data.query(f"Player == '{player_name}' & Squad == '{team}'").id.values[0]

# Searching players similar to him in the similarity dataset
indexes = similarity_df.loc[id_player].sort_values(ascending=False).index.to_list()

# Removing the player himself from the dice
del indexes[0]

# Getting player position and filtering similar players by position
position = cleaned_data.query(f"id == '{id_player}'").Pos.values[0]
data_to_show = cleaned_data.query(f"id == {indexes}")[['Player', 'Age', 'Pos', 'Squad']]
data_to_show = data_to_show.query(f"Pos == '{position}'")

# Writing the page header and sub header
st.header("Player recommendation system")
st.subheader(f':soccer: Players similar to {player_name}:')

# Showing the table with the recommendations
data_to_show = data_to_show.reset_index().drop(columns='index')
st.write(data_to_show.head(rec_qtd))
# %%
st.subheader(":bar_chart: Check here the statistics of the players in the season:")
possible_choices = data_to_show.head(rec_qtd).Player.to_list()
possible_choices.append(player_name)
choices = st.multiselect("Players", options=possible_choices)
