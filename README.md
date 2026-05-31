🚢 FisherGuard AI
An Explainable AI-Based Web System for Fishermen Safety, Location and Border Risk Assessment

FisherGuard AI is a web-based safety monitoring and risk assessment platform designed to improve the safety of fishermen operating in coastal and international maritime regions. The system combines Explainable Artificial Intelligence (XAI), risk prediction, border proximity detection, and real-time vessel monitoring to help fishermen avoid dangerous situations at sea.

📌 Project Overview

Fishing is one of the most hazardous occupations due to:

Extreme weather conditions
High sea waves
Poor visibility
Maritime border crossing risks
Lack of intelligent safety prediction systems

FisherGuard AI provides a browser-accessible platform that predicts voyage safety risks and explains the reasons behind each prediction using Explainable AI techniques.

🎯 Objectives
Predict fishing voyage risk levels.
Detect proximity to international maritime borders.
Identify dangerous maritime zones.
Provide Explainable AI (XAI) insights.
Monitor multiple vessels through a live dashboard.
Display vessel locations on an interactive map.
Offer actionable safety recommendations.
✨ Key Features
🌊 Multi-Factor Risk Prediction

The system evaluates:

Wind Speed
Wave Height
Visibility
Fishing Experience
Border Proximity
Danger Zone Presence

and generates a risk score between 0 and 100.

🧠 Explainable AI (XAI)
SHAP-inspired contribution analysis
Visual risk factor breakdown
Natural language explanations
🚨 Border Risk Detection
Detects proximity to maritime boundaries
Alerts fishermen before entering restricted zones
Prevents accidental border crossings
🗺️ Interactive Live Map
Real-time vessel tracking
Border zone visualization
Danger zone overlays
Risk-colored vessel markers
📊 Safety Dashboard
Fleet monitoring
Risk distribution analysis
Active alert notifications
Auto-refreshing live updates
📱 Browser Based Access
No special hardware required
Accessible from any modern browser
Mobile-friendly interface
🏗️ System Architecture
User Interface
     │
     ▼
 Flask Web Server
     │
 ┌───┼───────────────┐
 │   │               │
 ▼   ▼               ▼
Risk Engine     XAI Module
                     │
                     ▼
          Border Detection
                     │
                     ▼
              JSON Response
                     │
                     ▼
      Dashboard / Map / Alerts
🛠️ Technology Stack
Backend
Python 3.11
Flask 3.0
Frontend
HTML5
CSS3
JavaScript (ES6)
Mapping
Leaflet.js
CartoDB Dark Matter Tiles
AI & Analytics
Rule-Based Risk Scoring Engine
SHAP-Inspired Explainable AI
Geographic Computation
Haversine Formula
📂 Project Structure
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
⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/FisherGuard-AI.git

cd FisherGuard-AI
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Application
python app.py
5️⃣ Open Browser
http://127.0.0.1:5000
📈 Risk Classification
Risk Score	Risk Level
0 – 39	LOW
40 – 69	MEDIUM
70 – 100	HIGH
🚨 Safety Recommendations
LOW Risk
Safe to proceed.
Follow standard safety practices.
MEDIUM Risk
Exercise caution.
Monitor weather and sea conditions.
HIGH Risk
Avoid departure.
Seek shelter immediately.
Contact coast guard if necessary.
🌍 Sustainable Development Goals (SDGs)

This project supports:

SDG 3 – Good Health and Well-Being
SDG 9 – Industry, Innovation and Infrastructure
SDG 10 – Reduced Inequalities
SDG 16 – Peace, Justice and Strong Institutions
🔮 Future Enhancements
Live Weather API Integration
AIS Vessel Tracking Integration
Machine Learning Risk Prediction Models
Multi-language Support
PostgreSQL Database Integration
SMS and Mobile Alerts
Mobile Application Development
👨‍💻 Authors

Abinasri E
B.Tech Artificial Intelligence and Data Science

Ancy Antony A L
B.Tech Artificial Intelligence and Data Science

St. Joseph's College of Engineering, Chennai
Academic Year: 2025–2026

📜 License

This project is developed for academic and research purposes. Feel free to modify and extend it for educational use.

⭐ FisherGuard AI aims to make fishing safer through Explainable Artificial Intelligence and real-time maritime risk assessment.
