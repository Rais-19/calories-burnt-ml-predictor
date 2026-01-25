import streamlit as st
import requests

# URL FastAPI backend 
API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Calories Burnt Calculator",
    page_icon="🔥",
    layout="centered"
)

#Header:
st.title("🔥 Calories Burnt Calculator")
st.markdown("**Quickly see how many calories you burn during your workout!** 💪")

st.info("Just fill in your details below — no need to be exact, just your best guess!")

with st.form("workout_form", clear_on_submit=False):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox(
            "Are you male or female?",
            ["male", "female"],
            index=0,
            help="Just choose what best describes you"
        )

        age = st.number_input(
            "How old are you? (years)",
            min_value=10,
            max_value=100,
            value=30,
            step=1,
            help="Your age in years"
        )

        weight = st.number_input(
            "Your weight (kg)",
            min_value=30.0,
            max_value=200.0,
            value=75.0,
            step=0.5,
            help="Your current body weight in kilograms (kg)"
        )

    with col2:
        height = st.number_input(
            "Your height (cm)",
            min_value=100.0,
            max_value=250.0,
            value=175.0,
            step=1.0,
            help="Your height in centimeters (cm) — about 170-180 cm for most adults"
        )

        duration = st.number_input(
            "How long was your workout? (minutes)",
            min_value=5.0,
            max_value=300.0,
            value=45.0,
            step=5.0,
            help="Total time you exercised in minutes (e.g., 30 min jog = 30)"
        )

        heart_rate = st.number_input(
            "Average heart rate during workout (beats per minute)",
            min_value=50,
            max_value=200,
            value=120,
            step=1,
            help="How fast your heart was beating on average — you can check on a smartwatch or just guess"
        )

        body_temp = st.number_input(
            "Your body temperature during exercise (°C)",
            min_value=35.0,
            max_value=42.0,
            value=38.5,
            step=0.1,
            help="Usually around 37-39°C during exercise — if you don't know, leave it at 38.5"
        )

    submit_button = st.form_submit_button("Calculate Calories Burnt 🔥", use_container_width=True)

if submit_button:
    payload = {
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp
    }

    try:
        with st.spinner("Calculating your calorie burn..."):
            response = requests.post(API_URL, json=payload, timeout=10)
            response.raise_for_status()

            result = response.json()
            calories = result["predicted_calories"]

            # Success message :
            st.success(f"**You burned approximately {calories:.0f} calories!** 🔥")
            st.balloons()

            # Visual feedback:
            st.progress(min(calories / 600, 1.0))  
            st.caption(f"That's like burning off {calories / 100:.1f} big chocolate bars!")

    except requests.exceptions.RequestException as e:
        st.error(f"Couldn't connect to the calculator. Is the backend running? ({e})")
    except Exception as e:
        st.error(f"Something went wrong: {e}")