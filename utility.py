import os
import requests
import datetime
from yahoo_fin import stock_info as si

API_KEY     = os.environ['API_KEY']
LIMIT_NEWS  = '100'

CLIENT_ID   = os.getenv('CLIENT_ID')
PERM        = '2148002880'

Invite_URL = f'https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&permissions={PERM}&scope=bot'

def getPrice(ticker):
  price = '0'
  try:
    price = si.get_live_price(ticker)
  except:
    pass
  return price

def getDetails(ticker):
    Detail_URL = f'https://api.polygon.io/v1/meta/symbols/{ticker}/company?&apiKey={API_KEY}'
    Data       = requests.get(Detail_URL).json()

    Logo          = ''
    URL           = ''
    Description   = ''
    Name          = ''
    Industry      = ''
    Symbol        = ''

    try:
      Logo          = Data['logo']
      URL           = Data['url']
      Description   = Data['description']
      Name          = Data['name']
      Industry      = Data['industry']
      Symbol        = Data['symbol']
    except:
      pass
    
    return Logo, URL, Description, Name, Industry, Symbol

def getNews(ticker):
    today = datetime.datetime.utcnow().date()

    yesterday = today - datetime.timedelta(days=3)

    API_URL_NEWS     = f'https://api.polygon.io/v2/reference/news?limit={LIMIT_NEWS}&order=descending&sort=published_utc&ticker={ticker}&published_utc.gte={yesterday}&apiKey={API_KEY}'
    Data = requests.get(API_URL_NEWS).json()

    List_Description   = []
    List_URL_Article   = []
    List_Title         = []
    List_Image_URL     = []

    for i in range(int(LIMIT_NEWS)):
        try:
            newsDes     = Data['results'][i]['description']
            newsURL     = Data['results'][i]['article_url']
            newsTitle   = Data['results'][i]['title']
            image       = Data['results'][i]['image_url']

            List_Description.append(newsDes)
            List_URL_Article.append(newsURL)
            List_Title.append(newsTitle)
            List_Image_URL.append(image)
        except:
            pass

    return List_Description, List_URL_Article, List_Title, List_Image_URL

def getChart(ticker):
  pass
