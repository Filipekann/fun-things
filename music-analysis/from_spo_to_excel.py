import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from openpyxl import Workbook
import os
import datetime

def save_playlist_to_excel(client_id, client_secret, playlist_id):
    # Get the directory of the Python script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Create a folder for the playlists
    folder_name = 'playlist_files'
    folder_path = os.path.join(script_directory, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Set up Excel file
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    excel_file = f'playlist_data_{current_time}.xlsx'
    file_location = os.path.join(folder_path, excel_file)

    wb = Workbook()
    ws = wb.active
    ws.append(['Song Name', 'Artist Name'])

    # Authenticate with Spotify
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Retrieve playlist tracks
    results = sp.playlist_tracks(playlist_id)

    # Extract song data
    for item in results['items']:
        track = item['track']
        song_name = track['name']
        artist_name = track['artists'][0]['name']
    
        ws.append([song_name, artist_name])

    # Save Excel file
    wb.save(file_location)

    return file_location
