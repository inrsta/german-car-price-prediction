import streamlit as st
import pandas as pd
import pickle

# Load your model
with open(
    r"model/best_xgboost_model.pkl",
    "rb",
) as file:
    model = pickle.load(file)

# Load the unique values for the categorical columns
with open(
    r"model/unique_categorical_values.pkl",
    "rb",
) as handle:
    unique_categorical_values = pickle.load(handle)

with open(
    r"model/dict_vectorizer.pkl",
    "rb",
) as dv_file:
    dv = pickle.load(dv_file)


# Define the app
def main():
    st.title("Car Price Prediction App")

    # Create inputs for the user to fill in the details
    brand = st.selectbox("Brand", unique_categorical_values["brand"])
    model_car = st.selectbox("Model", unique_categorical_values["model"])
    color = st.selectbox("Color", unique_categorical_values["color"])
    registration_date = st.selectbox(
        "Registration Date", unique_categorical_values["registration_date"]
    )
    transmission_type = st.selectbox(
        "Transmission Type", unique_categorical_values["transmission_type"]
    )
    fuel_type = st.selectbox("Fuel Type", unique_categorical_values["fuel_type"])
    power_ps = st.number_input("Power (kW)", min_value=0.0, max_value=1000.0)
    mileage_in_km = st.number_input("Mileage (in km)", min_value=0)
    # Add more input parameters as necessary

    # Button to predict price
    if st.button("Predict Price"):
        # Create a DataFrame with the input data
        input_data = pd.DataFrame(
            {
                "brand": [brand],
                "model": [model_car],
                "color": [color],
                "registration_date": [registration_date],
                "transmission_type": [transmission_type],
                "fuel_type": [fuel_type],
                "power_ps": [power_ps],
                "mileage_in_km": [mileage_in_km],
            }
        )

        # Preprocess the input data in the same way as your training data
        # Here, handle categorical encoding, missing values, etc.
        input_dict = input_data.to_dict(orient="records")

        # Vectorize the input data using the DictVectorizer
        input_vectorized = dv.transform(input_dict)

        # Make prediction
        prediction = model.predict(input_vectorized)

        # Display the prediction
        st.success(f"The estimated price for your car is €{prediction[0]:,.2f}")


if __name__ == "__main__":
    main()
