import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB


os.chdir(r'/home/trevor/Documents/Projects/text_class_data/')
df = pd.read_csv('consumer_complaints.csv')
col = ['product', 'consumer_complaint_narrative']

df = df[col]
df = df[df['consumer_complaint_narrative'].notnull()]

df['category_id'] = df['product'].factorize()[0]

category_id_df = df[['product', 'category_id']].drop_duplicates().sort_values('category_id')
category_to_id = dict(category_id_df.values)

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')
features = tfidf.fit_transform(df.consumer_complaint_narrative)