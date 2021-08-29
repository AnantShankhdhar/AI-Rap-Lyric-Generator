import os
from pathlib import Path
from unicodedata import name
import lyricsgenius
import sys

ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))

class Genius:
    def __init__(self, client_access_token, timeout, retries, songs_foldername = 'songs'):
        self.songs_foldername = songs_foldername
        self._api_ = lyricsgenius.Genius(client_access_token, timeout=timeout, retries=retries)
    def scrape_artist(self, artist_name: str):
        artist = self._api_.search_artist(artist_name, max_songs=1)
        print(f"stvaram file {artist.name.strip()}")
        f = open(Path(self.songs_foldername, f'{artist.name.strip()}.txt'), 'w')  
        for song in artist.songs:
            f.write("\n" + '*'*50 + "\n")
            f.write(song.title)
            f.write(song.lyrics)
        f.close()
        print(f"done with {artist_name}")

filename = 'wutang.txt'
songs_folder = Path(ROOT_DIR, 'songs', filename[:-4])

#Add you genius api key where your_api_key is mentioned
genius = Genius("your_api_key", songs_foldername = songs_folder, timeout = 15, retries = 30)

try:
    os.makedirs(songs_folder)
except:
    pass #folder already exists irrelevant error tbh

with open(Path(ROOT_DIR, 'data', filename)) as f:
    for rapper in [line.strip() for line in f.readlines()]:
        genius.scrape_artist(rapper)
