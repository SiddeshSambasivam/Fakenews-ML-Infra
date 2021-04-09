# import keras
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense,Embedding,LSTM,Dropout
from keras.callbacks import ReduceLROnPlateau
import tensorflow as tf

max_features = 10000
maxlen = 300
embed_size = 100
# weights=[embedding_matrix]

def get_model(load_checkpoint="ckpt"):
    # model = Sequential()
    # #Non-trainable embeddidng layer
    # model.add(Embedding(max_features, output_dim=embed_size, input_length=maxlen, trainable=False))
    # #LSTM 
    # model.add(LSTM(units=128 , return_sequences = True , recurrent_dropout = 0.25 , dropout = 0.25))
    # model.add(LSTM(units=64 , recurrent_dropout = 0.1 , dropout = 0.1))
    # model.add(Dense(units = 32 , activation = 'relu'))
    # model.add(Dense(1, activation='sigmoid'))
    # model.compile(optimizer=keras.optimizers.Adam(lr = 0.01), loss='binary_crossentropy', metrics=['accuracy'])

    # load_status = model.load_weights(load_checkpoint)
    # load_status.assert_consumed()
    model = keras.models.load_model('./checkpoints/my_model')

    return model

# print(get_model())