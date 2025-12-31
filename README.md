# 🏡 California Housing Price Predictor (MLOps)

A production-ready Machine Learning API that predicts housing prices based on California census data. 
This project demonstrates a complete **MLOps pipeline**, moving from data exploration to a containerized model ready for deployment.

## 🚀 Key Features
* **Model:** Scikit-Learn Pipeline with Random Forest Regressor (RMSE: ~$49k).
* **API:** FastAPI for real-time inference.
* **Containerization:** Dockerized for consistent deployment across environments.
* **Reproducibility:** Strict versioning via `requirements.txt`.

## 🛠️ Tech Stack
* **Python 3.11**
* **Docker**
* **FastAPI**
* **Scikit-Learn / Pandas**

---

## 💻 How to Run Locally

### Option A: Using Docker (Recommended)
You can run the API without installing Python or dependencies.

1. **Build the Image**
   ```bash
   docker build -t housing-api .