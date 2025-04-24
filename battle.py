import streamlit as st

# --- OOP CLASS ---

class BankAccount:
    def __init__(self, name, password, balance=0):
        self.name = name
        self.password = password
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

# --- Create Account or Login ---

if not st.session_state.get("name_entered"):
    option = st.selectbox("Select an action", ["Create Account", "Login"])

    if option == "Create Account":
        user_name = st.text_input("👤 Enter your name:")
        user_password = st.text_input("🔒 Create a password:", type="password")
        if st.button("Create Account"):
            if user_name.strip() == "" or user_password.strip() == "":
                st.warning("Please enter a valid name and password.")
            else:
                st.session_state.account = BankAccount(user_name, user_password)
                st.session_state.name_entered = True
                st.success(f"Account created for {user_name}!")
                st.balloons()

    elif option == "Login":
        login_name = st.text_input("👤 Enter your name to login:")
        login_password = st.text_input("🔒 Enter your password:", type="password")
        if st.button("Login"):
            if login_name == st.session_state.get("account").name and login_password == st.session_state.get("account").password:
                st.session_state.name_entered = True
                st.success(f"Welcome back, {login_name}!")
            else:
                st.error("Invalid credentials. Please try again.")

# --- Banking Interface ---

if st.session_state.get("name_entered"):
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
    if st.button("❌ Logout"):
        st.session_state.clear()
        st.rerun()  # Updated to use st.rerun()
