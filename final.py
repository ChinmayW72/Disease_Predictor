import pandas as pd

train_data = pd.read_csv('Medical2.csv') 
eval_data = pd.read_csv('modified_data.csv')


from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


X_train = train_data.drop('Disease', axis=1)
y_train = train_data['Disease']
X_eval = eval_data.drop('Disease', axis=1)
y_eval = eval_data['Disease']


model = RandomForestClassifier(n_estimators=100, random_state=42)


model.fit(X_train, y_train)


y_pred = model.predict(X_eval)


accuracy = accuracy_score(y_eval, y_pred)
print("Accuracy:", accuracy)
print(classification_report(y_eval, y_pred))


import joblib

model_filename = 'disease_prediction_model.pkl'
joblib.dump(model, model_filename)
