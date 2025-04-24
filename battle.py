import streamlit as st
import random

# Define the Flashcard class
class Flashcard:
    def __init__(self, question, answer, category):
        self.question = question
        self.answer = answer
        self.category = category

# Define the FlashcardApp class
class FlashcardApp:
    def __init__(self):
        self.flashcards = []
        self.categories = []
        self.score = 0
        self.total_flashcards = 0

    def add_flashcard(self, question, answer, category):
        flashcard = Flashcard(question, answer, category)
        self.flashcards.append(flashcard)
        if category not in self.categories:
            self.categories.append(category)

    def get_flashcard(self):
        return random.choice(self.flashcards)  # Select a random flashcard

    def check_answer(self, user_answer, correct_answer):
        if user_answer.strip().lower() == correct_answer.strip().lower():
            self.score += 1
            return True
        return False

    def show_score(self):
        return f"Score: {self.score} / {self.total_flashcards}"

# Initialize the flashcard app
app = FlashcardApp()

# Streamlit Interface
st.title("Flashcard Learning App")
st.write("Welcome to the Flashcard Learning App! Add questions and answers to create flashcards and test your knowledge.")

# Add flashcard functionality
st.header("Add Flashcard")
with st.form(key="add_flashcard_form"):
    question = st.text_input("Enter Question")
    answer = st.text_input("Enter Answer")
    category = st.selectbox("Select Category", ["Python", "Next.js", "English"])
    submit_button = st.form_submit_button(label="Add Flashcard")

    if submit_button:
        app.add_flashcard(question, answer, category)
        st.success("Flashcard added successfully!")

# Display the categories and flashcard questions
st.sidebar.header("Choose Category")
selected_category = st.sidebar.selectbox("Select Category to Practice", app.categories)

st.header(f"Flashcards for {selected_category}")
category_flashcards = [fc for fc in app.flashcards if fc.category == selected_category]

if category_flashcards:
    # Pick a random flashcard for the selected category
    flashcard = app.get_flashcard()

    # Show the question and take input for the answer
    user_answer = st.text_input(f"Question: {flashcard.question}")

    if st.button("Check Answer"):
        if app.check_answer(user_answer, flashcard.answer):
            st.success("Correct!")
        else:
            st.error(f"Incorrect! The correct answer was: {flashcard.answer}")

        # Update progress
        app.total_flashcards += 1
        st.write(app.show_score())
else:
    st.write(f"No flashcards available for {selected_category}. Add more!")

