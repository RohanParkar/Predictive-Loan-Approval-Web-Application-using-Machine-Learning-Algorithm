# Evaluating Machine Learning Algorithms to Build Web-Based Predictive Loan Approval System Based on Credit Score
## Abstract
In the financial sector, the accuracy and efficiency of loan approval processes are critical for minimizing default risk and ensuring that only eligible applicants receive loans. This research project focuses on applying machine learning algorithms to predict loan approval based on credit scores and other relevant factors. The study employed a comprehensive methodology, including data collection, preprocessing, exploratory data analysis, model development, and evaluation. A detailed analysis and comparison of five widely used classification algorithms: Logistic Regression, Extreme Gradient Boosting (XGBoost), K-Nearest Neighbors (KNN), Multilayer Perceptron (MLP) Classifier, and Support Vector Machine (SVM) was conducted. The results demonstrate that Extreme Gradient Boosting outperforms other models' accuracy, precision, recall, F1-score, and the Area Under the Receiver Operating Characteristic Curve (ROC-AUC) score. A web-based application was developed to integrate the best-performing model for real-time loan approval predictions using HTML, CSS, JavaScript, and Flask. In the financial sector, the accuracy and efficiency of loan approval processes are critical for minimizing default risk and ensuring that eligible applicants receive loans. This project highlights the potential of machine learning algorithms in transforming traditional credit scoring methods, addressing limitations of subjective assessments, and improving the overall reliability and accuracy of loan approval systems.
Keywords: machine learning, loan approval, credit score, predictive modeling, web-based application.

## Usability
* Unzip the zipped folder on your machine.
* Import the project in Visual Studio Code.  
* Install the dependencies from requirements.txt
* Run the loanApprovalPrediction-XGB_Model.py to train the model.
* After the training is complete run the app.py to start web application.


>app.py: Main Flask application file.

>loanApprovalPrediction-XGB_Model.py: Contains the XGBoost model code.

>/data: Folder containing data files (loan application data).

>/templates: HTML templates for the web interface.

>/static: CSS and other static files.

>model.pkl: Pre-trained xg boost model.


## Libraries Required:
* Flask==3.0.3
* numpy==1.24.3
* pandas==2.0.1
* scikit-learn==1.2.2
* xgboost==2.1.1

