import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# importing the dataset
df = pd.read_csv('pizzas.csv')

# creating the model
model = LinearRegression()
x=df[['diametro']]
y = df[['preco']]

model.fit(x, y)

# creating the webpresentation
st.title('Pizza Price Predictor')
st.divider()
st.write('This is a simple app to predict the price of a pizza based on its diameter.')
diameter = st.number_input('Enter the diameter of the pizza in cm:')
price = model.predict([[diameter]])

# Predict button
if st.button('Predict'):
    st.write(f'The predicted price of a pizza with {diameter} cm diameter is R${price[0][0]:.2f}')
    

# Refresh button
if st.button('Refresh'):
    st.empty()  
