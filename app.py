import streamlit as st
import joblib
model=joblib.load('model.pkl')
st.title('machine learning project')

sl=st.number_input(label='sepal length',min_value=0.0,max_value=4)
sw=st.number_input(label='sepal width',min_value=10,max_value=2)
pl=st.number_input(label='petal length',min_value=3,max_value=5)
pw=st.number_input(label='petal width',min_value=0.10,max_value=6)
if st.button(label='predict'):
    result=model.predict([[sl,sw,pl,pw]])
    if result==0:
        st.success('setosa')
    elif result==1:
        st.success('versicolor')
    else:
       st.success('verginica')