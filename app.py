#import library
import pandas as pd
import numpy as np
import joblib
import tensorflow as tf
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import string
import ast
from tensorflow.keras.models import load_model
import streamlit as st
from PIL import Image

nltk.download('punkt')
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download('stopwords')
nltk.download('tokenizers')

# Set up app title and header image
st.title('Ulta Skincare Reviews Prediction')
# Tampilkan gambar dengan menggunakan URL
st.image('https://upload.wikimedia.org/wikipedia/commons/b/bc/Cosmetics.JPG', width=100, use_column_width=True)


# open chatwords.txt
with open('chatwords.txt') as f:
    data = f.read()
chatwords =  ast.literal_eval(data)


# open abbreviation.txt
with open('abbreviation.txt') as abb:
    ab2 = abb.read()
abbreviation =  ast.literal_eval(ab2)

# define stopwords
stop_words = stopwords.words('english')

# define lemmatizer
lem = WordNetLemmatizer()

# Load Model
final_lstm= tf.keras.models.load_model('model_lstm')

# Import Functions
def check_chatwords(text):
    temp=[]
    for chat in text.split():
        if chat.upper() in chatwords:
            temp.append(chatwords[chat.upper()])
        else:
            temp.append(chat)
    return " ".join(temp)

def lower(text):
    data = text.lower()
    return data 

def check_abbr(text):
    temp2=[]
    for abbr in text.split():
      if abbr in abbreviation:
          temp2.append(abbreviation[abbr])
      else:
          temp2.append(abbr)

    return " ".join(temp2)

def check_punctuation(text):
    data = re.sub("[^a-zA-Z]",' ', text)
    data = re.sub('[[^]]*]', ' ', data)
    data = re.sub(r"\n", " ", data)
    data = data.strip()
    data = ' '.join(data.split())
    return data

def token_stopwords_lemma(text):
    tokens = word_tokenize(text)
    stop_words2 = ' '.join([word for word in tokens if word not in stop_words])
    data = [lem.lemmatize(word) for word in stop_words2.split()]
    data = ' '.join(data)
    return data
    

Review_Text = st.text_input('Please input your review here:')
st.write('Review:', Review_Text)

inf =[Review_Text]
df1= pd.DataFrame()
df1['Review_Text'] = inf

df1['Review_Text'] = df1['Review_Text'].apply(lambda j: check_chatwords(j))
df1['Review_Text'] = df1['Review_Text'].apply(lambda k: lower(k))
df1['Review_Text'] = df1['Review_Text'].apply(lambda l: check_abbr(l))
df1['Review_Text'] = df1['Review_Text'].apply(lambda m: check_punctuation(m))
df1['Review_Text'] = df1['Review_Text'].apply(lambda n: token_stopwords_lemma(n))

y_pred_inf = final_lstm.predict(df1['Review_Text'])
y_pred_inf = np.where(y_pred_inf >= 0.5, 1, 0)


# Membuat dataframe dari array
pred_df = pd.DataFrame(y_pred_inf, columns=['label'])


# Melakukan prediksi pada dataframe yang baru dibuat
df_inf2 = pd.DataFrame(df1,columns=['Review_Text'])
df_combined = pd.concat([df_inf2,pred_df], axis=1)


if st.button('Predict'):
    y_pred_inf = final_lstm.predict(df1['Review_Text'])
    y_pred_inf = np.where(y_pred_inf >= 0.5, 1, 0)
    spam_status = str(y_pred_inf[0][0])
    
    if spam_status == "0":
        st.success("Verified.")
    else:
        st.error("Not Verified.")