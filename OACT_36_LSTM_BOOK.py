from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
import numpy as np

raw_text = open('Book.txt', 'r', encoding='utf-8').read() 
raw_text = raw_text.lower()
print(len(raw_text))
print(raw_text[0:1000])

raw_text = ''.join(c for c in raw_text if not c.isdigit())

raw_text=raw_text.replace("$", "")

chars = sorted(list(set(raw_text)))

char_to_int = dict((c, i) for i, c in enumerate(chars))

int_to_char = dict((i, c) for i, c in enumerate(chars))

n_chars = len(raw_text)
n_vocab = len(chars)
print("Total Characters in the text: ", n_chars)
print("Total Vocab: ", n_vocab)

seq_length = 60
step = 10   
sentences = []    
next_chars = []   
for i in range(0, n_chars - seq_length, step):  
    sentences.append(raw_text[i: i + seq_length])  
    next_chars.append(raw_text[i + seq_length])  
n_patterns = len(sentences)    
print('Number of sequences:', n_patterns)


x = np.zeros((len(sentences), seq_length, n_vocab), dtype=bool)
y = np.zeros((len(sentences), n_vocab), dtype=bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_to_int[char]] = 1
    y[i, char_to_int[next_chars[i]]] = 1
    
model = Sequential()
model.add(LSTM(128, input_shape=(seq_length,  n_vocab)))
model.add(Dense(n_vocab, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')

model.fit(x, y, epochs=2)
print(np.argmax(model.predict(x[0:1])))