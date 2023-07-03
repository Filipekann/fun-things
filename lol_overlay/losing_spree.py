import time
from riotwatcher import LolWatcher

#Psudo kod:
"""
Vi kollar först vem är spelaren.
Vilka i hens game är med?
Gör en for loop som går igenom varje spelare förutom sig själv
    I loopen kallar vi på en funktionen suger du
    resultatet från du suger kopplas till spelarens namn via en dict

print dict eller lägg dict i en txt fil som vi kan jobba med sen.
    

def suger du(spelare):
    if sats om spelaren har förlorat flera games i rad:
        return ja han suger.
    else 
        return nä han e bra.


"""

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'RGAPI-6bd202f1-ab1a-4621-af66-aa559db331f8'
region = 'euw1'  # e.g., 'na1', 'euw1', 'kr', etc.

def get_losing_spree_players(summoner_name):
    watcher = LolWatcher(api_key)
    
    try:
        # Retrieve summoner details
        summoner = watcher.summoner.by_name(region, summoner_name)
        
        # Retrieve current game details
        current_game = watcher.spectator.by_summoner(region, summoner['id'])
        
        # Retrieve match history for each player in the current game
        match_history = {}
        for participant in current_game['participants']:
            summoner_id = participant['summonerId']
            match_history[summoner_id] = watcher.match.matchlist_by_account(region, summoner_id)
        
        # Process match history to identify players on a losing spree
        losing_spree_players = []
        for summoner_id, matches in match_history.items():
            lost_games_in_a_row = 0
            for match in matches['matches']:
                match_details = watcher.match.by_id(region, match['gameId'])
                participant_id = None
                for participant_identity in match_details['participantIdentities']:
                    if participant_identity['player']['accountId'] == summoner_id:
                        participant_id = participant_identity['participantId']
                        break
                
                participant_details = match_details['participants'][participant_id - 1]
                if participant_details['stats']['win'] is False:
                    lost_games_in_a_row += 1
                else:
                    lost_games_in_a_row = 0
                    
                if lost_games_in_a_row > 5:
                    losing_spree_players.append(participant_details['summonerName'])
        
        return losing_spree_players
    
    except Exception as e:
        print(f"Error: {e}")
        return []

# Replace 'YOUR_SUMMONER_NAME' with the summoner name you want to check
summoner_name = 'phoneymacaroni'

losing_spree_players = get_losing_spree_players(summoner_name)
if losing_spree_players:
    print(f"Players on a losing spree greater than 5 games in a row: {', '.join(losing_spree_players)}")
else:
    print("No players found on a losing spree greater than 5 games in a row.")
