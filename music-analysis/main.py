from from_spo_to_excel import save_playlist_to_excel
from excel_to_downloaded_mp3 import download_songs_from_excel

client_id = '9e5c31b452ed435797b730b73d283b09'
client_secret = 'fb3d62047ff8423ea523686a550345d6'
playlist_id = 'https://open.spotify.com/playlist/1LkmNFkKQhbPQIhxG1XNZH?si=dc5ecf172d61469c'

excel_file_location = save_playlist_to_excel(client_id, client_secret, playlist_id)

#excel_file_location = 'c:\\Users\\filip\\GitHub Portfolio\\fun-things\\music-analysis\\playlist_files\\playlist_data_2023-06-30_22-38-28.xlsx'

#download_songs_from_excel(excel_file_location)

