from datetime import date
from datetime import time
from datetime import datetime
from dotenv import load_dotenv
import os

# google news api

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
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#client_id = os.getenv('spotifyClientId')
#SPOTIPY_CLIENT_SECRET = os.getenv('spotifyClientSecret')

# lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# results = spotify.artist_top_tracks(lz_uri)

# for track in results['tracks'][:10]:
#     print('track    : ' + track['name'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()


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
    return artist['name'], artist['images'][0]['url'], url

#artistSearch('Cardi B')

def songSearch(songName):
    name = songName
    results = spotify.search(q='track:' + name, type='track')
    #print(results)
    #items = results['track']['items']
    url = results['tracks']['items'][0]['external_urls']['spotify']
    finalResults = ''
    for i in range(5):
        finalResults += f"{results['tracks']['items'][i]['external_urls']['spotify']} \n"
    #if len(items) > 0:
        #track = items[0]
        #print(track['name'], track['images'][0]['url'], url)
    #return track['name'], track['images'][0]['url'], url
    return finalResults

print(songSearch('Bad Guy'))

""" def searchSpotify(query, search):
    if query == 'album': 
    elif query == 'song':
    elif query == 'artist': """

# name = 'Bad Guy'
# results = spotify.search(q='track:' + name, type='track')
# print(results)
# items = results['track']['items']
# url = results['track']['items'][0]['external_urls']['spotify']
# if len(items) > 0:
#     song = items[0]
#     print(track['name'], track['images'][0]['url'], url)