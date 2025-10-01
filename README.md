🌱 KrishiRakshak – From Soil to Sky, We Care with Flair
An AI-driven platform to predict agricultural & financial risks for farmers, and provide timely advisory + financial rescue solutions (loans, subsidies, insurance).


🚀 Overview
Farmers face unpredictable risks such as climate variability, pest attacks, soil degradation, and financial instability.
KrishiRakshak integrates AI-powered crop risk prediction with credit & financial safety nets, delivering real-time, localized insights and proactive financial support.
This solution aims to minimize losses, improve resilience, and ensure sustainable farming.


🏗️ Features
✅ Crop Risk Prediction – Predict pest/drought/yield risks using weather, soil & satellite data.
✅ Credit Risk Prediction – Farmer-level creditworthiness scores for financial partners.
✅ Ensemble Risk Index (ERI) – Unified score combining agricultural + financial risk.
✅ Advisory Pipeline – Farmers ask questions & receive AI-driven recommendations.
✅ Financial Rescue Module – Automated suggestions for loans, subsidies, insurance.
✅ Localized Alerts – SMS/voice-based advisories in regional languages.


⚙️ Tech Stack
Backend: Python (Flask, FastAPI-ready)
Machine Learning: PyTorch
Database: PostgreSQL
Frontend: HTML/CSS (Flask templates), scalable to React
APIs: OpenWeather API (climate), extendable to Satellite APIs



📂 Directory Structure

KrishiRakshak_UI_Pro/
│── app.py # Flask entry point
│── requirements.txt # Dependencies
│── services/
│ ├── lang.py # Language/advisory service
│ └── __init__.py
│── templates/
│ ├── index.html # Homepage
│ └── pipeline.html # Advisory pipeline UI
│── static/
│ └── style.css # Frontend styling



🔧 Setup & Installation

1. Clone Repository
git clone https://github.com/AgarwalAayushi/KrishiRakshak.git
cd KrishiRakshak_UI_Pro

2. Create Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the App
python app.py

5. Access in Browser
http://127.0.0.1:5000/


🎥 Demo

📺 https://www.loom.com/share/025415308cec48bdae7e97efaa82cfb6?sid=257e3f1e-7ee0-402e-bc1f-1d4fba4a5cc1

The demo shows:

Farmer landing page
Advisory pipeline with farmer queries
Successful recommendation (e.g., pesticide advice)
Failure case + roadmap to fix


🔬 Known Limitations
Limited dataset for niche crops
Connectivity challenges in rural areas
Financial partner integrations are simulated (not live)


🛠️ Future Work
IoT soil sensors & drone imagery
Native Android/iOS app with offline mode
Multilingual NLP for regional dialects
Blockchain-based farmer credit profiles
Financial marketplace integration


📊 Success Metrics
Adoption rate among farmers
Reduction in loan defaults
Timeliness of alerts
Farmer satisfaction (feedback ratings)
Partner adoption (banks, insurance)


👩‍💻 Contributors
Aayushi Agarwal – Developer
