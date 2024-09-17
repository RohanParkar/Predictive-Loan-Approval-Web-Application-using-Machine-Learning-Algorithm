
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import pickle

df = pd.read_csv("data\prosperLoanDataCleaned.csv")

df = df.drop(['LoanNumber'], axis=1)
categorical = ['Term','IsHomeowner','IsEmployed','AnyDelinquencies','IncomeVerifiable']
numerical = ['LoanAmount','InterestRate','MonthlyInstallment','MonthsOfEmployementExperience','AverageCreditScore'
             ,'OpenCreditLines','TotalInquiries','AvailableBankcardCredit','DebtToIncomeRatio','StatedMonthlyIncome']

Q1 = df[numerical].quantile(0.25)
Q3 = df[numerical].quantile(0.75)
IQR = Q3 - Q1

# Calculate median
median = df[numerical].median()

# Identify outliers
outliers_lower = (df[numerical] < (Q1 - 1.5 * IQR))
outliers_upper = (df[numerical] > (Q3 + 1.5 * IQR))

# Replace outliers with median
df[numerical] = df[numerical].mask(outliers_lower, median, axis=1)
df[numerical] = df[numerical].mask(outliers_upper, median, axis=1)

X = df.drop(columns=['GoodLoan']) 
y = df['GoodLoan']  

Standard_Scaler = StandardScaler()
X[numerical] = Standard_Scaler.fit_transform(X[numerical])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=42)

best_subset_XGB = ['InterestRate', 'MonthlyInstallment', 'AverageCreditScore', 'Term', 'AnyDelinquencies', 
                   'IsHomeowner', 'DebtToIncomeRatio', 'StatedMonthlyIncome', 'OpenCreditLines']
best_params_XGB =  {'learning_rate': 0.1, 'max_depth': 4, 'n_estimators': 100}

weight=len(y_train[y_train == 0]) / len(y_train[y_train == 1])

XGB = XGBClassifier(**best_params_XGB,random_state=42,scale_pos_weight=weight)

XGB.fit(X_train[best_subset_XGB], y_train)

from sklearn.metrics import classification_report, accuracy_score
y_pred = XGB.predict(X_train[best_subset_XGB])
train_acc_XGB = accuracy_score(y_train, y_pred)
print("Training accuracy:", train_acc_XGB)

# Calculate testing accuracy
y_pred = XGB.predict(X_test[best_subset_XGB])
test_acc_XGB = accuracy_score(y_test, y_pred)
print("Testing accuracy:", test_acc_XGB)

# Save the model using pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(XGB, f)

print("Model trained and saved successfully!")