#Guessing game 1- User guesses the number

import streamlit as st
import random
st.sidebar.title("Choose any one")
option=st.sidebar.radio("Options:",("Guessing game 1", "Guessing game 2", "Portfolio"))
if option== "Guessing game 1":
 #intro
 st.title("**GUESSING GAME 1**")
 st.text("Are you ready to guess the number?")
 #randomise guess
 if 'Gnum' not in st.session_state:
    st.session_state.Gnum = random.randint(0,100)
 #slider
 num = st.slider("Guess the number", min_value=1, max_value=100)
 #checking guess
 def check_guess():
   if num ==st.session_state.Gnum:
      st.success("Congratulations! You guessed the correct number!")
      st.session_state.Gnum = random.randint(1, 100)
   elif num < st.session_state.Gnum:
      st.text("Try a higher number!")
   else: 
      st.text("Try a lower number!")
 #button
 st.button("Submit Guess", on_click=check_guess) 


 #Guessing game 2- Computer guesses the number
elif option== "Guessing game 2":
 # Title
 st.title("Guessing Game: Computer Guesses Your Number") 

 st.write(f"Is your number {st.session_state.guess}?")
 if 'low' not in st.session_state:
     st.session_state.low = 1
 if 'high' not in st.session_state:
     st.session_state.high = 100
 if 'guess' not in st.session_state:
     st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
 if 'found' not in st.session_state:
     st.session_state.found = False
 # Button
 if st.button("Try Higher"):
     if st.session_state.guess < st.session_state.high:
         st.session_state.low = st.session_state.guess + 1
         st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
     else:
         st.write("No more higher numbers to try!")
 if st.button("Try Lower"):
     if st.session_state.guess > st.session_state.low:
         st.session_state.high = st.session_state.guess - 1
         st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
     else:
         st.write("No more lower numbers to try!")
 if st.button("You Found It!"):
     st.session_state.found = True
 #result
 if st.session_state.found:
     st.success(f"The computer found your number: {st.session_state.guess}!")
 else:
     st.write("Guide the computer to guess your number using the buttons.")


# Portfolio Section
if option== "Portfolio":
 st.title("Welcome to My Portfolio")
 # Intro
 st.header("About Me")
 st.write(""" Hi! I'm Dharshika Pugalenthi, a passionate I-Year B.Tech student in Artificial Intelligence and Data Science at Kgisl Institute of Technology.
            I'm enthusiastic about the field of Technology and exploring the ways technology and business strategies intersect. 
            I would like to be a BI(BUSINESS INTELLIGENCE) Developer/Analyst in the future.""")
 # Skills
 st.header("Skills")
 st.write("""- I am currently developing my skills in Python, the most important programming language these days. Learning Streamlit along with it, which helps me to do better projects.
       - I like designing digital spaces, especially in Canva.""")
 # Projects
 st.header("Projects")
 st.write(""" As I am just developing my skills in Python, I have done quite basic projects in it. 
         Some of them are:
        - **Project 1**: Creating a guessing Game- User guessing
        - **Project 2**: Loan Eligibility calculating app.
        - **Project 3**: Python code on testing Armstrong numbers.""")
 # Contact
 st.header("Contact Me")
 st.write("**Email**: dharshikapugal@gmail.com")
 st.write("Thank you for visiting my portfolio!")