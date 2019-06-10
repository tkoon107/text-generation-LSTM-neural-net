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
n_chars = len(text)
n_vocab = len(unique_chars)

SEQ_LENGTH = 100

dataX = []
dataY = []

for i in range (0, n_chars - SEQ_LENGTH, 1):
    seq_in = text[i: i + SEQ_LENGTH]
    seq_out = text[i + SEQ_LENGTH]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])

n_sequences = len(dataX)
X = numpy.reshape(dataX, (n_sequences, SEQ_LENGTH, 1))
X = X / float(n_vocab)

y = np_utils.to_categorical(dataY)

# define the LSTM model
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

# define the checkpoint

os.chdir("./model_checkpoints")
filepath="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

