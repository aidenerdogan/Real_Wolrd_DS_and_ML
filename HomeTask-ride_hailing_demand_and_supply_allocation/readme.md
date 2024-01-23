To see notebook, download it or download html format

## 1. Exploratory Data Analysis (EDA)

### 1.1 Data Cleaning and Preprocessing
   - Check for missing values, outliers, and inconsistencies.
   - Convert `start_time` to a datetime format for time-related analysis.
   - Explore the distribution of `ride_value` to understand the monetary aspect of rides.

### 1.2 Feature Engineering - # Featue Extraction 1
    - Extract Time Features like
        - minute on hour
        - interval
        - hour of day
        - day of week

### 1.3 Temporal Analysis
   - Time Series Analysis: Visualize ride demand patterns over time using heatmaps.
   - Identify peak demand hours and days.
   - Extract Trend and Seasonality Patterns
   - Make Sarima Model
   - Spatial Analyasis: Analyze the distribution of ride values across different locations to extract some landmarks to use in model.

### 1.4 Feature Engineering - Feture Extraction 2
   - Create additional features such as 
   - Calculate distances and ride duration of rides to understand the trip characteristics.
   - Genrate label cluster with descidin Elbow

## 2. Baseline Model

### 2.1 Model Selection
   - Consider using a regression model XGB Regressor and Random Forest Regressor to predict ride values based on spatial and temporal features.
   - Split the data into training and testing sets.
   - Select Model with RandomizedGridSearch and R2 metric for best params and model
   - Extract Feature Importance

### 2.2 Training and Validation
   - Train the baseline model on the training set.
   - Evaluate model performance on the testing set using appropriate metrics like
    - Mean Absolute Error(MAE)
    - Mean Squared Errod(MSE)
    - Root MAE
    - R2

### 3 Model Deployment Sample
   - Generate deployment model with scoring system to decide for recomendations based on given time and location
   - Show Recommendations on map

## 4. Design and Deployment Methods (Theoretical Explained)

## 5. Communicating Model Recommendations to Drivers (Theoretical Explained)

## 6. Experiment Design (Theoretical Explained)

## Additional Data Considerations

## References