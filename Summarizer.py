import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import re
from spacy import displacy

import DataCleaning

nlp = spacy.load("en_core_web_sm")


def summarize_jobs(each_job):
    # Remove stopwords and empty spaces, lemmatize, and tokenize using Spacy
    doc = nlp(each_job)
    filtered_tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_space]
    # Join the filtered tokens back into a string
    filtered_text = ' '.join(filtered_tokens)
    # Use spaCy to extract sentences from the filtered text
    doc = nlp(filtered_text)
    sentences = [sent.text for sent in doc.sents]

    # Use NLTK to summarize the sentences
    from nltk.probability import FreqDist
    from heapq import nlargest

    sentence_scores = {}
    # frequency distribution
    fdist = FreqDist(filtered_tokens)

    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in fdist:
                if sent not in sentence_scores:
                    sentence_scores[sent] = fdist[word]
                else:
                    sentence_scores[sent] += fdist[word]

    # Get the top 3 sentences with the highest scores
    summary_sentences = nlargest(3, sentence_scores, key=sentence_scores.get)

    # Join the summary sentences back into a string
    summary = '\n'.join(summary_sentences)
    print(summary)
    print("-" * 400)
    return summary
