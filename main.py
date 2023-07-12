import numpy as np
import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from spacy.lang.en.stop_words import STOP_WORDS
import re
from spacy.language import Language
from spacy.lang.en import Language
import DataCleaning

nlp = spacy.load('en_core_web_sm')

separated_jobs = DataCleaning.dataCleaning()

#Printing the separated jobs list
y = 1
for x in separated_jobs:
    print(y, ". " + x)
    y = y + 1
    print("-" * 100)

