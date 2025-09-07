# 🩺 Breast Cancer Prediction Model

A Machine Learning + Flask web application that predicts whether a tumor is **Cancerous** or **Not Cancerous** based on user-provided medical feature values.

---

## 🚀 Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **ML Model**: scikit-learn (trained and saved as `model.pkl`)
- **Other Tools**: NumPy, Pandas, Jupyter Notebook

---

## 📂 Project Structure
├── app.py # Flask backend

├── app.ipynb # Jupyter notebook (model training & testing)

├── data.csv # Dataset used for training

├── model.pkl # Trained ML model

├── templates/

│ └── index.html # Frontend HTML (Flask template)

├── static/

│ ├── image1.jpeg # Header image

│ ├── img1.jpeg # Cancerous image

│ └── img2.jpeg # Non-cancerous image


---

## ⚙️ How to Run Locally

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/breast-cancer-prediction.git
   cd breast-cancer-prediction
   pip install -r requirements.txt
   python app.py
