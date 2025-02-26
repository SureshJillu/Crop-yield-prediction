# 🌾 Crop Yield Prediction 🚜

## 📌 Overview
This project predicts **crop yield** based on environmental factors using an **ensemble learning model** (Lasso Regression + Decision Tree). The web application, built with **Flask**, provides an intuitive UI for users to input values and receive predictions.  

Additionally, a **"Did You Know?"** box fetches **real-time interesting facts** every 30 seconds, enhancing user engagement.  

---


## ⚙️ Features
✅ **ML Model**: Stacking Regressor (Lasso + Decision Tree)  
✅ **Flask-Based UI**: User-friendly design with dropdowns for region & crop selection  
✅ **Real-Time Fun Facts**: Displays **changing random interesting facts**  

---

## 📁 Project Structure
```
📦 Crop Yield Prediction
├── 📂 static
│   ├── style.css              # UI Styling
├── 📂 templates
│   ├── index.html             # Frontend Page
├── app.py                     # Flask Backend
├── preprocesser.pkl           # Preprocessing Pipeline
├── stacking_model.pkl         # Trained ML Model
├── yield.csv                  # Dataset 
├── requirements.txt           # Python Dependencies
├── README.md                  # Project Documentation
```

---

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/YOUR_USERNAME/Crop-Yield-Prediction.git
cd Crop-Yield-Prediction
```

### 2️⃣ Set Up a Virtual Environment (Recommended)
Create and activate a virtual environment:  

#### 🔹 Windows (CMD/PowerShell)
```sh
python -m venv venv
venv\Scripts\activate
```

#### 🔹 macOS/Linux (Terminal)
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
Ensure **pip** is up to date, then install dependencies:  
```sh
pip install --upgrade pip
pip install -r requirements.txt
```

### 4️⃣ Run the Application
Start the Flask server:  
```sh
python app.py
```
The application will now be available at:  
🔗 **http://127.0.0.1:5000/**  

---

## 🧠 How It Works

1️⃣ The **user enters**:
   - **Region (Area)**
   - **Crop Name (Item)**
   - **Year**
   - **Avg Temperature**
   - **Avg Rainfall**
   - **Pesticide Usage**  

2️⃣ The **preprocessor.pkl** file transforms the inputs into a format suitable for the model.  

3️⃣ The **stacking_model.pkl** predicts the **expected crop yield**.  

4️⃣ The **Did You Know? box** fetches **real-time interesting facts** every 30 seconds.  

---

## 📌 Future Improvements 
- 🤖 **More Advanced Models**: Experiment with deep learning techniques for better accuracy.  
- 🌎 **Geospatial Integration**: Use maps to select regions dynamically.  

