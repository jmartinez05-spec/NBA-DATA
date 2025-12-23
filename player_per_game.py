#%%
import pandas as pd

#%%

nba_data=pd.read_csv('/Users/jimmymartinez/Library/Mobile Documents/com~apple~CloudDocs/DATA/nba.csv',skiprows=1)
df=pd.DataFrame(nba_data)
print('NBA Data 2020')

df.columns= ['rank','player','position', 'teams','total_points', 'total_games','points_per_game','field_goals','three_point_goals', 'free_shots','born','active_player','hall_of_fame','country']

numeric_cols=['rank','total_points','total_games','points_per_game','field_goals','three_point_goals','free_shots','born','active_player','hall_of_fame']

for col in numeric_cols:
    df[col] = df[col].astype(str).str.replace(',', '').str.strip()
    df[col] = pd.to_numeric(df[col], errors='coerce')
df['ppg_calc']=df['total_points']/df['total_games']
df.head()
df.info()
df.isnull().sum()
df.head(51)
print('Points Per Game Calculator')
df[['player','total_points','total_games','ppg_calc']].sort_values('ppg_calc',ascending=False).head(11)



#%%

#%%
df['ppg_without_free_shots']=df['total_points']-df['free_shots']
df[['player','position','total_points','total_games','ppg_without_free_shots']].sort_values('ppg_without_free_shots',ascending=False).head(11)
#%%
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,10))
sns.regplot(
    x="total_games",
    y="total_points",
    data=df,
    scatter_kws={"alpha": 0.7},
    line_kws={"color": "red"} )
plt.scatter(df["total_games"], df["total_points"], alpha=0.7)
plt.xlabel("Total Games Played")
plt.ylabel("Total Points")
plt.title("Total Games vs Total Points")
plt.show()


#%%
plt.figure(figsize=(6,6))
plt.bar(avg_ppg_country["country"], avg_ppg_country["points_per_game"])
plt.xlabel("Player Country")
plt.ylabel("Average Points Per Game")
plt.title("Average Points Per Game by Country")
plt.xticks(rotation=45)
plt.show()
#%%
