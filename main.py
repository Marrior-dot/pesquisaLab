import pandas as pd
from ntscraper import Nitter

scrap = Nitter()

bully = scrap.get_tweets("bullying", mode="term", number=5)
print(bully)