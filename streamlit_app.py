import pickle  # Loads the saved machine learning model.
import numpy as np   # Used for numerical operations.
import streamlit as st   # Streamlit for creating the web app.

model = pickle.load(open('model.pkl', 'rb'))  # Loads a pre-trained model from the model.pkl file and puts it in read binary(rb) mode. The model will be used to predict salary.

col0, col1, col2, col3, col4 = st.columns(5)  # Defines the spaces used to place elements in the app (7 horizontal columns)
with col0:
    st.write('')  # empty column 
with col1:
    st.write('')  # empty column
with col2:
     st.title("ⴍage") # The title is placed in the middle column to center it
with col3:
    st.write('')  # empty column
with col4:
    st.write('') 



col5, col6, col7 = st.columns(3)  # Defines space for the subtitles.
with col5:
    st.write('')   # empty column 
with col6:
    st.markdown("<h6 style='text-align: center;'>A simple web app to predict annual salary</h6>", unsafe_allow_html=True)  # Creates a subtitle and centers it

with col7:
    st.write('') # empty column

# These are lists that give users fixed choices for gender, education and job title.
gen_list = ["Female", "Male"]
edu_list = ["Bachelor's", "Master's", "PhD"]
job_list = ["Director of Marketing", "Director of Operations", "Senior Data Scientist", "Senior Financial Analyst", "Senior Software Engineer"]

# Job titles have been encoded into numerical values to match the format used during model training.
job_idx = [0, 1, 10, 11, 20]

# User interface components used to collect user input
gender = st.radio('Pick your gender', gen_list)
age = st.slider('Pick your age', 21, 55)
education = st.selectbox('Pick your education level', edu_list)
job = st.selectbox('Pick your job title', job_list)
experience = st.slider('Pick your years of experience', 0.0, 25.0, 0.0, 0.5, "%1f")

# Columns are created to center the 'Predict Salary' button
col8, col9, col10, col11, col12 = st.columns(5)
with col8:
    st.write('')
with col9:
    st.write('')    
with col10:
    predict_btn = st.button('Predict Salary')
with col11:
    st.write('')
with col12:
    st.write('')

if(predict_btn):     # if statement for when a user clicks on the predict salary button
    inp1 = int(age)      # converts age value input to integer
    inp2 = float(experience)     # converts experience value input to a float
    inp3 = int(job_idx[job_list.index(job)])   # Searches for the index of the chosen job and then it uses this index to find the numeric code value for the job title so that is model friendly.
    inp4 = int(edu_list.index(education))      # finds the index of the education selected and converts it to an integer
    inp5 = int(gen_list.index(gender))         # finds the index of the gender selected and converts it to an integer
    X = [inp1, inp2, inp3, inp4, inp5]    # places all the inputs into a list
    salary = model.predict([X])        # predicts the salary based on the model using the list created above
    col13, col14, col15 = st.columns(3) # creates 3 columns
    with col13:
        st.write('')  # blank space  
    with col14:
        st.text(f"Estimated salary: ${int(salary[0])}")  #prints the estimated salary generated
    with col15:
        st.write('')  # blank space

