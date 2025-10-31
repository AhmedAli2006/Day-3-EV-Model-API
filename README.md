# ⚡ EV Demand Prediction API (Day 3)

This project deploys a trained **CatBoost regression model** that predicts **electric vehicle (EV) charging energy consumption (in kWh)** based on charger site, session duration, and time-based factors.  
The model is served using **FastAPI**, a high-performance web framework for building machine learning APIs.

---

## 🚀 Project Overview

This API enables quick, automated predictions of energy consumed during EV charging sessions.  
It can be integrated into dashboards, IoT systems, or edge devices to optimize grid management and charger utilization.

### 🎯 Objective
Predict the **energy consumption (`Consum(kWh)`)** of an EV charging session using:
- Site and charger information
- Connector type
- Session duration
- Date and time features (hour, weekday, month)
- Location postcode

---

## 🧠 Model Summary

| Metric | Value |
|---------|--------|
| **MAE** | 5.61 kWh |
| **RMSE** | 7.95 kWh |
| **R²** | 0.756 |

**Best Model:** CatBoost  
**Dataset:** Dundee City Council Public EV Charge Point Usage (2024)

---

## ⚙️ Tech Stack

| Component | Description |
|------------|--------------|
| 🧩 **FastAPI** | Framework for serving ML models as REST APIs |
| 🐍 **Python 3.12+** | Programming language |
| 🧠 **CatBoost** | Gradient boosting model used for prediction |
| 💾 **Joblib** | Model persistence & serialization |
| 🧰 **Pydantic** | Data validation for API inputs |
| ⚡ **Uvicorn** | ASGI web server to host the API |

---

## 🧱 Folder Structure

```
Day3-EV-Model-API/
│
├── app/
│   ├── main.py              # FastAPI application
│   ├── schemas.py           # Input data validation models
│   └── utils.py             # (Optional) helper functions
│
├── model/
│   └── ev_demand_catboost.joblib    # Trained CatBoost model
│
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── .gitignore               # Ignore virtual env & large files
└── .venv/                   # Virtual environment (excluded from git)
```

---

## 🧩 API Endpoints

### **1️⃣ Health Check**
```http
GET /
```
**Response:**
```json
{ "message": "EV Demand Prediction API is running!" }
```

---

### **2️⃣ Prediction Endpoint**
```http
POST /predict
```

**Request Body:**
```json
{
  "Site": 12,
  "CP_ID": 5,
  "Connector_Type": 2,
  "Duration_hours": 0.75,
  "hour": 14,
  "day_of_week": 2,
  "month": 10,
  "Postcode": 33
}
```

**Response:**
```json
{
  "Predicted_Consumption_kWh": 26.37
}
```

---

## ⚙️ Running the API Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/AhmedAli2006/Day3-EV-Model-API.git
cd Day3-EV-Model-API
```

### 2️⃣ Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate     # (on Linux/macOS)
# or
.venv\Scripts\activate        # (on Windows)
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the FastAPI server
```bash
uvicorn app.main:app --reload
```

### 5️⃣ Open in your browser
- Swagger UI → http://127.0.0.1:8000/docs  
- Root endpoint → http://127.0.0.1:8000/

---

## 📦 Example Workflow

1. Send a POST request to `/predict`  
2. The model processes your input  
3. You receive an instant prediction of energy usage (in kWh)

---

## 🧰 Example Output

```json
{
  "Predicted_Consumption_kWh": 26.37
}
```

---

## 📚 Future Improvements

- Add weather & temperature features for improved accuracy  
- Deploy on Render or Hugging Face Spaces for live public access  
- Add Streamlit dashboard for real-time visualization  

---

## 👨‍💻 Author

**Ahmed Ali**  
Embedded Systems & AI Engineer  
GitHub: [AhmedAli2006](https://github.com/AhmedAli2006)

---

### 🏁 Status: ✅ Completed (Deployed Locally)
