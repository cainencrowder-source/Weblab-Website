import streamlit as st
import random
import numpy as np

QUIZ_QUESTIONS = {
    "q1": {
        "text": "Which genre relies heavily on the 'four on the floor' kick drum pattern?",
        "type": "radio",
        "options": ["Jazz", "Dubstep", "House", "Reggae"],
        "answer": "House"
    },
    "q2": {
        "text": "Estimate the BPM (Beats Per Minute) range for most modern Trap/Hip-Hop tracks.",
        "type": "number_input",
        "min_value": 60, 
        "max_value": 200,
        "correct_range": (130, 160)
    },
    "q3": {
        "text": "Which instruments are essential to a traditional Bluegrass ensemble?",
        "type": "multiselect",
        "options": ["Banjo", "Electric Guitar", "Drums", "Fiddle", "Upright Bass"],
        "answer": ["Banjo", "Fiddle", "Upright Bass"]
    },
    "q4": {
        "text": "Which feature is most typical of Grunge music?",
        "type": "radio",
        "options": ["Synthesizer solos", "Loud-quiet dynamics", "Complex time signatures", "Latin percussion"],
        "answer": "Loud-quiet dynamics"
    },
    "q5": {
        "text": "What is the primary language used in K-Pop songs?",
        "type": "radio",
        "options": ["Japanese", "Korean", "Mandarin", "English"],
        "answer": "Korean"
    }
}

st.title("🎧 The Ultimate Musical Genre Challenge 🎶")
st.write("Test your knowledge across the musical spectrum, from the club to the concert hall!")
st.image('/Users/cainencrowder/Downloads/WebDevLab01 2/WebDevLab01/Images/music.jpg', caption="Which genre is calling you?", use_container_width=True)

score = 0
results = {}

st.header("Your Musical Knowledge Check")

q1_answer = st.radio(
    QUIZ_QUESTIONS["q1"]["text"],
    QUIZ_QUESTIONS["q1"]["options"],
    key='q1_key'
)

q2_answer = st.number_input(
    QUIZ_QUESTIONS["q2"]["text"],
    min_value=QUIZ_QUESTIONS["q2"]["min_value"],
    max_value=QUIZ_QUESTIONS["q2"]["max_value"],
    step=5,
    key='q2_key'
)

q3_answer = st.multiselect(
    QUIZ_QUESTIONS["q3"]["text"],
    QUIZ_QUESTIONS["q3"]["options"],
    key='q3_key'
)

q4_answer = st.radio(
    QUIZ_QUESTIONS["q4"]["text"],
    QUIZ_QUESTIONS["q4"]["options"],
    key='q4_key'
)

q5_answer = st.radio(
    QUIZ_QUESTIONS["q5"]["text"],
    QUIZ_QUESTIONS["q5"]["options"],
    key='q5_key'
)

if st.button("Submit My Answers!"):
    if q1_answer == QUIZ_QUESTIONS["q1"]["answer"]:
        score += 1
    
    min_bpm, max_bpm = QUIZ_QUESTIONS["q2"]["correct_range"]
    if min_bpm <= q2_answer <= max_bpm:
        score += 1

    required_answers = set(QUIZ_QUESTIONS["q3"]["answer"])
    submitted_answers = set(q3_answer)
    if submitted_answers == required_answers:
        score += 1
        
    if q4_answer == QUIZ_QUESTIONS["q4"]["answer"]:
        score += 1
    if q5_answer == QUIZ_QUESTIONS["q5"]["answer"]:
        score += 1

    st.metric(label="Your Final Score", value=f"{score} / 5", delta=f"{score*20}% Accuracy") #NEW
    
    st.subheader("Your Post-Quiz Vibe Check")
    if score >= 4:
        st.success("You are a TRUE MUSIC MAN! 🏆")
        st.image('/Users/cainencrowder/Downloads/WebDevLab01 2/WebDevLab01/Images/Trophy.jpg', caption="Your Vibes Are TOO GOOD, ROCK ON🤘", width=300)
         #New
        st.balloons()#New
    else:
        st.warning("Keep exploring! Music is a universe waiting for you.")
        st.image('/Users/cainencrowder/Downloads/WebDevLab01 2/WebDevLab01/Images/Your Learning.png', caption="Time to study up!", width=300)
          #New
