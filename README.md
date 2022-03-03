# Telecome-Deliquency-Prediction
Delinquency Telecom Model Definition: Delinquency is a condition that arises when an activity or situation does not occur at its scheduled (or expected) date i.e., it occurs later than expected.

Use Case: Many donors, experts, and microfinance institutions (MFI) have become convinced that using mobile financial services (MFS) is more convenient and efficient, and less costly, than the traditional high-touch model for delivering microfinance services. MFS becomes especially useful when targeting the unbanked poor living in remote areas. The implementation of MFS, though, has been uneven with both significant challenges and successes.

One of our Client in Telecom collaborates with an MFI to provide micro-credit on mobile balances to be paid back in 5 days. The Consumer is believed to be delinquent if he deviates from the path of paying back the loaned amount within 5 days.

## Approach

●	A Telecom company collaborates with microfinance institutions to provide micro-credit on mobile balances to be paid back in 5 days. We have to predict if the consumer will be delinquent or not by paying back in 5 days.

●	Data Cleaning: The data had to be numeric but had some errors (having alphabets, #, and null values). These were found out and cleaned based on data understanding using pandas.

●	EDA: Data analysis was done using bar plot and insights were drawn. Delinquency based on account balance, recharge frequency, number of loans and amount of loans taken by customer was compared.

●	Finding best ML model: Using heat-map, highly correlated features were drop which increased the model accuracy. The oversampling was done using SMOTE to avoid biasness. Using GridsearchCV best ML model and its parameters were found based on score.

●	Applying the best ML model: Prediction model was made using Decision Tree Classifier.

●	Deploying the model using streamlit: The pickle file was used to load the model. Sublime text as a source code editor, the model was deployed using streamlit.

●	Business recommendation: Using mutual_info_classifier from 35 features, top 5 features affecting the delinquency were found out and suggestion was given to focus on them.
