
# 🔊 SONAR Rock vs Mine Classifier

This project uses a Machine Learning model trained on sonar signal data to classify underwater objects as either **rock** or **mine**. A real-time web app is built using **Streamlit**, allowing users to input 59 SONAR signal features and instantly get a prediction.

---

## 📌 Project Overview

- **Problem**: Submarines need to detect underwater threats like mines. This project aims to classify objects based on SONAR readings.
- **Goal**: Predict whether an object is a **Mine (M)** or a **Rock (R)** using 59 numerical features.

---

## 🚀 Features

- 🔢 Input **comma-separated SONAR readings** (59 values)
- 🤖 Predict using a **pre-trained ML model**
- ✅ Display result with clear interpretation
- 📱 Built using **Streamlit** for real-time use

---

## 📁 Folder Structure

```
sonar-rock-mine-predictor/
│
├── app.py                  # Streamlit app code UI
├── sonar_model.ipynb       # Training the model 
├── sonar_model.pkl         # Trained ML model
├── requirements.txt        # Required packages
├── README.md               # Documentation
```

---

## 🧪 Sample Input

-Each prediction is made using a snapshot of 59 consecutive sonar intensity values collected over a 3-second window.

```text
0.02,0.0379,0.0422,0.0205,0.0954,0.0986,0.1539,0.1601,0.3109,0.2111,
0.1609,0.1582,0.2238,0.0645,0.066,0.2273,0.3109,0.2991,0.5078,0.4797,
0.5783,0.5071,0.4328,0.555,0.6711,0.6415,0.7104,0.808,0.6791,0.3857,
0.1307,0.2604,0.5123,0.7547,0.8537,0.8507,0.6692,0.6097,0.4943,0.2744,
0.051,0.2834,0.2825,0.4256,0.2641,0.1386,0.1051,0.1343,0.0383,0.0324,
0.0232,0.0027,0.0065,0.0159,0.0072,0.0167,0.018
```

---

## 💻 Setup Instructions

### 🧬 Clone the Repository

```bash
git clone https://github.com/your-username/sonar-rock-mine-predictor.git
cd sonar-rock-mine-predictor
```

### ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📦 Model Training (Optional)

If you want to retrain the model:

```python
# Load dataset
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_csv("sonar.all-data.csv", header=None)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("sonar_model.pkl", "wb"))
```

---

## 📊 Model Info

- **Input Features**: 59 numeric values representing SONAR energy in various frequency bands
- **Target**:
  - `R` → Rock
  - `M` → Mine

---

## 🧠 ML Techniques Used

- Logistic Regression (or any classifier you used)
- Feature scaling (if applicable)
- Model saved using `pickle`

---

## 📌 Applications

- Underwater object detection for submarines and marine robotics
- Real-time defense systems
- Sonar data signal processing

---

## 👩‍💻 Author

**Monasri M**  
B.Tech - Artificial Intelligence and Data Science  
🔗 [LinkedIn](https://www.linkedin.com/) |
