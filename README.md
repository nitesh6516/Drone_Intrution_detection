# Drone_Intrution_detection

🚁 UAV Intrusion Detection Command Center

AI-powered Drone Network Intrusion Detection System designed to identify cyber attacks in UAV communication signals using Machine Learning and an interactive command-center dashboard.
This project analyzes drone network traffic and detects attacks such as Sybil, Wormhole, Flooding, and Blackhole attacks using an optimized XGBoost classification model.


📌 Project Overview

Unmanned Aerial Vehicles (UAVs) rely on wireless communication networks that are vulnerable to cyber attacks.
This project builds an AI-based intrusion detection system capable of identifying malicious drone network activity.
The system provides a command-center style dashboard that allows users to upload UAV network logs and instantly detect intrusions.


🎯 Features

✔ AI-based UAV intrusion detection
✔ Detection of multiple cyber attacks
✔ High accuracy XGBoost ML model (~96–98%)
✔ Real-time prediction on uploaded datasets
✔ Military-style command center dashboard
✔ Radar scanner visualization
✔ Threat level gauge
✔ Drone tracking simulation
✔ Global attack visualization


🧠 Machine Learning Model

The project uses an XGBoost classifier trained on UAV network traffic data.
Model Pipeline
Dataset preprocessing
Feature engineering
Protocol encoding
Train-test split
XGBoost training
Model deployment with Streamlit

     Model Performance
Metric	                   Score
Accuracy	                ~96–98%
Model	                    XGBoost
Dataset Size	   120,000+ records


📊 Dataset

Dataset used: UAVIDS-2025

The dataset contains UAV network traffic records representing normal and malicious drone communication.
                     Features
   Feature	                                  Description
FlowDuration	                     Duration of communication flow
Protocol	                         Network protocol used
TxPackets	                         Transmitted packets
RxPackets                          Received packets
LostPackets	                       Packet loss
TxPacketRate	                     Transmission rate
RxPacketRate	                     Receive rate
MeanDelay	                         Average network delay
MeanJitter	                       Network jitter
Throughput	                       Network throughput

Attack Classes

Normal
Flooding Attack
Sybil Attack
Wormhole Attack
Blackhole Attack


🖥 System Architecture
UAV Network Data
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
XGBoost ML Model
        │
        ▼
Prediction Engine
        │
        ▼
Streamlit Command Center Dashboard


📂 Project Structure
Drone_Intrusion_Detection
│
├── data
│   └── UAVIDS-2025.csv
│
├── models
│   ├── train_classifier.py
│   ├── evaluate_model.py
│   ├── classifier.pkl
│   └── encoder.pkl
│
├── dashboard
│   ├── app.py
│   └── ui_theme.css
│
├── requirements.txt
└── README.md


⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/yourusername/drone-intrusion-detection.git
2️⃣ Navigate to Project Folder
cd drone-intrusion-detection
3️⃣ Install Dependencies
pip install -r requirements.txt


▶ Running the Project
Train Model
        python models/train_classifier.py
Evaluate Model
        python models/evaluate_model.py
Launch Dashboard
        streamlit run dashboard/app.py
The application will open in your browser.


📷 Dashboard Preview
The command center includes:

• Radar Scanner Visualization
• UAV Attack Detection Table
• Threat Level Gauge
• Attack Distribution Graph
• Global Drone Activity Map
• Live Drone Tracking Simulation

            
                    🚀 Technologies Used
    Category	                           Technology
Programming	                                 Python
ML Framework	                               Scikit-Learn
Model	                                       XGBoost
Data Processing	                             Pandas
Visualization	                               Plotly
Dashboard	                                   Streamlit
Deployment	                                 Local Web Application


📈 Future Improvements

• Real-time drone network monitoring
• Integration with real UAV telemetry
• Deep learning based anomaly detection
• Live radar animation
• Global UAV threat heatmap
• Deployment using Docker or cloud services


👨‍💻 Author

Nitesh Kumar

LinkedIn:
https://linkedin.com/in/nitesh-kumar-5a600716b

GitHub:
https://github.com/nitesh6516

Email:
nk340917@gmail.com
