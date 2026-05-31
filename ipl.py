import pandas as pd

matches=pd.read_csv("matches.csv") 
matches=matches.fillna("Not Available") 

def most_wins(): 
  most_winner=matches["winner"].value_counts() 
  team = most_winner.idxmax() 
  wins = most_winner.max() 
  print (f"Team {team} has highest wins of {wins}") 


def most_wins_in_a_season(s):
  season = s 
  most_win = matches[matches["season"] == season]       
  most_win_count=most_win["winner"].value_counts()
  team=most_win_count.idxmax() 
  print(f"Team {team} Won Most Times in {season}") 

def season_winner(s): 
  season = s
  season_last_match=matches[matches["season"]==season].tail(1) 
  winner = season_last_match["winner"].iloc[0]
  print(f"Winner of season {season} is {winner}") 

def match_winner(team_1,team_2,season):
 team1=team_1.title()
 team2=team_2.title()
 season=season
 result= matches[(matches["season"]==season) & 
     (((matches["team1"]==team1) & (matches["team2"]==team2)) |
      ((matches["team1"]==team2) & (matches["team2"]==team1)))] 
 if not result.empty:
    win = str(result["win_by_runs"].iloc[0])+" Runs" if result["win_by_runs"].iloc[0] != 0 else str(result["win_by_wickets"].iloc[0]) +" wickets" 
    print(f"\n\nWinner of the First Match is {result["winner"].iloc[0]}\n"
          f"won by {win}\n"
          f"Toss winner = {result["toss_winner"].iloc[0]} and they have decided to {result["toss_decision"].iloc[0]} first\n"
          f"player of the match = {result["player_of_match"].iloc[0]}\n"
          f"match venue = {result["venue"].iloc[0]} \n\n") 

 if len(result) > 1 :
    win = str(result["win_by_runs"].iloc[1])+" Runs" if result["win_by_runs"].iloc[1] != 0 else str(result["win_by_wickets"].iloc[1]) +" wickets" 
    print(f"Winner of the Second Match is {result["winner"].iloc[1]}\n"
          f"won by {win}\n"
          f"Toss winner = {result["toss_winner"].iloc[1]} and they have decided to {result["toss_decision"].iloc[1]} first\n"
          f"player of the match = {result["player_of_match"].iloc[1]}\n"
          f"match venue = {result["venue"].iloc[1]} ") 
 else: 
     print("no data") 

def main(): 
  print("---------IPL DATA (2008 - 2017)---------") 
  print("\n 1) Most wins so far\n 2) Most wins in a season\n 3) Season Winner\n 4) Match winner\n")    
  option=int(input("Enter your option :")) 
  if option == 1:
    most_wins() 
  elif option == 2: 
    season = int(input("Enter season :"))
    most_wins_in_a_season(season)
  elif option == 3: 
    season = int(input("Enter season :")) 
    season_winner(season)
  elif option == 4: 
    team1=input("Enter First team :")
    team2=input("Enter Second team :") 
    season = int(input("Enter season :")) 
    match_winner(team1,team2,season)
  else : 
    print("Invalid Input")

if __name__ == "__main__":
    main()