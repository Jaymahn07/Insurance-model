import pickle
import streamlit as st
pickle_in = open('rfmodel.pkl', 'rb')
clf = pickle.load(pickle_in)

@st.cache()

def mk_prediction(Age, EstSalary, Gender):
    if Gender == "Male":
        GenderM = 1
        GenderF = 0
    elif Gender == "Female":
        GenderM = 0
        GenderF = 1
        
    prediction = clf.predict([[Age,EstSalary, GenderF, GenderM]])[0]
    if prediction == 0:
        value = " not to purchase the insurance"  

    elif prediction == 1:
        value = " to purchase the insurance"
    return value
        
def main():  
    # frontend
            
    html_temp = """
    <div style ='background-color:blue;padding:13px">
    <img.src = />
    <h1 style = "color:white;text-align:center:"> Insurance Prediction Model</h1>
    </div>
    """  
    st.title(' INSURANCE PREDICITION MODEL')                        
    st.markdown("![](https://www.allerin.com/wp-blog/wp-content/uploads/2017/05/building-effective-machine-learning-models.jpg)")
    st.markdown(html_temp,unsafe_allow_html = True)                        
   
    Age = st.slider('Enter Age', 0,100)
    EstSalary = st.number_input('Enter your salary')
    Gender = st.selectbox('Gender',("Male","Female"))
    result = ""
     
    if st.button("Predict Now"):
        result = mk_prediction(Age, EstSalary, Gender)
        st.success('This client is likely{}'.format(result))
        print("Just test")
        
                        
if __name__ =='__main__':
    main()
 
      
