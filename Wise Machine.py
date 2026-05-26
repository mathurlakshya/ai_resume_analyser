import pandas as pd
import joblib

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Load dataset
df = pd.read_excel('beginner_house_price_dataset.xlsx')

# Remove outliers
df = df[df['PRICE'] < df['PRICE'].quantile(0.99)]

# Features and target
X = df.drop(columns=['PRICE'])
Y = df['PRICE']

# Columns
num_cols = [
    'AREA_SQFT',
    'BEDROOMS',
    'BATHROOMS',
    'FLOORS',
    'AGE_OF_PROPERTY',
    'PARKING_SPACES'
]

cat_cols = ['LOCALITY', 'HOUSE_TYPE']

# Preprocessing
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), num_cols),
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)
])

# Pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

# Train
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

pipeline.fit(X_train, y_train)

# Save model
joblib.dump(pipeline, 'house_price_model.pkl')

print("Model trained and saved successfully!")