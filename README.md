# 🚢 FisherGuard AI

## 📌 Project Overview

**FisherGuard AI** is an Explainable Artificial Intelligence (XAI)-based web application designed to improve the safety of fishermen operating in coastal and international maritime regions. The system predicts voyage risk levels using multiple environmental and geographical factors and provides transparent explanations for every prediction.

Unlike traditional vessel tracking systems, FisherGuard AI combines **risk prediction, border proximity detection, danger zone identification, and Explainable AI** into a single browser-accessible platform.

This system is suitable for **fishermen, coast guard authorities, maritime safety organizations, and coastal monitoring agencies**.

---

## 🌟 Key Features

* ✅ Multi-factor voyage risk prediction
* 🧠 Explainable AI (XAI) risk analysis
* 🌊 Weather and sea condition assessment
* 🚨 Maritime border proximity alerts
* ⚠️ Danger zone detection
* 📊 Real-time fleet monitoring dashboard
* 🗺️ Interactive live vessel map
* 📱 Browser-based access with no special hardware required

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Leaflet.js

### Backend

* Python
* Flask 3.0

### AI & Analytics

* Rule-Based Risk Scoring Engine
* SHAP-Inspired Explainable AI

### Geographic Processing

* Haversine Distance Formula

### Tools

* VS Code
* GitHub
* Ngrok (for deployment)

---

## 📂 Project Structure

```text
FisherGuard-AI/
│
├── app.py
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── predict.html
│   └── map.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ How It Works

1. User enters vessel location and environmental details.
2. System evaluates:

   * Wind Speed
   * Wave Height
   * Visibility
   * Fishing Experience
   * Border Proximity
   * Danger Zone Presence
3. Risk scoring engine calculates a score between 0–100.
4. Explainable AI module shows factor contributions.
5. Border and danger zone detection modules generate alerts.
6. Dashboard and live map display vessel status in real time.

---

## ▶️ How to Run the Project

### Prerequisites

* Python 3.11 or later
* Flask 3.0
* Internet connection

### Steps

```bash
# Clone repository
git clone https://github.com/your-username/FisherGuard-AI.git

# Navigate to project folder
cd FisherGuard-AI

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## 🧪 Sample Use Cases

### Safe Day Scenario

* Low wind speed
* Good visibility
* Calm sea conditions

Result:

* LOW Risk

### Storm Scenario

* High wind speed
* High wave height
* Poor visibility

Result:

* HIGH Risk with emergency recommendation

### Border Risk Scenario

* Vessel close to international maritime boundary

Result:

* Border Alert generated
* Increased risk score

---

## 🎯 Advantages

* Improves fishermen safety
* Predicts risks before departure
* Prevents accidental border crossings
* Provides transparent AI explanations
* Supports coast guard monitoring
* No expensive hardware required
* Easy to deploy and maintain

---

## 🚀 Future Enhancements

* Live Weather API Integration
* AIS Vessel Tracking Integration
* Machine Learning Risk Prediction Models
* SMS and Mobile Notifications
* Multi-language Support
* PostgreSQL Database Integration
* Mobile Application Development

---

## 🌍 Sustainable Development Goals (SDGs)

* SDG 3 – Good Health and Well-Being
* SDG 9 – Industry, Innovation and Infrastructure
* SDG 10 – Reduced Inequalities
* SDG 16 – Peace, Justice and Strong Institutions

---

## 👩‍💻 Authors

**Abinasri E**
B.Tech – Artificial Intelligence and Data Science

**Ancy Antony A L**
B.Tech – Artificial Intelligence and Data Science

**St. Joseph's College of Engineering, Chennai**

---

## 📜 License

This project is developed for educational and research purposes. Feel free to use, modify, and extend it for academic projects.

⭐ *FisherGuard AI – Empowering Fishermen Safety through Explainable Artificial Intelligence.*

