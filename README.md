# 🏡 California Housing Price Predictor (MLOps)

A production-ready Machine Learning API that predicts housing prices based on California census data. 
This project demonstrates a complete **MLOps pipeline**, moving from data exploration to a containerized model ready for deployment.

## 🚀 Key Features
* **Model:** Scikit-Learn Pipeline with Random Forest Regressor (RMSE: ~$49k).
* **API:** FastAPI for real-time inference.
* **Containerization:** Dockerized for consistent deployment across environments.
* **Reproducibility:** Strict versioning via `requirements.txt`.

## 🛠️ Tech Stack
* **Python 3.12**
* **Docker**
* **FastAPI**
* **Scikit-Learn / Pandas**

---

## 💻 How to Run Locally (via Docker)
You can run the API without installing Python or dependencies.

1. **Build the Image**
   ```bash
   docker build -t housing-api .

2. **Run the Container**
   ```bash
   docker run -p 80:80 housing-api

3. **Test the API**
   Open your browser to http://localhost/docs to access the interactive Swagger UI.

## 📂 Project Structure

```text
├── app/
│   └── main.py          # FastAPI application entry point
├── model/
│   ├── train_model.py   # Script to train and save the model
│   └── housing_model.pkl # Serialized trained model
├── Dockerfile           # Blueprint for the container
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## 🧠 Model Details

The model was trained on the California Housing dataset using a Random Forest Regressor.
- Preprocessing: Imputation for missing values, log transformation for skewed features.
- Validation: 80/20 Train-Test split.
