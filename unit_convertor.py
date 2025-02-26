import streamlit as st


# Page Config 
st.set_page_config(page_title="Unit Converter ⇔", page_icon="📏")

# Title
st.title("Welcome to Unit Converter 📐")
st.header("Convert any unit into different Units easily!")


# Conversion Options
conversion_type = st.selectbox("Select a conversion type:", [
    "Length", "Weight", "Temperature", "Speed"
])


# Conversion Logic
def convert(value, from_unit, to_unit, conversion_dict):
    return value * conversion_dict[from_unit][to_unit]

if conversion_type == "Length":
    length_units = {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084}
    from_unit = st.selectbox("From:", list(length_units.keys()))
    to_unit = st.selectbox("To:", list(length_units.keys()))
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    
    if st.button("Convert"):
        result = value * (length_units[to_unit] / length_units[from_unit])
        st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")

elif conversion_type == "Weight":
    weight_units = {"Grams": 1, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274}
    from_unit = st.selectbox("From:", list(weight_units.keys()))
    to_unit = st.selectbox("To:", list(weight_units.keys()))
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    
    if st.button("Convert"):
        result = value * (weight_units[to_unit] / weight_units[from_unit])
        st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")

elif conversion_type == "Temperature":
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From:", temp_units)
    to_unit = st.selectbox("To:", temp_units)
    value = st.number_input("Enter value:", format="%.2f")
    
    if st.button("Convert"):
        result = None
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value
        
        st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

elif conversion_type == "Speed":
    speed_units = {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694, "Feet per second": 3.28084}
    from_unit = st.selectbox("From:", list(speed_units.keys()))
    to_unit = st.selectbox("To:", list(speed_units.keys()))
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    
    if st.button("Convert"):
        result = value * (speed_units[to_unit] / speed_units[from_unit])
        st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")

# Footer
st.write("---")
st.write("🚀 Convert units quickly and accurately!")
st.write("**Created by Hanishah**")
