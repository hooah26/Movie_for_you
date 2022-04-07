import pandas as pd

df = pd.read_csv('./crawling_data/reviews_20222.csv')
print(df.head())
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
df.info()

one_sentences = []
for title in df['title'].unique():
    temp = df[df['title']==title]
    temp = temp['reviews']
    one_sentence = ' '.join(temp)
    one_sentences.append(one_sentence)
df_one_sentences = pd.DataFrame(
    {'titles':df['title'].unique(), 'reviews':one_sentences})
print(df_one_sentences.head())
df_one_sentences.to_csv('./crawling_data/movie_review_onesentence_2018_20222.csv',
                        index=False)





