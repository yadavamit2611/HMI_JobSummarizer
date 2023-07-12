import spacy
import re
from langdetect import detect


def dataCleaning():
    # Load job offers from file into pandas dataframe
    with open('Assets/eures_job_desc_en.txt', encoding='utf-8') as f:
        contents = f.readlines()

    nlp = spacy.load('en_core_web_sm')

    delimiter = ''
    jobs_string = delimiter.join(contents)
    # jobs_string = jobs_string.replace("\n", " ")
    jobs_string = jobs_string.replace("requirement profile", "requirement profile:")
    separated_jobs = re.split(r"-----", jobs_string)
    separated_jobs = separated_jobs[1:500]

    # Removing Empty Entries
    separated_jobs = [element for element in separated_jobs if element != ""]
#    y = 1

    # Removing non-English Entries
    separated_jobs = [job_ad for job_ad in separated_jobs if is_english(job_ad)]

    return separated_jobs


def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False
