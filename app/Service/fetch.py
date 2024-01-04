class Fetching():
    def __init__(self,api_key,url) -> None:
        self.api_key = api_key
        self.url = url
        self.q = ["apple","tesla"]
        self.qInTitle = [""]
        self.sources = [""]
        self.domains=[""]
        self.endpoint = ["top-headlines","everything"]
        pass
    def createBaseCommonData(self,fromDate):
        urls = [f"https://newsapi.org/v2/everything?q=apple&from={fromDate}&sortBy=popularity&apiKey={self.api_key}",
                f"https://newsapi.org/v2/everything?q=tesla&from={fromDate}&sortBy=publishedAt&apiKey={self.api_key}",
                f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={self.api_key}",
                f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={self.api_key}",
                f"https://newsapi.org/v2/everything?domains=wsj.com&apiKey={self.api_key}"
                ]

