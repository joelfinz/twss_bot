import pickle
import sys
import pickle
import tensorflow as tf

def eval(sentence):
    with open("tokenizer_new.pickle", "rb") as handle:
        tokenizer = pickle.load(handle)
    
    model = tf.keras.models.load_model("model-1.h5")

    sequence = tokenizer.texts_to_sequences([sentence])
    padded_sequence = tf.keras.preprocessing.sequence.pad_sequences(
        sequence,
        maxlen=100,
        padding="post",
        truncating="post"
    )

    pred_score = model.predict(padded_sequence)
    pred_class = (pred_score > 0.5).astype("int32")

    if pred_class:
        print('That is what she said! ;)')
        print(f'[INFO] pred_class : {pred_class}')
        print(f'[INFO] pred_score : {pred_score}')
    else:
        print('Not a TWSS punchline! :(')
        print(f'[INFO] pred_class : {pred_class}')
        print(f'[INFO] pred_score : {1.0 - pred_score}')

if __name__ == "__main__":
    eval(sys.argv[1])