#%%
import pandas as pd
from sqlalchemy import create_engine







#%%
Nba_data=pd.read_csv('/Users/jimmymartinez/Downloads/archive/Player Per Game.csv')
engine = create_engine("sqlite:///nba.db")
Nba_data.to_sql("player_per_game", engine, if_exists="replace", index=False)
df_check = pd.read_sql("SELECT * FROM player_per_game LIMIT 5;", engine)
print(df_check)



#%%
df_check = pd.read_sql(
    "SELECT * FROM player_per_game WHERE Age >=25 AND pts_per_game >30 AND season==2026 LIMIT 30;",engine )

print(df_check)

#%%
print(' In the league today, there are only 4 players who are averaging more the 30 PPG')
#%%
df_check = pd.read_sql(
    """
    SELECT player, COUNT(*) AS seasons_30_ppg
    FROM player_per_game
    WHERE age > 20
      AND pts_per_game > 30
      AND season >= 2000
      AND g > 65
    GROUP BY player
    ORDER BY seasons_30_ppg DESC
    LIMIT 50;
    """,
    engine
)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
plt.barh(df_check['player'], df_check['seasons_30_ppg'])
plt.xlabel('Number of 30+ PPG Seasons')
plt.title('Players with Multiple 30+ PPG Seasons Since 2000')
plt.gca().invert_yaxis()  # Highest at top
plt.show()

#%%
print('Here are the players who are averaging more the 30 PPG sinch the year 2000 with more then 65 games played.65 games is the minimum amount of games that has to be played to be able to qualify for awards. As you can see SGA, James Harden, and Allen Iverson leads the 2,000s with the most 30ppg seasons.')
#%%
df_check=pd.read_sql(
    'SELECT*FROM player_per_game WHERE g==82 AND season==2025 ORDER BY age DESC LIMIT 200;', engine)
print(df_check)
#%%
print('A very important stat in the NBA is how often can a player stay healthy. Organizations pay these players millions upon millions and when the time comes to play they are injured. The ability to stay healthy and provide your team with the opportunity to win when you are on the court is a very important stat. Out of these 11 players, Chris Paul was the oldest and Bub Carrington (rookie) was the youngest to play in all 82 games.')

#%%
df_check=pd.read_sql(' SELECT* FROM player_per_game WHERE pts_per_game >=20 AND season==2025', engine)
print(df_check)
df_check=pd.read_sql('SELECT COUNT(DISTINCT player) AS num_players FROM player_per_game WHERE season=2025', engine)

print(df_check)
df_check=pd.read_sql('SELECT 58.0/569 AS result;', engine)
print(df_check)
#%%
print('In 2025 there were 58 players that scored over 20 points per game that is about a little more then 10 percent of the league.')

#%%
