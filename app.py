from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import random
import requests

app = Flask(__name__)

# Load model and preprocessor
with open("preprocesser.pkl", "rb") as f:
    preprocesser = pickle.load(f)

with open("stacking_model.pkl", "rb") as f:
    stacking_model = pickle.load(f)

# Load dataset to extract unique values for dropdowns
df = pd.read_csv("yield.csv")
regions = sorted(df["Area"].unique())
crops = sorted(df["Item"].unique())

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            year = int(request.form["year"])
            rainfall = float(request.form["rainfall"])
            pesticides = float(request.form["pesticides"])
            temp = float(request.form["temp"])
            region = request.form["region"]
            crop = request.form["crop"]

            # Preprocess input and predict
            features = pd.DataFrame([[year, rainfall, pesticides, temp, region, crop]],
                                    columns=["Year", "average_rain_fall_mm_per_year", "pesticides_tonnes", "avg_temp", "Area", "Item"])
            transformed_features = preprocesser.transform(features)
            prediction = stacking_model.predict(transformed_features)[0]

        except Exception as e:
            print("Error:", e)
    
    return render_template("index.html", regions=regions, crops=crops, prediction=prediction)

# API Endpoint for "Did You Know?" facts
@app.route("/get_fact")
def get_fact():
    try:
        response = requests.get("https://api.api-ninjas.com/v1/facts", headers={"X-Api-Key": "dHMBz7RJE0R1bHarMtAJvg==JnoFnlX968UjVZTF"})
        fact_data = response.json()
        fact = fact_data[0]["fact"]
    except:
        fact = "Unable to load fact at this time."
    return jsonify({"fact": fact})

if __name__ == "__main__":
    app.run(debug=True)
