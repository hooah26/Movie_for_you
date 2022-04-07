import pandas as pd
from konlpy.tag import Okt
import re


df = pd.read_csv('./crawling_data/movie_review_onesentence_2018_20222.csv')
# print(df.head)
df.info()

# stopwords = pd.read_csv('./crawling_data/stopwords.csv')
# stopwords_list = list(stopwords['stopword'])
# cleaned_sentences = []
# # print()
# for review in df.reviews:
#     review_word = review.split(' ')
#     words=[]
#     for word in review_word:
#         if word not in stopwords_list:
#             words.append(word)
#     cleaned_sentence = ' '.join(words)
#     cleaned_sentences.append(cleaned_sentence)
# df['cleaned_sentences'] = cleaned_sentences
# df.to_csv('./crawling_data/movie_review_onesentence_2018_202222.csv', index=False)
# # print(df.head())

df.info()
okt = Okt()
cleaned_sentences = []
for sentence in df.reviews:
    sentence = re.sub('^가-힣', '',sentence)
    token = okt.pos(sentence, stem=True)
    print(token)
    df_token = pd.DataFrame(token, columns=[])