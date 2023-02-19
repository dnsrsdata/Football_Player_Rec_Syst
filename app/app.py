# Importing the libraries
import streamlit as st
import pandas as pd

#%%
# Importing the data
cleaned_data = pd.read_csv('../data/interim/all_players_data_withoutDuplicates.csv', index_col=0)
similarity_df = pd.read_csv('../similarity_results/similarity_df.csv', index_col=0)
#%%
team = st.sidebar.selectbox('Pick a team:', options=cleaned_data.Squad.drop_duplicates())
player_name = st.sidebar.selectbox('Select a player:',
                                   options=cleaned_data.query(f"Squad == '{team}'").Player.drop_duplicates())
rec_qtd = st.sidebar.selectbox('Choose the number of recommendations', options=(5, 10, 15, 20, 25, 30))
st.sidebar.write(":warning: The greater the number of desired recommendations, the lower the accuracy of the recommendations.")
#%%
id_player = cleaned_data.query(f"Player == '{player_name}' & Squad == '{team}'").id.values[0]
indexes = similarity_df.loc[id_player].sort_values(ascending=False).index.to_list()
values = similarity_df.loc[id_player].sort_values(ascending=False).values
data_to_show = cleaned_data.query(f"id == {indexes[1:int(rec_qtd)+1]}")[['Player', 'Age', 'Pos', 'Squad']]
data_to_show['Similarity'] = values[1:rec_qtd+1]
st.header("Find similar players")
st.subheader(f'Players similar to {player_name}:')
st.write(data_to_show.sort_values(by=['Similarity', 'Age'], ascending=False))
#%%

