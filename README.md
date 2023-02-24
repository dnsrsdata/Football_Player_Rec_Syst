# Football Player Recommendation Systems

## Instructions:
Follow the steps below to be able to play the project locally.

The Python version used in this project is 3.9.13. In order for the project to play smoothly, I suggest you are using the same version.
1. Clone the repository
   ```sh
   git clone https://github.com/dnsrsdata/Football_Player_Rec_Syst.git
   ```
2. install the packages
   ```sh
   pip install -r requirements.txt
   ```
3. Run the following command in the app's directory to run your web app
    ```sh
    streamlit run app.py
    ```

3. Go to http://localhost:8501/

## Project Motivation
Every football season, many players stand out in their teams and end up being bought by other teams during the transfer window. This causes several clubs to lose important pieces, making them have to go to the market to look for a replacement. Sometimes, there is no time for a deeper analysis of the players by the clubs, causing many wrong signings to be made.

Therefore, to help clubs and their scouts, this recommendation system was created, taking into account the numbers of each player in his last full season.

## File Descriptions
    - app
    |- app.py  # Python file that runs app
    |
    - data
    | - interim
    | |- all_players_data.csv  # data concatenated into a single file
    | |- all_players_data_withoutDuplicates.csv  # data without duplicate data
    | |- column_Description.txt  # description of some data columns
    |- processed
    | |- binarized_data.csv  # already split and binarized data
    |- raw
    | |- defense_actions_bg5.csv  # premier league, la liga, liga 1, serie A Tim and Bundesliga defensive actions
    | |- defense_actions_BrasileiroSerieA.csv  # primeira liga defensive actions
    | |- defense_actions_Eredivisie.csv  # eredivisie defensive actions
    | |- defense_actions_PrimeiraLiga.csv  # brasileiro serie A defensive actions
    | |- goalkeepers_bg5.csv  # premier league, la liga, liga 1, serie A Tim and Bundesliga goalkeeping data
    | |- goalkeepers_BrasileiroSerieA.csv  # brasileiro serie A goalkeeping data
    | |- goalkeepers_Eredivisie.csv  # eredivisie goalkeeping data
    | |- goalkeepers_PrimeiraLiga.csv  # primeira Liga goalkeeping data
    | |- passes_actions_bg5.csv  # premier league, la liga, liga 1, serie A Tim and Bundesliga passes data
    | |- passes_actions_BrasileiroSerieA.csv  # brasileiro Serie A passes data
    | |- passes_actions_Eredivisie.csv  # eredivisie passes data
    | |- passes_actions_PrimeiraLiga.csv  # primeira liga passes data
    | |- shoots_bg5.csv  # premier league, la liga, liga 1, serie A Tim and Bundesliga shooting data
    | |- shoots_BrasileiroSerieA.csv  # brasileiro serie A shooting data
    | |- shoots_Eredivisie.csv  # eredivisie shooting data
    | |- shoots_PrimeiraLiga.csv  # primeira liga shooting data
    |
    - notebooks
    |- EDA.ipynb  # used to perform the exploratory analysis, seeking to get information from the data
    |- ETL_Playground.ipynb  # notebook used to test approaches to the ETL process
    |- RecomenderSys_Playground.ipynb  # used to obtain the correlation matrix and similarity calculation
    |
    - reports
    |- figures
    | |- correlation_age_per_minutes_played.png   # correlation age x minutes played
    | |- correlation_goals_per_passes.png  # correlation goals x passes
    | |- correlation_minutes_per_number_of_players.png # correlation minutes played x number of players
    | |- goals_per_position.png  # goals scored per position
    | |- passes_per_position.png  # passes made by position
    | |- player_distribuition_each_League.png -  # distribution of players by league
    | |- players_per_competition.png  # number of players in each league
    | |- players_per_position  # number of players per position
    |
    - similarity_results
    |- similarity_df.csv  # data containing the similarity of each id to other id
    |
    - README.md  # file containing project information
    - requirements.txt # file containing the necessary packages for the project to work

## Results
You can check the result by accessing http://localhost:8501/ after following the installation steps.

## Conclusion
This was a challenging project, which required specific and hard-to-obtain data.

After passing this initial barrier, other challenges arose during data processing, where the mid-season window generated movement of players between clubs, causing duplicate data to be generated. Such data was difficult to handle, as few fields actually changed, so going through this problem turned out to be challenging and time-consuming.

The other parts proved to be lighter and easier to deal with, as I was able to apply the knowledge obtained previously well, and this rooted the knowledge I already had even more.

Finally, we obtained a system that could make life easier for club scouts, helping both in the discovery of new potential players and for quick action after the loss of an important player, a problem that affects most clubs.

## Next Steps
- [❌] Create Python scripts from Notebooks
- [❌] Containerize the project and deploy on AWS
- [❌] Add each player's market value

## Licensing, Authors, Acknowledgements
Must give credit to Fbref for the data. Otherwise, feel free to use the code here as you would like!
