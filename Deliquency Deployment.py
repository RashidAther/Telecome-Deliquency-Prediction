import numpy as np
import pickle
import streamlit as st
import sklearn
import time

# loading the saved model
loaded_model = pickle.load (open('C:/Users/Rashid/Desktop/Jupyter Practice/Skill Vertex/Major Project - Updated/trained_model.sav',
     'rb'))

# creating a function for Prediction

def delinquency_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The label is 0: The customer will not payback in 5 days'
    else:
      return 'The label is 1: The customer will payback in 5 days '

rad =st.sidebar.radio("Navigation",["Prediction","About Model"])


if rad == "Prediction":

    def main():

        # giving a title
        st.title('Telecom Delinquency Prediction Web App')
        
        
        # getting the input data from the user
        
        aon = st.text_input('Age on cellular network in days')
        daily_decr30 = st.text_input('Daily amount spent from main account, averaged over last 30 days')
        col1 , col2 = st.columns(2)
        rental30 = col1.text_input('Average main account balance over last 30 days')
        last_rech_date_ma = col2.text_input('Number of days till last recharge of main account')
        col3 , col4 = st.columns(2)
        last_rech_date_da = col3.text_input('Number of days till last recharge of data account')
        last_rech_amt_ma = col4.text_input('Amount of last recharge of main account')
        cnt_ma_rech30 = st.text_input('Number of times main account got recharged in last 30 days')
        fr_ma_rech30 = st.text_input('Frequency of main account recharged in last 30 days')
        medianmarechprebal30= st.text_input('Median of main account balance just before recharge in last 30 days at user level')
        fr_ma_rech90 = st.text_input('Frequency of main account recharged in last 90 days')
        medianmarechprebal90=st.text_input('Median of main account balance just before recharge in last 90 days at user level')
        cnt_da_rech30=st.text_input('Number of times data account got recharged in last 30 days')
        fr_da_rech30=st.text_input('Frequency of data account recharged in last 30 days')
        cnt_da_rech90=st.text_input('Number of times data account recharged in last 90 days')
        fr_da_rech90=st.text_input('Frequency of data account recharged in last 90 days')
        maxamnt_loans30=st.text_input('maximum amount of loan taken by the user in last 30 days')
        medianamnt_loans30=st.text_input('Median of amounts of loan taken by the user in last 30 days')
        cnt_loans90=st.text_input('Number of loans taken by user in last 90 days')
        maxamnt_loans90=st.text_input('maximum amount of loan taken by the user in last 90 days')
        payback30=st.text_input('Average payback time in days over last 30 days')
        
        # code for Prediction
        delinquency = ''
        
        # creating a button for Prediction
        
        if st.button('Telecom Delinquency Prediction Result'):
            delinquency = delinquency_prediction([aon, daily_decr30, rental30, last_rech_date_ma, last_rech_date_da, last_rech_amt_ma,
                cnt_ma_rech30, fr_ma_rech30, medianmarechprebal30, fr_ma_rech90, medianmarechprebal90, cnt_da_rech30, fr_da_rech30,
                cnt_da_rech90, fr_da_rech90, maxamnt_loans30, medianamnt_loans30, cnt_loans90, maxamnt_loans90, payback30])
            
            
        st.success(delinquency)
        
        st.success("Model Predicted Successfully")


    if __name__ == '__main__':
        main()

if rad == "About Model": 
    st.title("Info About: Delinquency Data")
    st.info("Information Loading...")
    progress = st.progress(0)
    for i in range(50):
        time.sleep(0.1)
        progress.progress(i+1)
    st.success("Info loaded Successfuly")
    
    st.header("Context")
    st.markdown("""Delinquency is a condition that arises when an activity or situation does not occur at its scheduled (or expected) date
         i.e., it occurs later than expected.""")

    st.header("Data Description")
    st.markdown("""A Telecom collaborates with an MFI to provide micro-credit on mobile balances to be paid back in 5 days.
        The Consumer is believed to be delinquent if he deviates from the path of paying back the loaned amount within 5 days.
        The sample data from our client database is hereby given to you for the exercise.""")

    st.header("Model Output")
    st.markdown("""We will predict whether the customer will be paying back the loaned amount 
        within 5 days of insurance of loan. """)
    m1 , m2, m3 = st.columns([1,2,1])
    m1.markdown(""" Label 1:  YES """)
    m2.markdown(""" OR """)
    m3.markdown(""" Lable 0:  NO """)
