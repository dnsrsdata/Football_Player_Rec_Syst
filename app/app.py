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

# Adding a checkbox
agree = st.sidebar.checkbox('I only want to see players who play in the same position.')

# Getting the amount of recommendations
rec_qtd = st.sidebar.selectbox('Choose the number of recommendations:', options=(5, 10, 15, 20, 25))

# Creating the sidebar
st.sidebar.write(":warning: The further down the table, the less precise the recommendation is.")
# %%
# Fetching the player id
id_player = cleaned_data.query(f"Player == '{player_name}' & Squad == '{team}'").id.values[0]

# Searching players similar to him in the similarity dataset
indexes = similarity_df.loc[id_player].sort_values(ascending=False).index.to_list()

# Removing the player himself from the dice
del indexes[0]

# Getting players data
copy_cleaned_data = cleaned_data.set_index('id').copy()
data_to_show = copy_cleaned_data.loc[indexes, ['Player', 'Age', 'Pos', 'Squad']]

# Filtering similar players by position
if agree:
    position = cleaned_data.query(f"id == '{id_player}'").Pos.values[0]
    data_to_show = data_to_show.query(f"Pos == '{position}'")

# Writing the page header and sub header
st.header("Player recommendation system")
st.subheader(f':soccer: Players similar to {player_name}:')

# Showing the table with the recommendations
st.write(data_to_show.head(rec_qtd))
# %%
st.subheader(":bar_chart: Compare player stats from last season:")
possible_choices = data_to_show.head(rec_qtd).Player.to_list()
choices = st.multiselect("Players", options=possible_choices)
choices.append(player_name)

# %%
# Saving a new table
data_to_plot = cleaned_data.set_index('Player').copy()

# Specifying columns by position
fw_stats = ['Gls', 'Sh', 'G/Sh', 'Sh/90']
mf_stats = ['Gls', 'Att_Passes', 'Cmp%', 'Mid 3rd']
df_stats = ['Tkl+Int', 'Blocks', 'Pass']
gk_stats = ['Save%', 'Save%.1']

# Specifying a new columns name
new_fw_columns_name = {'Gls': 'Goals', 'Sh': 'Shoots', 'G/Sh': 'Goals per Shoot', 'Sh/90': 'Shoots per 90 Min'}
new_mf_columns_name = {'Gls': 'Goals', 'Att_Passes': 'Passes Made', 'Cmp%': 'Percentage of Correct Passes',
                       'Mid 3rd': 'Ball Steals in Midfield'}
new_df_columns_name = {'Tkl+Int': 'Steals + Interceptions', 'Blocks': 'Blocks', 'Pass': 'Blocked Passes'}
new_gk_columns_name = {'Save%': 'Percentage of shots saved', 'Save%.1': 'Percentage of penalties saved'}

# Obtaining the position
position = cleaned_data.query(f"Player == '{player_name}'").Pos.values[0][:2]

# Plotting graphs for forwards
if position == 'FW':
    forward_stats = data_to_plot.loc[choices, fw_stats]
    forward_stats = forward_stats.rename(columns=new_fw_columns_name)
    st.bar_chart(forward_stats)

# Plotting graphs for midfielders
elif position == 'MF':
    midfielder_stats = data_to_plot.loc[choices, mf_stats]
    midfielder_stats = midfielder_stats.rename(columns=new_mf_columns_name)
    st.bar_chart(midfielder_stats)

# Plotting graphs for defensors
elif position == 'DF':
    defensor_stats = data_to_plot.loc[choices, df_stats]
    defensor_stats = defensor_stats.rename(columns=new_df_columns_name)
    st.bar_chart(defensor_stats)

# Plotting graphs for goalkeepers
else:
    goalkeeper_stats = data_to_plot.loc[choices, gk_stats]
    goalkeeper_stats = goalkeeper_stats.rename(columns=new_gk_columns_name)
    st.bar_chart(goalkeeper_stats)
