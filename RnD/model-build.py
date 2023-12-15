import pandas as pd 
import os
from sklearn.linear_model import LogisticRegression
import pickle

current_dir = os.getcwd()
current_dir = os.path.basename(current_dir)

csv_file_path = "diabetes.csv"
if current_dir != "RnD":
    csv_file_path = "RnD/" + csv_file_path

model_export_path = "web-server/diabetes-model.pkl"
if current_dir == "RnD":
    model_export_path = "../" + model_export_path

daibetes = pd.read_csv(csv_file_path)

train_X = daibetes[['Pregnancies','Glucose','BloodPressure','SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']] # taking the training data features
train_y=daibetes.Outcome

model = LogisticRegression(random_state=0, max_iter=1000)
model.fit(train_X,train_y)

pickle.dump(model, open(model_export_path, 'wb'))