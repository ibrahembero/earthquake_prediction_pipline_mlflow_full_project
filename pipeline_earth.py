import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os
import datetime
import time
from datetime import datetime
import calendar
import mlflow
import mlflow.sklearn
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsRegressor

def convert_to_timestamp(real_time):
    try:
         # Adjust format string to match 'YYYY-MM-DDTHH:MM:SS.sssZ' format
        ts = datetime.strptime(real_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        # Use calendar.timegm to get the Unix timestamp
        timestamp = calendar.timegm(ts.utctimetuple())
        return float(timestamp)
    except ValueError:
        # Handle the case where the format is invalid
        return 'ValueError'


def run_pipeline():
    # 1. Read data
    file_path = r"C:\Users\dell\Downloads\bronze.csv"
    if os.path.exists(file_path):
        print(f"The file exists at: {file_path}")
        df = pd.read_csv(file_path)
        print("Data read successfully...")
    else:
        print(f"File not found at: {file_path}")

    # 2. Convert 'time' column to 'Timestamp'
    df['Timestamp'] = df['time'].apply(convert_to_timestamp)
    print("Timestamp conversion complete.")

    # 3. Extract relevant columns
    X = df[['longitude', 'latitude', 'depth', 'Timestamp']]  # Using the 'Timestamp' column here
    y = df['mag']
    print("Data ready for training...")

    # 4. Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 5. Fill missing values with the median (imputation)
    imputer = SimpleImputer(strategy='median')
    X_train_imputed = imputer.fit_transform(X_train)
    X_test_imputed = imputer.transform(X_test)

    print("Missing values filled with median.")

    # 6. Scale the data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_imputed)
    X_test_scaled = scaler.transform(X_test_imputed)

    print("Data scaling complete.")

    # 7. Train the model and use mlflow to track experiment
    knn = KNeighborsRegressor(n_neighbors=5)
    current_date = datetime.now().strftime("%Y-%m-%d")
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    experiment_name = f"Earthquake_Magnitude_Prediction_{current_date}"
    experiment_id = mlflow.set_experiment(experiment_name).experiment_id
    # Start a new MLflow run
    with mlflow.start_run():
        # Log the parameters used for the Voting Regressor
        mlflow.log_param("n_neighbors_knn", knn.n_neighbors)
        
        # Train the Voting Regressor
        print('start fitting')
        knn.fit(X_train_scaled, y_train)
        print('end fitting')
        
        # Log the model
        mlflow.sklearn.log_model(knn, "knn_regressor_model")

        
        print("Model and parameters logged successfully")
    

    # 8. Save the scaler and model
    # Get the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Define the directory where you want to save the files (for example, 'models/')
    directory = 'models'

    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)

    # Save the scaler and model with the current date and time in the filenames
    scaler_filename = os.path.join(directory, f"scaler_{current_time}.pkl")
    model_filename = os.path.join(directory, f"knn_model_{current_time}.pkl")

    joblib.dump(scaler, scaler_filename)
    joblib.dump(knn, model_filename)

    print("Model training complete and saved.")


# This line is a standard Python idiom. 
# It ensures that the run_pipeline() function is only called if the script is run directly 
# (not when it is imported as a module in another script).
if __name__ == "__main__":
    run_pipeline()