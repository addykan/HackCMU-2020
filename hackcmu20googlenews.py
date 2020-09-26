# google news api

from newsapi import NewsApiClient
from datetime import date
from datetime import time
from datetime import datetime

today = str(date.today())

# set up 1 month ago
date = '2020-09-25'
month = int(date[5:7])
month -= 1
if month + 1 < 10:
    newMonth = '0'
    newMonth += str(month)
else:
    newMonth = str(month)
newDate = f'{date[0:5]}{newMonth}{date[7:-1]}{str(int(date[-1])+1)}'

# Init
newsapi = NewsApiClient(api_key='493020083d574c64974b2eed15eaa050')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='Biden',
                                          # sources='bbc-news,the-verge',
                                          #category='general',
                                          language='en',
                                          country='us')

# /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param=newDate,
#                                       to=today,
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)
# /v2/sources
# sources = newsapi.get_sources()
#categories = newsapi.get_categories()

# this works!  
# print(type(top_headlines['articles'][0]['url']))
def printArticles():
    allArticles = ''
    for i in range(len(top_headlines['articles'])):
        if i > 4:
            break
        url = top_headlines['articles'][i]['url']
        allArticles += f'{url} \n'
    return allArticles

print(printArticles())
