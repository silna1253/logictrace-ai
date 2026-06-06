import streamlit as st
import google.generativeai as genai

# 1. This sets up the Title of our Web Page
st.set_page_config(page_title="LogicTrace AI", page_icon="💻")

st.title("💻 LogicTrace AI")
st.write("Welcome! This tool helps students find hidden logic mistakes in their code.")

# 2. BACKEND API KEY INTEGRATION (Completely replaces the sidebar text box!)
# This looks for the key in your local secrets file or your live deployment console.
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    st.error("⚠️ Backend Configuration Error: 'GEMINI_API_KEY' is missing from Streamlit Secrets!")
    st.stop()

# 3. Creating the main input boxes for the student
language = st.selectbox("Select Programming Language:", ["Python", "JavaScript", "C++", "Java"])

expected_behavior = st.text_area(
    "What is your code SUPPOSED to do?", 
    placeholder="e.g., It is supposed to print numbers 1 to 10, but it keeps printing 1 forever."
)

source_code = st.text_area(
    "Paste your broken code here:", 
    placeholder="# Paste your code here..."
)

# 4. What happens when the user clicks the blue button
if st.button("Find the Logic Mistake", type="primary"):
    if not source_code or not expected_behavior:
        st.warning("Please fill out both text boxes!")
    else:
        # Show a loading animation while the AI thinks
        with st.spinner("Analyzing your code logic..."):
            try:
                # Connect to the Google Gemini AI
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                # We give the AI clear instructions on how to answer a school student
                prompt = f"""
                You are a friendly, helpful high school Computer Science teacher. 
                A student is confused because their code runs but gives the wrong result.
                
                Language: {language}
                What they want it to do: {expected_behavior}
                Their broken code:
                ```{language}
                {source_code}
                ```
                
                Please help them by writing a response with these exact sections:
                ### 🔍 1. Where the Logic Broke
                Explain in very simple words where their thinking missed a step. 
                
                ### 📊 2. What the Variables Are Doing
                Show a small step-by-step example of how the data changes incorrectly.
                
                ### 🛠️ 3. How to Fix It
                Provide the corrected code block and a quick, encouraging tip to remember for next time!
                """
                
                # Ask the AI for the answer
                response = model.generate_content(prompt)
                
                # Show the answer on the website
                st.success("Done!")
                st.markdown("---")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")
