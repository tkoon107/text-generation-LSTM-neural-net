import numpy
import os
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

os.chdir("../project_data/text_gen_data")
file_name = "alice.txt"

text = open(file_name).read()
text = text.lower()

unique_chars =  sorted(list(set(text)))
char_to_int = dict((c,i) for i, c in enumerate(unique_chars))
n_chars = len(raw_text)
n_vocab = len(chars)

SEQ_LENGTH = 100

dataX = []
dataY = []

for i in range (0, n_charis - seq_length, 1):
    seq_in = row_text[i: i + SEQ_LENGTH]
    seq_out = row_text[i + SEQ_LENGTH]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])

n