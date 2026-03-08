import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import random
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Drone Intrusion Detection", layout="wide")

def load_css():
    with open("dashboard/ui_theme.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.title("🚁 Drone Intrusion Detection Command Center")

model = joblib.load("models/classifier.pkl")
encoder = joblib.load("models/encoder.pkl")

def radar_chart():

    theta = np.linspace(0, 2*np.pi, 200)
    r = np.abs(np.sin(4*theta))

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=r,
        theta=np.degrees(theta),
        mode='lines',
        line=dict(color='lime', width=3)
    ))

    fig.update_layout(
        polar=dict(
            bgcolor="#02110a",
            radialaxis=dict(visible=False),
            angularaxis=dict(visible=False)
        ),
        showlegend=False,
        height=350
    )

    return fig

def threat_gauge(score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': "Threat Level"},
        gauge={
            'axis': {'range': [0, 10]},
            'bar': {'color': "red"},
            'steps': [
                {'range': [0, 3], 'color': "green"},
                {'range': [3, 7], 'color': "yellow"},
                {'range': [7, 10], 'color': "red"},
            ],
        }
    ))

    return fig

def drone_positions():

    drones = []

    for i in range(10):
        drones.append({
            "lat": random.uniform(-60,60),
            "lon": random.uniform(-180,180)
        })

    return pd.DataFrame(drones)

uploaded_file = st.file_uploader("Upload UAV Network Dataset")

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    df = df.drop(["FlowID","SrcAddr","DstAddr"], axis=1)

    protocol_encoder = LabelEncoder()
    df["Protocol"] = protocol_encoder.fit_transform(df["Protocol"])

    X = df.drop("label", axis=1)

    predictions = model.predict(X)

    labels = encoder.inverse_transform(predictions)

    df["PredictedAttack"] = labels

    st.subheader("Detection Results")

    st.dataframe(df)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Radar Scanner")

        st.plotly_chart(radar_chart(), use_container_width=True)

    with col2:

        st.subheader("Threat Level")

        threat_score = 7
        st.plotly_chart(threat_gauge(threat_score), use_container_width=True)

    st.subheader("Attack Distribution")

    fig = px.histogram(
        df,
        x="PredictedAttack",
        title="Detected UAV Attacks"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Global Drone Activity")

    globe = px.scatter_geo(
        df,
        lat="MeanDelay/s",
        lon="MeanJitter/s",
        color="PredictedAttack",
        projection="orthographic"
    )

    st.plotly_chart(globe, use_container_width=True)

    st.subheader("Live Drone Tracking")

    tracking = drone_positions()

    track_fig = px.scatter_geo(
        tracking,
        lat="lat",
        lon="lon",
        projection="natural earth"
    )

    st.plotly_chart(track_fig, use_container_width=True)

    if "Wormhole" in df["PredictedAttack"].values:
        st.error("🚨 CRITICAL: Wormhole Attack Detected")

    elif "Blackhole" in df["PredictedAttack"].values:
        st.warning("⚠ High Risk Attack Detected")

    else:
        st.success("✅ Network Secure")