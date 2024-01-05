import requests
from itertools import groupby
from operator import itemgetter
import csv
class Fetching():
    def __init__(self,api_key="20db85b15d3b4ecdb61d7e1fd3e9df16",url_fetch="https://newsapi.org/v2/") -> None:
        self.api_key = api_key
        self.url_fetch = url_fetch
        pass
    '''
    return file path
    '''
    def crawlData(self,fromDate='2023-12-12',toDate='2024-01-4'):
        urls = []
        categories = ['business', 'entertainment', 'health', 'science', 'sports', 'technology']
        for category in categories:
            urls.append(f"https://newsapi.org/v2/top-headlines?from={fromDate}&to={toDate}&category={category}&apiKey=api_key")
        articles =[]
        for url in urls:
            response = requests.get(url)
            response=response.json()
            print(len(response["articles"]))
            articles.extend(response["articles"])
        grouped_articles = {}
        for (year, month), group in groupby(articles, key=lambda x: (x['publishedAt'][:4], x['publishedAt'][5:7])):
            month_key = f'{year}-{month}'
            grouped_articles[month_key] = list(group)

            # Save each group to a CSV file
        file_paths=[]
        for date, articles_group in grouped_articles.items():
            csv_filename = f'./app/data/articles_{date}.csv'
            file_paths.append(csv_filename)
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=articles_group[0].keys())
                csv_writer.writeheader()
                csv_writer.writerows(articles_group)
        return file_paths