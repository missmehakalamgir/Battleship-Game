import streamlit as st

# --- OOP CLASS ---

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"₹{amount} deposited successfully. New balance: ₹{self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"₹{amount} withdrawn successfully. New balance: ₹{self.balance}"
        else:
            return "⚠️ Insufficient balance!"

    def check_balance(self):
        return f"💰 Current Balance: ₹{self.balance}"


# --- STREAMLIT UI ---

st.set_page_config(page_title="🏦 MyBank App", layout="centered")
st.title("🏦 Welcome to MyBank")
st.markdown("### Your Simple Digital Bank Interface")

# Session state
if "account" not in st.session_state:
    st.session_state.name_entered = False

# Step 1: Enter user name
if not st.session_state.get("name_entered"):
    user_name = st.text_input("👤 Enter your name to create an account:")

    if st.button("Create Account"):
        if user_name.strip() == "":
            st.warning("Please enter a valid name.")
        else:
            st.session_state.account = BankAccount(user_name)
            st.session_state.name_entered = True
            st.success(f"Account created for {user_name}!")
            st.balloons()

# Step 2: Show Banking Interface
else:
    account = st.session_state.account
    st.markdown(f"### 👋 Hello, **{account.name}**")

    action = st.radio("Select an action", ["Deposit", "Withdraw", "Check Balance"], horizontal=True)

    if action == "Deposit":
        deposit_amount = st.number_input("Enter amount to deposit", min_value=1, step=1)
        if st.button("Deposit"):
            msg = account.deposit(deposit_amount)
            st.success(msg)

    elif action == "Withdraw":
        withdraw_amount = st.number_input("Enter amount to withdraw", min_value=1, step=1)
        if st.button("Withdraw"):
            msg = account.withdraw(withdraw_amount)
            if "Insufficient" in msg:
                st.error(msg)
            else:
                st.success(msg)

    elif action == "Check Balance":
        st.info(account.check_balance())

    st.markdown("---")
    if st.button("❌ Close Account"):
        st.session_state.clear()
        st.experimental_rerun()
