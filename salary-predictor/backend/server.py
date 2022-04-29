# Import libraries
from crypt import methods
from operator import mod
import numpy as np
from flask import Flask, request, jsonify
import pickle
from flask_cors import cross_origin
from sklearn.model_selection import train_test_split
import pandas as pd

# Importing the dataset
dataset = pd.read_csv("salary_data.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1]

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

app = Flask(__name__)

# Load the model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/salary", methods=['POST'])
@cross_origin()
def predict():
    # Get the data from the POST request
    data = request.get_json(force=True)
    print("request data : ", data)
    prediction = model.predict([[np.array(data['yearsExperience'])]])
    output = prediction[0]
    return jsonify({"salary": output})

@app.route("/data", methods=['GET'])
@cross_origin()
def data():
    testFeature = [[X_train.min()], [X_train.max()]]
    testTarget = model.predict(testFeature)
    return jsonify({"point": np.concatenate([X_train, y_train.values.reshape((-1, 1))], axis=1).tolist(), 
                    "line": np.concatenate([testFeature, testTarget.reshape((-1, 1))], axis=1).tolist(),
                    "coef": model.coef_.tolist(),
                    "intercept": [model.intercept_.tolist()],
            })

if __name__ == "__main__":
    app.run(port=5000, debug=True)