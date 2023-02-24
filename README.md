# Football Player Recommendation Systems
## Overview
Football is one of the most popular sports in the world, and therefore it is expected that it moves a lot of money. Much
of that money moves during the transfer windows, when clubs look for players from other teams to join their squad or 
replace an important player.

Because it is short, this transfer window phase, which occurs twice a year, tends to pose a problem for clubs with less 
financial power, as richer clubs can easily take their key players, giving them little time to replace the loss of an 
important player, often leading to wrong signings due to lack of time for the clubs' intelligence centers to work after
the loss.

## About the data
The data used refer to the statistics of players from 8 major leagues in the world, they are:

- Premier League
- La Liga
- Ligue 1
- Bundesliga
- Serie A TIM
- Eredivisie
- Primeira Liga
- Brasileirão Serie A

The data are subdivided into data referring to:
- shooting
- passing
- defensive actions
- goalkeeping

All data were collected on the [Fbref](https://fbref.com/en/) website.

## About the problem
With the opening of the transfer window, many clubs lose important players, and sometimes there is not enough time for 
a quality replacement that really makes sense, as the transfer windows are open for a short period, making clubs 
signings that don't make sense or with a player who doesn't have the same quality as the lost player.

## Solution
Thinking about this problem, a recommendation system would be useful to bring names of players who performed similarly 
to the player that the club lost, making this period of search for substitutes less time consuming and making the club 
replace him with more quality.

## Metrics
To evaluate, I will use the Jaccard index, as I will transform my data into binary vectors, and this metric is suitable 
this, calculating the level of similarity between players.
<br>
<br>
<img src="https://latex.codecogs.com/gif.latex?J(A, B)=\frac {A \cap B}{A \cup B}"/>

## Data characteristic
Although we are working with data from several leagues, we only have 4 datasets, where only 1 contains data from 5 
leagues together.
All have a similar number of lines, varying between 500 and 800, with the exception of the dataset that contains the 
data of the 5 big leagues, which has 6x more lines and 1 additional column, with the name of the league that the player 
belongs to.

A description of each column can be found in the **column_description.txt** file which is located in the following path: 
<i>data/interim</i>

In addition, the periodicity of the transfer window generated a problem of duplicate data in our dataset, which needs to
be handled with care, as there is a great risk of losing relevant data during the treatment process. Another problem 
that is present in the data are missing values, as it is expected, for example, that forwards have goals, but do not 
have saved penalties.

## Data Visualizations
For a better view, you can check the **EDA.ipynb** file in the <i>notebooks</i> folder.

In this file, I sought to use the data to answer the following questions:
- What are the most common player positions?
- Which competition has the most active players?
- Does the player's age directly affect the number of minutes he can play?
- Does a team that keeps the ball and exchanges more passes necessarily have more goals?

## Reflection
This was a challenging project, which required specific and hard-to-obtain data.

After passing this initial barrier, other challenges arose during data processing, where the mid-season window generated movement of players between clubs, causing duplicate data to be generated. Such data was difficult to handle, as few fields actually changed, so going through this problem turned out to be challenging and time-consuming.

The other parts proved to be lighter and easier to deal with, as I was able to apply the knowledge obtained previously well, and this rooted the knowledge I already had even more.

Finally, we obtained a system that could make life easier for club scouts, helping both in the discovery of new potential players and for quick action after the loss of an important player, a problem that affects most clubs.

## Improvement
- [❌] Create Python scripts from Notebooks
- [❌] Containerize the project and deploy on AWS.
- [❌] Add each player's market value

## Instructions:
Follow the steps below to be able to play the project locally.

The Python version used in this project is 3.9.13. In order for the project to play smoothly, I suggest you are using 
the same version.
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

## Licensing, Authors, Acknowledgements
Must give credit to Fbref for the data. Otherwise, feel free to use the code here as you would like!
