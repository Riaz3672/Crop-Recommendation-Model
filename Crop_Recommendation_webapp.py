import streamlit as st
import pickle
import pandas as pd 
import numpy as np
import seaborn as sns 
crop_model=pickle.load(open('Crop_Recommendation.pkl','rb'))

st.title('Crop Recommendation System')
st.header('Input Variales')
N=st.number_input('Nitrogen')
P=st.number_input('Phosphorus')
K=st.number_input('Postassium')
temperature=st.number_input('Temsperature')
humidity=st.number_input('Humidity')
ph=st.number_input('ph')
rainfall=st.number_input('rainfall')
crop_names = {
    0: 'apple',
    1: 'banana',
    2: 'blackgram',
    3: 'chickpea',
    4: 'coconut',
    5: 'coffee',
    6: 'cotton',
    7: 'grapes',
    8: 'jute',
    9: 'kidneybeans',
    10: 'lentil',
    11: 'maize',
    12: 'mango',
    13: 'mothbeans',
    14: 'mungbean',
    15: 'muskmelon',
    16: 'orange',
    17: 'papaya',
    18: 'pigeonpeas',
    19: 'pomegranate',
    20: 'rice',
    21: 'watermelon'
}

#crop_names={0:'apple',1:'banana',2:'blackgram',3:'chickpea',4:'coconut',5:'coffee',6:'cotton',7:'grapes',8:'jute',9:'kidneybeans',10:'lentil',11:'maize',12:'mango',13:'mothbeans',14:'mungbean',15:'muskmelon',16:'orange',17='papaya',18:'pigeonpeas',19:'pomegranate',20:'rice',21:'watermelon'}
if st.button('Recommended Crop'):
    data={
        'N':[N],
        'P':[P],
        'K':[K],
        'temperature':[temperature],
        'humidity':[humidity],
        'ph':[ph],
        'rainfall':[rainfall]
    }
    df=pd.DataFrame(data)
    prediction=crop_model.predict(df)
    predicted_crop=crop_names[int(prediction[0])]
    st.write("The recommended crop is: ", predicted_crop)



