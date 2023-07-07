import requests
import json
import itertools
import time
import os

API_KEY = 'RGAPI-ab9db0af-b659-48a4-91ee-b19973008d7c'

SUMMONER_NAME = 'phoneymacaroni'
#NoosaMaan
#RomnarN
#Yun
#Browntissue69
#God Complexes
#1T1T1T1T1T1
#tomseli
#BobbyNugget
#phoneymacaroni

# Constants for rate limiting
REQUESTS_PER_SECOND = 20
REQUESTS_PER_MINUTE = 100

# Global variables for rate limiting
request_counter = 0
request_timestamps = []


def main():
    print(f"Getting players in game with {SUMMONER_NAME}:")
    players = get_players_in_game()
    print("Done\n")
    """
    print("Calculating win rates")
    players_with_win_rates = calculate_win_rates(players)
    print("Done\n")
    """
    print("Calculating losing spree")
    losing_spree =calculate_losing_spree(players)
    print("Done\n")

    folder_name = "dict_txt"

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Created folder: {folder_name}")
    else:
        print(f"Folder {folder_name} already exists. Skipping folder creation.\n")

    current_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    file_name = f"{current_time}.txt"
    file_path = os.path.join(folder_name, file_name)

    with open(file_path, "w") as file:
        json.dump(losing_spree, file, indent=4)

    print(f"Created file: {file_path} with the players_with_win_rates dictionary.")



def make_request(url):
    global request_counter, request_timestamps

    # Check rate limits
    current_timestamp = time.time()
    request_timestamps = [ts for ts in request_timestamps if ts > current_timestamp - 60]

    if len(request_timestamps) >= REQUESTS_PER_MINUTE:
        # Maximum requests per minute reached, wait for rate limit reset
        sleep_time = max(request_timestamps[0] + 60 - current_timestamp, 0)
        time.sleep(sleep_time)
        request_timestamps = []

    if request_counter >= REQUESTS_PER_SECOND:
        # Maximum requests per second reached, wait for rate limit reset
        sleep_time = max(request_timestamps[0] + 1 - current_timestamp, 0)
        time.sleep(sleep_time)
        request_counter = 0
        request_timestamps = []

    # Make the API request
    response = requests.get(url)

    if response.status_code == 200:
        # Update rate limiting variables
        request_counter += 1
        request_timestamps.append(time.time())

        return json.loads(response.text)
    else:
        error_message = json.loads(response.text)
        raise Exception(f"API request failed: {error_message}")



def get_players_in_game():
    REGION = 'euw1'
    base_url = f'https://{REGION}.api.riotgames.com'

    endpoint = f'/lol/summoner/v4/summoners/by-name/{SUMMONER_NAME}'
    url = base_url + endpoint + f'?api_key={API_KEY}'
    data = make_request(url)

    id = data['id']
    puuid = data['puuid']
    accountid = data['accountId']

    endpoint = f'/lol/spectator/v4/active-games/by-summoner/{id}'
    url = base_url + endpoint + f'?api_key={API_KEY}'
    data = make_request(url)

    participants = data['participants']
    player_names = {}

    for participant in participants:
        summoner_name = participant['summonerName']
        endpoint = f'/lol/summoner/v4/summoners/by-name/{summoner_name}'
        url = base_url + endpoint + f'?api_key={API_KEY}'
        data = make_request(url)

        id = data['id']
        accountId = data['accountId']
        puuid = data['puuid']
        name = data["name"]

        player_names[name] = {
            'id': id,
            'accountId': accountId,
            'puuid': puuid,
            'teamId': participant['teamId'],
            'championId': participant['championId']
        }

    return player_names



def calculate_win_rates(players):
    REGION = 'EUROPE'
    base_url = f'https://{REGION}.api.riotgames.com'

    with requests.Session() as session:
        for player_name, player_info in players.items():
            id = player_info['id']
            puuid = player_info['puuid']
            accountId = player_info['accountId']

            endpoint = f'/lol/match/v5/matches/by-puuid/{puuid}/ids'
            url = base_url + endpoint + f'?api_key={API_KEY}'
            data = make_request(url)

            matches = list(itertools.islice(data, 5))  # Limit to 5 matches

            wins = 0
            losses = 0

            for match_id in matches:
                endpoint = f'/lol/match/v5/matches/{match_id}'
                url = base_url + endpoint + f'?api_key={API_KEY}'
                match_data = make_request(url)

                participant_identities = match_data['info']['participants']
                participant_stats = match_data['info']['participants']

                participant_id = None
                for identity in participant_identities:
                    if identity['summonerId'] == id:
                        participant_id = identity['participantId']
                        break

                for stat in participant_stats:
                    if stat['participantId'] == participant_id:
                        if stat['win']:
                            wins += 1
                        else:
                            losses += 1

                time.sleep(0.5)  # Pause for 0.5 seconds between each match request

            total_games = wins + losses
            win_rate = (wins / total_games) * 100 if total_games > 0 else 0
            players[player_name]['win_rate'] = win_rate

    return players



def calculate_losing_spree(players):
    REGION = 'EUROPE'
    base_url = f'https://{REGION}.api.riotgames.com'

    with requests.Session() as session:
        for player_name, player_info in players.items():
            id = player_info['id']
            puuid = player_info['puuid']
            accountId = player_info['accountId']

            endpoint = f'/lol/match/v5/matches/by-puuid/{puuid}/ids'
            url = base_url + endpoint + f'?api_key={API_KEY}'
            data = make_request(url)

            matches = list(itertools.islice(data, 7))  # Limit 

            current_streak = 0
            win_streak = 0
            loss_streak = 0

            for match_id in matches:
                endpoint = f'/lol/match/v5/matches/{match_id}'
                url = base_url + endpoint + f'?api_key={API_KEY}'
                match_data = make_request(url)

                participant_identities = match_data['info']['participants']
                participant_stats = match_data['info']['participants']

                participant_id = None
                for identity in participant_identities:
                    if identity['summonerId'] == id:
                        participant_id = identity['participantId']
                        break

                for stat in participant_stats:
                    if stat['participantId'] == participant_id:
                        if stat['win'] == True:
                            if win_streak == current_streak:
                                current_streak += 1
                                win_streak = max(win_streak, current_streak)
                                loss_streak = 0
                            else:
                                break
                        elif stat['win'] == False:
                            if loss_streak == current_streak:
                                current_streak -= 1
                                loss_streak = max(loss_streak, abs(current_streak))
                                win_streak = 0
                            else:
                                break
                        else:
                            # Handle other result types (e.g., draw, tie) if applicable
                            pass

            if win_streak > 0:
                players[player_name]['win_streak'] = win_streak
            elif loss_streak > 0:
                players[player_name]['loss_streak'] = loss_streak
            else:
                print("You are not currently on a winning or losing streak.")
            
            time.sleep(0.5)  # Pause for 0.5 seconds between each match request

    return players



main()