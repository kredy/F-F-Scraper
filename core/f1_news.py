'''

Scraps websites for headlines pertaining to Formula 1

'''

# Import necessary libraries
import requests
import datetime
import random
from bs4 import BeautifulSoup


class GetNews:

    def __init__(self):

        # Get data from url
        self.url_guardian = requests.get('https://www.theguardian.com/sport/formulaone')
        self.url_independent = requests.get('https://www.independent.co.uk/sport/motor-racing/formula1')
        self.url_bbc = requests.get('http://www.bbc.com/sport/formula1')

    # News from the Guardian
    def get_guardian_news(self):

        # Parse data
        soup_guardian = BeautifulSoup(self.url_guardian.text, 'lxml')

        # Date-time to get sort the data
        # Sorting the data is easier as the Guardian has date in the url
        today = datetime.date.today().strftime('%b/%d').lower()
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        day_before = datetime.date.today() - datetime.timedelta(days=2)
        yesterday = yesterday.strftime('%b/%d').lower()
        day_before = day_before.strftime('%b/%d').lower()

        # Get the most recent news
        days_lst = [today, yesterday, day_before]
        results_guardian = soup_guardian.find_all('h2', attrs={'class': 'fc-item__title'})
        records_guardian = []

        # Find the appropriate tags from the parsed data
        for element in results_guardian:
            a = element.find('a', attrs={'data-link-name': 'article'})
            records_guardian.append(a)
        records_guardian_dict = {}
        for element in records_guardian:
            text = element.get_text().strip()
            records_guardian_dict[element['href']] = text

        # Add appropriate headlines to a dictionary
        guardian_news = {}
        while len(guardian_news) == 0:
            for x, y in records_guardian_dict.items():
                for day in days_lst:
                    if day in x:
                        if 'blog' not in x:
                            guardian_news[x] = y
        return guardian_news

    # News from the Independent
    def get_independent_news(self):

        # Parse data
        soup_independent = BeautifulSoup(self.url_independent.text, 'lxml')
        results_independent = soup_independent.find_all('h1')
        records_independent = []

        # Find the appropriate tags from the parsed data
        for element in results_independent:
            a = element.find('a')
            if a is not None:
                records_independent.append(a)
        records_independent_dict = {}
        for element in records_independent:
            text = element.get_text().strip()
            a = 'http://www.independent.co.uk' + element['href']
            records_independent_dict[a] = text

        # Add appropriate headlines to a dictionary
        independent_news = {}
        while len(independent_news) == 0:
            for x, y in records_independent_dict.items():
                if 'as it happened' not in y and 'live-stream' not in x:
                    rnd_int = random.randint(0, 3)
                    if rnd_int == 0:
                        independent_news[x] = y
        return independent_news

    # News from BBC
    def get_bbc_news(self):

        # Parse data
        soup_bbc = BeautifulSoup(self.url_bbc.text, 'lxml')
        results_bbc = soup_bbc.find_all('h3', attrs={'class': 'lakeside__title faux-block-link__target gel-pica-bold'})
        records_bbc = []

        # Find the appropriate tags from the parsed data
        for element in results_bbc:
            a = element.find('a')
            if a is not None:
                records_bbc.append(a)
        records_bbc_dict = {}
        for element in records_bbc:
            text = element.get_text().strip()
            a = 'http://www.bbc.com' + element['href']
            records_bbc_dict[a] = text

        # Add appropriate headlines to a dictionary
        bbc_news = {}
        while len(bbc_news) == 0:
            for x, y in records_bbc_dict.items():
                # Filtering of headlines still in testing phase
                if 'live' not in x and 'programmes' not in x and 'Podcast' not in y:
                    rnd_int = random.randint(0, 3)
                    if rnd_int == 0:
                        bbc_news[x] = y
        return bbc_news
