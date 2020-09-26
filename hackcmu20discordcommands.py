from datetime import date
from datetime import time
from datetime import datetime
from dotenv import load_dotenv
import os

# google news api https://newsapi.org/docs

from newsapi import NewsApiClient

# Initialization for News API
load_dotenv()
apiKey = os.getenv('newsApiKey')
newsapi = NewsApiClient(api_key=apiKey)

# news API 
def getArticles(query):
    top_headlines = newsapi.get_top_headlines(q=query,
                                          # sources='bbc-news,the-verge',
                                          # category='general',
                                          language='en',
                                          country='us')
    allArticles = ''
    for i in range(len(top_headlines['articles'])):
        if i > 4:
            break
        url = top_headlines['articles'][i]['url']
        allArticles += f'{url} \n'
    return allArticles

# spotify
import spotipy #https://spotipy.readthedocs.io/en/2.16.0/
from spotipy.oauth2 import SpotifyClientCredentials

import sys
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

def artistSearch(artistName):
    name = artistName
    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    url = results['artists']['items'][0]['external_urls']['spotify']
    if len(items) > 0:
        artist = items[0]
        print(artist['name'], artist['images'][0]['url'], url)
    return url

def songSearch(songName):
    name = songName
    results = spotify.search(q='track:' + name, type='track')
    url = results['tracks']['items'][0]['external_urls']['spotify']
    finalResults = ''
    for i in range(5):
        finalResults += f"{results['tracks']['items'][i]['external_urls']['spotify']} \n"
    return finalResults

def albumSearch(albumName):
    name = albumName
    results = spotify.search(q='album:' + name, type='album')
    url = results['albums']['items'][0]['external_urls']['spotify']
    finalResults = ''
    number = min(3, len(results['albums']['items']))
    for i in range(number):
        finalResults += f"{results['albums']['items'][i]['external_urls']['spotify']} \n"
    return finalResults
