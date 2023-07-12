# HMI_JobSummarizer
Human Machine Interaction Project


Summarizer.py
The code uses the NLTK library to summarize sentences. It begins by importing the FreqDist class from the nltk.probability module and the nlargest function from the heapq module. The FreqDist class is used to create a frequency distribution of the words in the text, and the nlargest function is used to get the top 3 sentences with the highest scores.

The code then initializes an empty dictionary called sentence_scores to store the scores of each sentence. It creates a frequency distribution of the filtered tokens using the FreqDist class. Then, it loops through each sentence in the text and each word in the lowercase version of the sentence. If the word is in the frequency distribution, the score of the sentence is incremented by the frequency of the word. Finally, the nlargest function is used to get the top 3 sentences with the highest scores.

The summary_sentences variable contains the top 3 sentences with the highest scores, and these sentences are joined back into a string using the join() method to form the summary.


lastly, For the frontend we have used flask framework.

