import requests
from itertools import groupby
from operator import itemgetter
import csv

CATEGORIES = {
    'BUSINESS': 'business',
    'ENTERTAINMENT': 'entertainment',
    'HEALTH': 'health',
    'SCIENCE': 'science',
    'SPORTS': 'sports',
    'TECHNOLOGY': 'technology'
}

class Fetching():
    def __init__(self,api_key,url_fetch) -> None:
        self.api_key = api_key
        self.url_fetch = url_fetch
        pass
    '''
    return file path
    '''
    def crawlData(self,fromDate='2023-12-12',toDate='2024-01-7'):
        if not self.api_key or not self.url_fetch:
            print("Not provide API KEY or URL")
            return []
        urls = ["https://newsapi.org/v2/everything?q=apple&sortBy=popularity&apiKey=3a6e1c5340c0430f9f5c47c0fa3f747e",
                "https://newsapi.org/v2/everything?q=bitcoin&apiKey=3a6e1c5340c0430f9f5c47c0fa3f747e"]
        # for category in CATEGORIES.keys():
        #     urls.append(f"{self.url_fetch}?from={fromDate}&to={toDate}&category={CATEGORIES[category]}&apiKey={self.api_key}")
        articles =[]
        for url in urls:
            response = requests.get(url)
            response=response.json()
            print(f"{url} \n Totals:{response['totalResults']}")
            articles.extend(response["articles"])
        print(f'Articles:{len(articles)}')
        grouped_articles = {}
        list_key = set([x['publishedAt'][:7] for x in articles])
        for key in list_key:
            grouped_articles[key] = [x for x in articles if x['publishedAt'][:7]==key]
            print(f'{key}:{len(grouped_articles[key])}')

            # Save each group to a CSV file
        file_paths=[]
        for key in grouped_articles.keys():
            csv_filename = f'./app/data/articles_{key}.csv'
            file_paths.append(csv_filename)
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=grouped_articles[key][0].keys())
                csv_writer.writeheader()
                csv_writer.writerows(grouped_articles[key])
        return file_paths