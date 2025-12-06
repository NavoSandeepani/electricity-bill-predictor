import streamlit as st
import pandas as pd
import joblib

# ----------------- PAGE SETUP -----------------
st.set_page_config(
    page_title="Electricity Bill Predictor",
    page_icon="⚡",
    layout="centered"
)

# ----------------- CSS -----------------
page_css = """
<style>

 /* ---------- HERO TITLE ANIMATION ---------- */
.hero-title {
    text-align: center;
    color: #38bdf8;
    font-size: 2.4rem;
    font-weight: 800;
    animation: heroZoom 0.8s ease-out 0.1s both;
}
@keyframes heroZoom {
    0% { transform: scale(1.3); opacity: 0; }
    60% { transform: scale(1.05); opacity: 1; }
    100% { transform: scale(1); opacity: 1; }
}

/* ---------- INPUT CARD ---------- */
.input-card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 15px;
    width: 460px;
    margin: 0 auto 30px auto;
    box-shadow: 0 12px 35px rgba(0,0,0,0.35);
    backdrop-filter: blur(6px);
}

/* Section title */
.sub-zoom {
    display: inline-block;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 20px;
    transition: transform 0.25s ease, color 0.25s ease;
}

.sub-zoom:hover {
    transform: scale(1.04);
    color: #38bdf8;
}

/* ---------- LABEL ZOOM EFFECT ON FOCUS ---------- */
.stNumberInput label {
    font-size: 3rem;
    font-weight: 600;
    transition: all 0.25s ease-in-out;
}

/* When input is focused → label zoom in */
.stNumberInput:focus-within label {
    font-size: 1.35rem;
    transform: scale(1.18);
    color: #38bdf8;
}

/* Rounded input box */
.stNumberInput input {
    border-radius: 8px !important;
}

</style>
"""
st.markdown(page_css, unsafe_allow_html=True)

# ----------------- LOAD MODEL -----------------
model = joblib.load("best_electricity_model.pkl")

# ----------------- TITLE -----------------
st.markdown(
    "<h1 class='hero-title'>⚡ Sri Lanka Electricity Bill Predictor</h1>",
    unsafe_allow_html=True
)
# ----------------- INPUT FORM -----------------

st.markdown("<h3 class='sub-zoom'>Enter Your Household Details</h3>", unsafe_allow_html=True)

house_size_sqft = st.number_input("House Size (sqft)", min_value=100, max_value=5000, value=1000)
people_in_house = st.number_input("Number of People", min_value=1, max_value=10, value=4)
bulb_count = st.number_input("Number of Bulbs", min_value=0, max_value=50, value=8)
ceiling_fan_count = st.number_input("Number of Ceiling Fans", min_value=0, max_value=10, value=2)
table_fan_count = st.number_input("Number of Table Fans", min_value=0, max_value=10, value=1)
fridge_count = st.number_input("Number of Fridges", min_value=0, max_value=5, value=1)
ac_count = st.number_input("Number of ACs", min_value=0, max_value=5, value=1)
ac_hours_per_day = st.number_input("AC Hours per Day", min_value=0.0, max_value=24.0, value=5.0)
electric_kettle_count = st.number_input("Number of Electric Kettles", min_value=0, max_value=5, value=1)
washing_machine_count = st.number_input("Number of Washing Machines", min_value=0, max_value=5, value=1)
tv_count = st.number_input("Number of TVs", min_value=0, max_value=5, value=1)
computer_count = st.number_input("Number of Computers", min_value=0, max_value=5, value=1)
rice_cooker_count = st.number_input("Number of Rice Cookers", min_value=0, max_value=5, value=1)

st.markdown("</div>", unsafe_allow_html=True)

# ----------------- PREDICTION -----------------
if st.button("Predict Electricity Bill"):
    input_data = pd.DataFrame({
        "house_size_sqft": [house_size_sqft],
        "people_in_house": [people_in_house],
        "bulb_count": [bulb_count],
        "ceiling_fan_count": [ceiling_fan_count],
        "table_fan_count": [table_fan_count],
        "fridge_count": [fridge_count],
        "ac_count": [ac_count],
        "ac_hours_per_day": [ac_hours_per_day],
        "electric_kettle_count": [electric_kettle_count],
        "washing_machine_count": [washing_machine_count],
        "tv_count": [tv_count],
        "computer_count": [computer_count],
        "rice_cooker_count": [rice_cooker_count]
    })

    predicted_bill = model.predict(input_data)[0]
    st.success(f"Predicted Monthly Electricity Bill: LKR {predicted_bill:.2f}")
