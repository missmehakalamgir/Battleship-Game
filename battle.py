import streamlit as st
import random

# --- OOP Classes ---

class Ship:
    def __init__(self, size=1):
        self.size = size
        self.positions = []

    def place(self, board_size):
        self.positions = [(random.randint(0, board_size - 1), random.randint(0, board_size - 1))]

class Board:
    def __init__(self, size=5):
        self.size = size
        self.grid = [["🟦" for _ in range(size)] for _ in range(size)]
        self.ships = []
        self.hits = set()
        self.misses = set()

    def place_ship(self):
        ship = Ship()
        ship.place(self.size)
        self.ships.append(ship)

    def check_hit(self, row, col):
        for ship in self.ships:
            if (row, col) in ship.positions:
                self.hits.add((row, col))
                return True
        self.misses.add((row, col))
        return False

    def all_ships_sunk(self):
        all_positions = set()
        for ship in self.ships:
            all_positions.update(ship.positions)
        return all_positions.issubset(self.hits)

# --- Streamlit App Logic ---

st.set_page_config(page_title="Battleship Game", layout="centered")
st.title("🛳️ Single Player Battleship Game")
st.markdown("Try to sink the hidden ships!")

# Game state initialization
if "board" not in st.session_state:
    st.session_state.board = Board()
    for _ in range(3):  # place 3 ships
        st.session_state.board.place_ship()

board = st.session_state.board
status_placeholder = st.empty()

# Show grid
for row in range(board.size):
    cols = st.columns(board.size)
    for col in range(board.size):
        cell = "🟦"
        if (row, col) in board.hits:
            cell = "💥"
        elif (row, col) in board.misses:
            cell = "❌"
        if cols[col].button(cell, key=f"{row}-{col}"):
            if (row, col) in board.hits or (row, col) in board.misses:
                status_placeholder.info("Already targeted this cell!")
            elif board.check_hit(row, col):
                status_placeholder.success("🎯 It's a HIT!")
            else:
                status_placeholder.warning("💨 It's a MISS!")

# End game
if board.all_ships_sunk():
    st.success("🏆 Congratulations! You sank all ships!")
    if st.button("Play Again"):
        del st.session_state.board
