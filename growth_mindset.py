# growth_mindset.

import streamlit as st

# Title
st.title("🌱 Growth Mindset App")

# Introduction
st.subheader("What is a Growth Mindset?")
st.write(
    "A growth mindset is the belief that abilities and intelligence can be developed with effort, learning, and persistence."
)

# User input for motivation
st.subheader("💡 Need Some Motivation?")
challenge = st.text_input("Enter a challenge you're facing:")

if st.button("Get Motivation"):
    if challenge:
        st.success(f"Keep pushing forward! Every challenge helps you grow. 🚀")
    else:
        st.warning("Enter a challenge to receive motivation!")

# Quiz Section
st.subheader("📖 Quick Growth Mindset Quiz")
question = "Which statement reflects a growth mindset?"
options = [
    "I can't do this, so I give up.",
    "Mistakes help me learn and improve.",
    "I'm either good at something or I'm not."
]
answer = st.radio("Choose an option:", options)

if st.button("Submit Answer"):
    if answer == "Mistakes help me learn and improve.":
        st.success("✅ Correct! That's the growth mindset!")
    else:
        st.error("❌ Incorrect. Try again!")

# Encouragement Message
st.subheader("💪 Keep Growing!")
st.write("Remember, every day is a chance to improve. Stay positive and keep learning! 🚀")

