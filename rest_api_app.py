from joblib import dump, load
import pandas as pd
from flask import Flask,render_template,request,jsonify


app = Flask(__name__)

classifier = load('random_forest_classifier.joblib')


@app.route("/predict",methods=["POST"])
def predict():
    json_=request.json
    df=pd.DataFrame(json_)
    prediction=classifier.predict(df)
    return jsonify({"Prediction":list(prediction)})


@app.route("/test",methods=["GET"])
def test():
    return jsonify({"Prediction":400})


if __name__ == '__main__':
    app.run(host='0.0.0.0')






