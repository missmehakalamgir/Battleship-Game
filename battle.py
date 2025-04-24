import streamlit as st
import random
import time

# --- OOP Classes ---

class Card:
    def __init__(self, value):
        self.value = value
        self.is_matched = False
        self.is_flipped = False

class MemoryGame:
    def __init__(self):
        emojis = ['🍎', '🐶', '🚗', '⚽', '🌈', '🎵', '🍕', '🌻']
        deck = emojis * 2
        random.shuffle(deck)
        self.grid = [Card(value) for value in deck]
        self.first_card_index = None
        self.matches = 0
        self.total_pairs = len(deck) // 2

    def flip_card(self, index):
        card = self.grid[index]
        if card.is_matched or card.is_flipped:
            return False

        card.is_flipped = True
        if self.first_card_index is None:
            self.first_card_index = index
        else:
            first_card = self.grid[self.first_card_index]
            if first_card.value == card.value:
                card.is_matched = True
                first_card.is_matched = True
                self.matches += 1
            else:
                time.sleep(0.5)  # Pause before hiding mismatched cards
                card.is_flipped = False
                first_card.is_flipped = False
            self.first_card_index = None
        return True

    def is_won(self):
        return self.matches == self.total_pairs

# --- Streamlit Setup ---

st.set_page_config(page_title="🧠 Memory Matching Game", layout="centered")
st.title("🧠 Card Matching Game")

if "game" not in st.session_state:
    st.session_state.game = MemoryGame()

game = st.session_state.game
status_placeholder = st.empty()

# Display 4x4 Grid
grid_size = 4
for row in range(grid_size):
    cols = st.columns(grid_size)
    for col in range(grid_size):
        index = row * grid_size + col
        card = game.grid[index]
        if card.is_flipped or card.is_matched:
            cols[col].button(card.value, key=str(index), disabled=True)
        else:
            if cols[col].button("❓", key=str(index)):
                game.flip_card(index)

# Win Message
if game.is_won():
    st.balloons()
    st.success("🎉 You matched all the cards!")
    if st.button("Play Again"):
        del st.session_state.game
