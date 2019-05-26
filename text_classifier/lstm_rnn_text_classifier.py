import os
import pandas as pd
import re 

os.chdir(r'/home/trevor/Documents/Projects/text_class_data/')
df = pd.read_csv('consumer_complaints.csv')

df = df[df['']]

df = df[df['consumer_complaint_narrative'].notnull()]


#text preprocessing
def text_preprocess(text):

    replace_with_space = re.comple('[/(){}\[\]\|@,;]')
    remove_symbols = re.compile('[^0-9a-z #+_]')
    stop_words = set(stopwords.words('english'))

    #downcasing
    text = text.lower()
    text = replace_with_space.sub(' ', text)
    clean_string = remove_symbols.sub('', text)
    text = (word for word in clean_string.split() if word not in stop_words)


'factx xxx'.replace('x','')