import requests
import json
import sqlite3

api_key = 'YOUR_API_KEY'  # Replace with your actual API key
region = 'na1'  # Replace with the desired region

# Connect to the SQLite database
conn = sqlite3.connect('match_data.db')
cursor = conn.cursor()

def fetch_match_data(summoner_name):
    try:
        # Retrieve summoner details
        summoner_url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}'
        summoner_response = requests.get(summoner_url, params={'api_key': api_key})
        summoner_data = json.loads(summoner_response.text)
        summoner_id = summoner_data['id']
        
        # Retrieve match history
        match_history_url = f'https://{region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{summoner_id}'
        match_history_response = requests.get(match_history_url, params={'api_key': api_key})
        match_history_data = json.loads(match_history_response.text)
        
        # Store match data in the database
        for match in match_history_data['matches']:
            match_id = match['gameId']
            match_data_url = f'https://{region}.api.riotgames.com/lol/match/v4/matches/{match_id}'
            match_data_response = requests.get(match_data_url, params={'api_key': api_key})
            match_data = json.loads(match_data_response.text)
            
            # Store relevant match data in the database
            store_match_data(match_data)
        
        print("Match data successfully fetched and stored.")
        
    except Exception as e:
        print(f"Error: {e}")

def store_match_data(match_data):
    # Extract relevant information from the match data
    # Example: Storing match id, participant names, etc.
    match_id = match_data['gameId']
    participant_names = [participant['summonerName'] for participant in match_data['participantIdentities']]
    
    # Store the data in the database
    cursor.execute("INSERT INTO matches (match_id, participant_names) VALUES (?, ?)", (match_id, json.dumps(participant_names)))
    conn.commit()

# Example usage
summoner_name = 'SummonerName'  # Replace with the summoner name you want to fetch match data for
fetch_match_data(summoner_name)

# Close the database connection
conn.close()
