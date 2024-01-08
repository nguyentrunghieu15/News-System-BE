from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Source(BaseModel):
    id: Optional[str]
    name: str

class NewsArticle(BaseModel):
    source: Source
    author: str
    title: str
    description: str
    url: str
    urlToImage: str
    publishedAt: datetime
    content: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "source": {
                    "id": None,
                    "name": "C21media.net"
                },
                "author": "Natalie Apostolou",
                "title": "HBO commissions space fact and fiction doc from tech journo Ashlee Vance",
                "description": "Warner Bros Discovery-owned HBO is developing a documentary based on technology journalist Ashlee Vance’s book When the Heavens Went on Sale...",
                "url": "https://www.c21media.net/news/hbo-commissions-space-fact-and-fiction-doc-from-tech-journo-ashlee-vance/",
                "urlToImage": "https://cdn.c21media.net/wp-content/uploads/2024/01/ashleevance.jpg",
                "publishedAt": "2024-01-08T09:16:59Z",
                "content": "Ashlee Vance, author of When the Heavens Went on Sale\r\nWarner Bros Discovery-owned HBO is developing a documentary based on technology journalist Ashlee Vance’s book When the Heavens Went on Sale.\r\nTh… [+961 chars]"
            }
        }