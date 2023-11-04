import streamlit as st
from PIL import Image
import pickle
import numpy as np

st.sidebar.write("Features coming soon...")
st.header("Mech World")
image = Image.open(r"C:\Users\Om sinha\Downloads\ml.jpg")
st.image(image,use_column_width=True)
st.divider()
choice = st.selectbox("select the field",["Regression","Classification"])
if choice=='Regression':
   c = st.radio("select regression model",['LinearRegressor','RandomForestRegressor','KnnRegressor'])
   if c=='LinearRegressor':
      st.write("a linear regression model")
   elif c=='RandomForestRegressor':
      st.write("a randomforest regression model")
   elif c=='KnnRegressor':
      st.write("a KNN regression model")
elif choice=='Classification':
   c = st.radio("select classification model",['LogisticRegression','xgboost','DecisionTree'])
   if c=='LogisticRegression':
      st.write("a logistic regression model")
   elif c=='xgboost':
      st.write("a xgboost classification model")
      load_model = pickle.load(open(r"C:\Users\Om sinha\Downloads\penguin1.sav", 'rb'))

      def predict(input_data):
         d = np.array(input_data)
         d_reshape = d.reshape(1, -1)
         final_pre = load_model.predict(d_reshape)
         print(final_pre)

         if final_pre[0] == 0:
            return 'Adelie'
         elif final_pre[0] == 1:
            return 'Chinstrap'
         else:
            return 'Gentoo'

      def main():

         st.title("penguin species prediction app")

         island = st.text_input("enter island value between 0,1 or 2")
         culmen_length_mm = st.text_input("enter culmen length")
         culmen_depth_mm = st.text_input("enter culmen depth")
         flipper_length_mm = st.text_input("enter flipper length")
         body_mass_g = st.text_input("enter body weight")
         sex = st.text_input("enter sex between 0 or 1")

         species = ''

         if st.button('penguin species'):
            species = predict([island, culmen_length_mm, culmen_depth_mm, flipper_length_mm, body_mass_g, sex])

         if species=='Adelie':
            im1 = Image.open(r"C:\Users\Om sinha\Downloads\adelie.jpg")
            st.image(im1,caption='Adelie',use_column_width=True)
         elif species=='Chinstrap':
            im2 = Image.open(r"C:\Users\Om sinha\Downloads\Chinstrap-penguin.webp")
            st.image(im2,caption='Chinstrap',use_column_width=True)
         else:
            im3 = Image.open(r"C:\Users\Om sinha\Downloads\gentoo.jpg")
            st.image(im3, caption='Gentoo', use_column_width=True)

      if __name__ == '__main__':
         main()
   elif c=='DecisionTree':
      st.write("a decision tree classification model")




