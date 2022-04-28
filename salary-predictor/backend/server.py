# Import libraries
from operator import mod
import numpy as np
from flask import Flask, request, jsonify
import pickle
from flask_cors import cross_origin

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

if __name__ == "__main__":
    app.run(port=5000, debug=True)