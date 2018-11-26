# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda loan_amount_term: loan_amount_term/12)

big_loan_term = loan_term[loan_term >= 25].shape[0]


# code ends here


# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
bank = pd.read_csv(path);
categorical_var = bank.select_dtypes(include='object')
print(categorical_var)

numerical_var = bank.select_dtypes(include='number')
print(numerical_var)

# code starts here






# code ends here


# --------------
# Code starts here
banks
avg_loan_amount = pd.pivot_table(banks, index=['Gender', 'Married', 'Self_Employed'],values= 'LoanAmount')
print(avg_loan_amount)

# code ends here



# --------------
# code starts here

loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')].shape[0]

loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')].shape[0]

percentage_se = (loan_approved_se/banks.shape[0]) *100
percentage_nse = (loan_approved_nse/banks.shape[0]) *100
# code ends here


# --------------
# code ends here
loan_groupby = banks.groupby('Loan_Status')['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()


# code ends here


# --------------
# code starts here

banks = bank.drop('Loan_ID', axis=1)
print(banks.isnull().sum())
# print({ i,  for i in is_nans_series[is_nans_series>0].to_dict()})
bank_mode = banks.mode()

print(bank_mode)
banks = banks.fillna({
    'Gender': 'Male',
    'Married': 'Yes',
    'Dependents': '0',
    'Self_Employed': 'No',
    'LoanAmount': 120.0,
    'Loan_Amount_Term': 360.0,
    'Credit_History': 1.0
})
print(banks.isnull().sum())
#code ends here


