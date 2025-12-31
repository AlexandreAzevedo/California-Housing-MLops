import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import joblib
import os

# 1. Setup Paths
# This ensures the script finds files no matter where you run it from
current_dir = os.path.dirname(os.path.abspath(__file__)) # The 'model' folder
root_dir = os.path.dirname(current_dir)                  # The project root
data_dir = os.path.join(root_dir, 'data')

print(f"Looking for data in: {data_dir}")

# 2. Load Data
# We expect X_train.parquet and y_train.parquet to be in the 'data' folder
try:
    X_train = pd.read_parquet(os.path.join(data_dir, 'X_train.parquet'))
    y_train = pd.read_parquet(os.path.join(data_dir, 'y_train.parquet'))
    print("✅ Data loaded successfully.")
except FileNotFoundError as e:
    print(f"❌ Error: Could not find data files. {e}")
    exit()

# 3. Build the Pipeline
# We need to convert 'ocean_proximity' to numbers.
categorical_features = ['ocean_proximity']

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ],
    remainder='passthrough'  # Keep all other numerical columns as they are
)

model_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=50, random_state=42))
])

# 4. Train
print("Training model... (this might take a moment)")
model_pipeline.fit(X_train, y_train.values.ravel())

# 5. Save
output_path = os.path.join(current_dir, 'housing_model.pkl')
joblib.dump(model_pipeline, output_path)
print(f"✅ Success! Model saved to: {output_path}")