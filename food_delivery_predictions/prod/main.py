from pathlib import Path
import pandas as pd
import pickle
import xgboost as xgb
from utils import cleaning_steps, label_encoding,extract_label_value, perform_feature_engineering, data_split, standardize, evaluate_model



if __name__ == "__main__":
    df_train = pd.read_csv(str(Path(__file__).parents[1] / 'datasets/train.csv'))  # Load Data
    cleaning_steps(df_train)  # Perform Cleaning
    extract_label_value(df_train) #Extract Label Value
    perform_feature_engineering(df_train)  # Perform feature engineering

    # Split features & label
    X = df_train.drop('Time_taken(min)', axis=1)  # Features
    y = df_train['Time_taken(min)']  # Target variable

    label_encoders = label_encoding(X)  # Label Encoding
    X_train, X_test, y_train, y_test = data_split(X, y)  # Test Train Split
    X_train, X_test, scaler = standardize(X_train, X_test)  # Standardization

    # Build Model
    model = xgb.XGBRegressor(n_estimators=20, max_depth=9)
    model.fit(X_train, y_train)

    # Evaluate Model
    y_pred = model.predict(X_test)
    evaluate_model(y_test, y_pred)

    # Save Model
    with open(str(Path(__file__).parents[1] / 'model/xgb_model.pickle'), 'wb') as f:
        pickle.dump((model, label_encoders, scaler), f)