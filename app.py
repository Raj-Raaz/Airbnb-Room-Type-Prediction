from flask import Flask, jsonify, render_template, request
import pandas as pd
import joblib
from pydantic import ValidationError

from schemas import Features


app = Flask(__name__)

# Load trained pipeline
model = joblib.load("Model_pipeline.pkl")


COLUMNS = ['latitude', 'longitude', 'price', 'minimum_nights', 'number_of_reviews',
       'reviews_per_month', 'calculated_host_listings_count','availability_365','neighbourhood_group','neighbourhood']

@app.get('/')
def greet():
    return render_template('index.html')



@app.post('/predict')
def predict():
    data = request.form.to_dict()

    features = Features(**data)

    features_data = features.model_dump()
    row = pd.DataFrame([features_data], columns=COLUMNS)

    prediction = model.predict(row)[0]
    probability = model.predict_proba(row)[0]

    return render_template(
        "index.html",
        prediction=prediction,
        probabilities={room_type: round(float(prob) * 100, 2) for room_type, prob in zip(model.classes_, probability)}
    )


if __name__ == "__main__":
    app.run(debug=True)