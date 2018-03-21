'''

Scraps websites for headlines pertaining to football

'''


# Import necessary libraries
import requests
import datetime
import random
from bs4 import BeautifulSoup


class GetNews:

    def __init__(self):

        # Get data from url
        self.url_guardian = requests.get('https://www.theguardian.com/football')
        self.url_independent = requests.get('http://www.independent.co.uk/sport/football')
        self.url_metro = requests.get('http://metro.co.uk/sport/football/')

    # News from the Guardian
    def get_guardian_news(self):

        # Parse data
        soup_guardian = BeautifulSoup(self.url_guardian.text, 'lxml')

        # Date-time to get sort the data
        # Sorting the data is easier as the Guardian has date in the url
        today = datetime.date.today().strftime('%b/%d').lower()
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        yesterday = yesterday.strftime('%b/%d').lower()

        # Get today's and yesterday's news
        days_lst = [today, yesterday]
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
                        if ('football/live' not in x and 'football/video' not in x and 'football/blog' not in x and
                                'gallery' not in x and 'audio/' not in x):
                            # Pick random headlines
                            rnd_int = random.randint(0, 3)
                            if rnd_int == 0:
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
                if 'Club-by-club' not in y and 'live-score' not in x:
                    # Pick random headlines
                    rnd_int = random.randint(0, 3)
                    if rnd_int == 0:
                        independent_news[x] = y
        return independent_news

    # News from Metro
    def get_metro_news(self):

        # Parse data
        soup_metro = BeautifulSoup(self.url_metro.text, 'lxml')
        results_metro = soup_metro.find_all('h3')

        # Date-time to get sort the data
        # Sorting the data is easier as Metro has date in the url
        today = datetime.date.today().strftime('%m/%d').lower()
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        yesterday = yesterday.strftime('%m/%d').lower()
        days_lst = [today, yesterday]

        # Find the appropriate tags from the parsed data
        records_metro = []
        for element in results_metro:
            a = element.find('a')
            if a is not None:
                records_metro.append(a)
        records_metro_dict = {}
        for element in records_metro:
            text = element.get_text().strip()
            records_metro_dict[element['href']] = text

        # Add appropriate headlines to a dictionary
        metro_news = {}
        while len(metro_news) == 0:
            for x, y in records_metro_dict.items():
                for day in days_lst:
                    if day in x:
                        if 'video' not in x:
                            # Pick random headlines
                            rnd_int = random.randint(0, 3)
                            if rnd_int == 0:
                                metro_news[x] = y
        return metro_news
