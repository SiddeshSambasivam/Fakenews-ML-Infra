import os
import pickle
from keras.preprocessing import text, sequence

max_features = 10000
maxlen = 300


with open('./model/checkpoints/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

#Removing the stopwords from text
def remove_stopwords(text):
    final_text = []
    for i in text.split():
        if i.strip().lower() not in stop:
            final_text.append(i.strip())
    return " ".join(final_text)

#Removing the noisy text
def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    text = remove_stopwords(text)
    return text

def tokenize_inputs(sents:list):

    tokenized_test = tokenizer.texts_to_sequences(sents)
    X_test = sequence.pad_sequences(tokenized_test, maxlen=maxlen)
    
    return X_test
