import requests
from bs4 import BeautifulSoup



def pull_fox():
    #pulls the page for fox news
    fox_news = requests.get("https://www.foxnews.com/")
    #parses fox news page
    fox_soup = BeautifulSoup(fox_news.content, 'html.parser')
    #gets down to their main stories
    fox_main_content = fox_soup.main
    #this parses down all of the main stories on foxes page
    raw_fox_headline = fox_main_content.find(class_='info')
    #this holds the main fox headline
    fox_headline = raw_fox_headline.a.string
    return fox_headline

def pull_google():
    #pulls google news page, I think it is us news
    google_news = requests.get("https://news.google.com/?hl=en-US&gl=US&ceid=US:en")
    #parses page
    google_soup = BeautifulSoup(google_news.content, 'html.parser')
    #find the main headline
    google_headline = google_soup.find('a', {"class": "DY5T1d"}).string
    return google_headline

def pull_nbc():
    #pulls nbc news page
    nbc_news = requests.get("https://www.nbcnews.com/")
    #parses page
    nbc_soup = BeautifulSoup(nbc_news.content, 'html.parser')
    #find the main headline
    nbc_headline = nbc_soup.find('span', {"class": "headline___38PFH"}).string
    return nbc_headline

def pull_abc():
    #pulls abc news page
    abc_news = requests.get("https://abcnews.go.com/")
    #parses page
    abc_soup = BeautifulSoup(abc_news.content, 'html.parser')
    #refine
    abc_headline = abc_soup.find('article', {"id": "trio-hero-view"})
    #get the headline
    headline = abc_headline.find_all('a')[1].string
    return headline  #not sure why yet but this returns the string with some extra spaces

def pull_bbc():
    #pulls abc news page
    bbc_news = requests.get("https://www.bbc.com/news/world")
    #parses page
    bbc_soup = BeautifulSoup(bbc_news.content, 'html.parser')
    #refine
    bbc_headline = bbc_soup.find('h3', {"class": "gs-c-promo-heading__title gel-paragon-bold gs-u-mt+ nw-o-link-split__text"}).string
    return bbc_headline

def pull_ap():
    #pulls abc news page
    ap_news = requests.get("https://apnews.com/")
    #parses page
    ap_soup = BeautifulSoup(ap_news.content, 'html.parser')
    #refine
    ap_headline = ap_soup.main
    headline = ap_headline.find('div', {'class': 'Body'})
    return headline.find('h1', {'class': 'Component-h1-0-2-57'}).string



def show_all():
    print(f'''
        Fox:
        {pull_fox()}

        Google:
        {pull_google()}

        NBC:
        {pull_nbc()}

        ABC:
        {pull_abc()}

        BBC:
        {pull_bbc()}

        Associated Press:
        {pull_ap()}
        ''')

show_all()

