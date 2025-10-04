import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler
import numpy as np

# Load and preprocess data
@st.cache_data
def load_and_preprocess_data():
    try:
        # Load your dataset
        data = pd.read_csv("real_estate_india.csv")  
        
        # Check if necessary columns exist
        required_columns = {"Area", "Bedrooms", "Bathrooms", "Location", "Price"}
        if not required_columns.issubset(data.columns):
            st.error("Dataset is missing one or more required columns: 'Area', 'Bedrooms', 'Bathrooms', 'Location', 'Price'")
            return None, None, None, None, None, None, None
        
        # Here we assume all prices in the dataset are in ten lakhs
        # Filter out outliers using the 99th quantile
        price_threshold = data['Price'].quantile(0.99)
        data = data[data['Price'] <= price_threshold]
        
        # Encode the 'Location' column
        le = LabelEncoder()
        data['Location'] = le.fit_transform(data['Location'])
        
        # Separate features and target
        X = data[['Area', 'Bedrooms', 'Bathrooms', 'Location']]
        y = data['Price']
        
        # Split into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Scale features
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        
        return X_train, X_test, y_train, y_test, scaler, le, price_threshold
    except FileNotFoundError:
        st.error("Dataset file not found. Please check the file path.")
        return None, None, None, None, None, None, None
    except Exception as e:
        st.error(f"An error occurred during data loading and preprocessing: {e}")
        return None, None, None, None, None, None, None

# Train model
@st.cache_resource
def train_model(X_train, y_train):
    try:
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        st.error(f"An error occurred during model training: {e}")
        return None

# Load data and train model
X_train, X_test, y_train, y_test, scaler, le, price_threshold = load_and_preprocess_data()
if X_train is not None and y_train is not None:
    model = train_model(X_train, y_train)
else:
    model = None

# Streamlit app UI
st.title("Real Estate Price Prediction")

# Ensure the model is loaded
if model is not None:
    # User input
    Area = st.number_input('Area', min_value=500, max_value=5000, step=50)
    Bedrooms = st.number_input('Number of Bedrooms', min_value=1, max_value=10, step=1)
    Bathrooms = st.number_input('Number of Bathrooms', min_value=1, max_value=5, step=1)

    
    # Location selection with label encoding
if le:
        # Predefined list of locations
        Location = ['Bangalore', 'Delhi', 'Hyderabad', 'Mumbai', 'Patna', 'Pune', 'Kolkata', 'Shimla', 'Jaipur', 'Bhopal']
        Location = st.selectbox("Select Location:", Location)
        location_encoded = le.transform([Location])[0]  # Encode the selected location
        
        # Prepare input data for prediction
        input_data = scaler.transform([[Area, Bedrooms, Bathrooms, location_encoded]])

        

        # Predict button
        if st.button("Predict Price"):
            predicted_Price = model.predict(input_data)[0]  # Prediction in ten lakhs

            price_in_crores = predicted_Price / 10_000_000
            price_in_ten_lakhs = predicted_Price

            
            # Display price in ten lakhs or crores based on the amount
            
            st.success(f"Estimated Price: ₹{price_in_ten_lakhs:.2f} Lakhs (₹{price_in_crores:.2f}Crores)")

    # Optional: Display raw dataset with quantile filtering
if st.checkbox("Show Filtered Dataset"):
        data = pd.read_csv("real_estate_india.csv")  # Update with the path to your dataset
        # Apply quantile filtering again for display
        data = data[data['Price'] <= price_threshold]
        st.write(data)