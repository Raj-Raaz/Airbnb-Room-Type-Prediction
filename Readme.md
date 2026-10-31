# Airbnb Room Type Prediction

A Flask web application that predicts the room type of a New York City Airbnb listing using listing, location, pricing, review, and availability information.

## Dataset

This project uses the New York City Airbnb Open Data dataset from Kaggle:

[New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)

## Prediction Target

The model predicts the Airbnb `room_type`, including categories such as:

- Entire home/apt
- Private room
- Shared room

## Features

The prediction form uses these features:

- Latitude and longitude
- Price per night
- Minimum nights
- Number of reviews
- Reviews per month
- Calculated host listings count
- Availability during the year
- Neighbourhood group
- Neighbourhood

## Technologies

- Python
- Flask
- Pandas
- Scikit-learn
- Pydantic
- Joblib
- Bootstrap
- Jupyter Notebook

## Project Structure

```text
.
├── airbnb_room_type.ipynb  # Data analysis and model development
├── app.py                   # Flask application
├── dataset.csv              # Airbnb dataset
├── Model_pipeline.pkl      # Trained machine learning pipeline
├── requirements.txt         # Python dependencies
├── schemas.py               # Input validation schema
├── Readme.md
└── templates/
	└── index.html           # Prediction form and results page
```

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

## Run the Application

Start the Flask development server:

```powershell
python app.py
```

Open the application in a browser at:

```text
http://127.0.0.1:5000
```

Enter the listing details and select **Predict Room Type** to view the predicted class and prediction probabilities.

## Model Pipeline

The trained pipeline is stored in `Model_pipeline.pkl` and loaded by `app.py`. It must be present in the project root when the application starts. The input columns supplied to the model are defined in `app.py`.

Input values are validated with Pydantic in `schemas.py`, including geographic ranges, non-negative prices and review counts, and valid night and availability limits.

## Notebook

The notebook `airbnb_room_type.ipynb` contains the data exploration, preprocessing, model training, and evaluation work used to build the prediction pipeline.

## Future Improvements

- Add dropdowns for neighbourhood groups and neighbourhoods.
- Add automated tests for validation and prediction routes.
- Display model evaluation metrics in the application.
- Add feature-importance visualizations.
- Deploy the application to a cloud platform.

## License and Attribution

This project is intended for educational and portfolio purposes. Dataset ownership and usage are subject to the terms provided by Kaggle and the original dataset authors.