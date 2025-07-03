import streamlit as st

st.set_page_config(page_title="🔁 Google Unit Converter", layout="centered")
st.title("🔁 Google Unit Converter")
st.write("Convert values between different units — just like Google!")

# Conversion logic
def convert_units(category, from_unit, to_unit, value):
    try:
        value = float(value)
    except:
        return "Invalid input"

    if category == "Length":
        factors = {
            "Meters": 1,
            "Kilometers": 1000,
            "Centimeters": 0.01,
            "Millimeters": 0.001,
            "Miles": 1609.34,
            "Yards": 0.9144,
            "Feet": 0.3048,
            "Inches": 0.0254,
        }

    elif category == "Weight":
        factors = {
            "Kilograms": 1,
            "Grams": 0.001,
            "Milligrams": 1e-6,
            "Pounds": 0.453592,
            "Ounces": 0.0283495,
        }

    elif category == "Time":
        factors = {
            "Seconds": 1,
            "Minutes": 60,
            "Hours": 3600,
            "Days": 86400,
        }

    elif category == "Temperature":
        if from_unit == to_unit:
            return value
        if from_unit == "Celsius":
            return (
                value * 9 / 5 + 32
                if to_unit == "Fahrenheit"
                else value + 273.15
            )
        if from_unit == "Fahrenheit":
            return (
                (value - 32) * 5 / 9
                if to_unit == "Celsius"
                else (value - 32) * 5 / 9 + 273.15
            )
        if from_unit == "Kelvin":
            return (
                value - 273.15
                if to_unit == "Celsius"
                else (value - 273.15) * 9 / 5 + 32
            )
        return "Invalid"

    else:
        return "Unsupported Category"

    # Use conversion factor
    base_value = value * factors[from_unit]
    converted = base_value / factors[to_unit]
    return round(converted, 6)

# Unit Categories
categories = {
    "Length": ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"],
    "Weight": ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"],
    "Time": ["Seconds", "Minutes", "Hours", "Days"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

# UI Elements
category = st.selectbox("Choose Category", list(categories.keys()))
units = categories[category]

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From Unit", units)
with col2:
    to_unit = st.selectbox("To Unit", units)

value = st.text_input("Enter Value", placeholder="e.g. 100")

if st.button("Convert"):
    result = convert_units(category, from_unit, to_unit, value)
    st.success(f"{value} {from_unit} = {result} {to_unit}")
