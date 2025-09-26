import streamlit as st
import sidebar

# Title of App
st.title("Web Development Lab01")

# Assignment Data 
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Web Development - Section E")
st.subheader("Cainen Crowder")


# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Page Name**: Description
#       2. **Page Name**: Description
#       3. **Page Name**: Description
#       4. **Page Name**: Description

st.write("""
Welcome to my Streamlit Web Development Lab01 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. **About Me**:This "About Me" page serves as my digital professional introduction. The page opens with a little bit of my story, I’m a civil engineering student at Georgia Tech with a strong background in real estate, public sector engineering, and music direction. Outside of academics, I’m passionate about wellness, performance, and creating meaningful experiences through music, leadership, and community involvement.
2. **Music Quiz**: This quiz takes a part of me and shares it with you, lets see your knowledge of some basic music question and see if your vibes really are that good!


""")

# render shared sidebar links
sidebar.render_links()

