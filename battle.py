import streamlit as st
import datetime

# Class for handling questions related to Python and Streamlit
class PersonalAssistantBot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello! I'm {self.name}, your personal assistant. How can I help you with Python or Streamlit today?"

    def provide_python_help(self, question):
        # Example responses based on common Python-related questions
        if "list" in question.lower():
            return "In Python, a list is an ordered collection of items. You can create a list using square brackets. Example: `my_list = [1, 2, 3]`"
        elif "dictionary" in question.lower():
            return "A dictionary in Python is a collection of key-value pairs. You can create one using curly braces. Example: `my_dict = {'key': 'value'}`"
        elif "function" in question.lower():
            return "A function in Python is defined using the `def` keyword. Example: `def my_function():`"
        elif "for loop" in question.lower():
            return "A for loop in Python allows you to iterate over a sequence. Example: `for i in range(5):`"
        elif "import" in question.lower():
            return "In Python, you can import modules using the `import` keyword. Example: `import math`"
        else:
            return "I can help with Python! Please ask a specific question, and I'll do my best to assist."

    def provide_streamlit_help(self, question):
        # Example responses for Streamlit-related questions
        if "st.title" in question.lower():
            return "In Streamlit, you can set the title of your app using `st.title('Your Title')`."
        elif "st.button" in question.lower():
            return "The `st.button()` widget in Streamlit creates a button. Example: `if st.button('Click me'): ...`"
        elif "st.write" in question.lower():
            return "`st.write()` is a versatile function that can display text, data, or even charts in Streamlit. Example: `st.write('Hello World!')`"
        elif "st.text_input" in question.lower():
            return "`st.text_input()` creates a text input box. Example: `name = st.text_input('Enter your name')`"
        elif "st.sidebar" in question.lower():
            return "You can add elements to the sidebar in Streamlit using `st.sidebar`. Example: `st.sidebar.button('Click')`."
        else:
            return "Ask me something related to Streamlit, and I'll help you out!"

    def help_with_question(self, question):
        # Check if the question is related to Python or Streamlit
        if "python" in question.lower():
            return self.provide_python_help(question)
        elif "streamlit" in question.lower():
            return self.provide_streamlit_help(question)
        else:
            return "I can assist with Python or Streamlit. Please ask your question again with one of these keywords."


# Streamlit App Layout
st.title("Personal Assistant Bot for Python and Streamlit")

# Create the assistant bot instance
bot = PersonalAssistantBot(name="Buddy")

# Greet the user
st.subheader(bot.greet())

# Input text box for user question
question = st.text_input("Ask me anything related to Python or Streamlit:")

# Provide response based on the user's question
if question:
    response = bot.help_with_question(question)
    st.write(response)

# Instructions to guide users
st.markdown("""
### How to Use:
- Ask me questions related to **Python** or **Streamlit**.
- Example questions:
    - "How do I create a list in Python?"
    - "What is the use of st.button in Streamlit?"
    - "How can I define a function in Python?"
    - "How do I import a module in Python?"
""")
