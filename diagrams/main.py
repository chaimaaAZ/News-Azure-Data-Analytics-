from diagrams import Diagram, Cluster
from diagrams.custom import Custom


with Diagram('News Data Analytics'):
    with Cluster('News Source'):
        news_api = Custom("", "newsapi.png")
        
    news_api 
