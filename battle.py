import streamlit as st
from PIL import Image

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
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
            font-family: 'Roboto', sans-serif;
        }
        .header {
            font-size: 2.5rem;
            font-weight: 600;
            color: #1a73e8;
        }
        .subheader {
            font-size: 1.5rem;
            color: #5f6368;
        }
        .card {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin: 10px;
            text-align: center;
        }
        .button {
            background-color: #1a73e8;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 1.2rem;
            cursor: pointer;
            transition: all 0.3s;
        }
        .button:hover {
            background-color: #0056b3;
        }
        .error {
            color: #e53935;
            font-size: 1rem;
        }
        .success {
            color: #388e3c;
            font-size: 1rem;
        }
        .input-field {
            width: 100%;
            padding: 10px;
            font-size: 1.2rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .input-field:focus {
            outline: none;
            border-color: #1a73e8;
        }
    </style>
""", unsafe_allow_html=True)

# Session state
if "account" not in st.session_state:
    st.session_state.name_entered = False

# --- Create Account or Login ---

if not st.session_state.get("name_entered"):
    option = st.selectbox("Select an action", ["Create Account", "Login"], key="action_select")

    if option == "Create Account":
        st.markdown('<p class="header">Create Your Account</p>', unsafe_allow_html=True)
        user_name = st.text_input("👤 Enter your name:", key="create_name")
        user_password = st.text_input("🔒 Create a password:", type="password", key="create_password")
        
        if st.button("Create Account", key="create_button"):
            if user_name.strip() == "" or user_password.strip() == "":
                st.markdown('<p class="error">Please enter a valid name and password.</p>', unsafe_allow_html=True)
            else:
                st.session_state.account = BankAccount(user_name, user_password)
                st.session_state.name_entered = True
                st.success(f"Account created for {user_name}!", icon="✅")
                st.balloons()

    elif option == "Login":
        st.markdown('<p class="header">Login to Your Account</p>', unsafe_allow_html=True)
        login_name = st.text_input("👤 Enter your name to login:", key="login_name")
        login_password = st.text_input("🔒 Enter your password:", type="password", key="login_password")
        
        if st.button("Login", key="login_button"):
            if login_name == st.session_state.get("account").name and login_password == st.session_state.get("account").password:
                st.session_state.name_entered = True
                st.success(f"Welcome back, {login_name}!", icon="✅")
            else:
                st.markdown('<p class="error">Invalid credentials. Please try again.</p>', unsafe_allow_html=True)

# --- Banking Interface ---

if st.session_state.get("name_entered"):
    account = st.session_state.account
    st.markdown(f'<p class="header">Welcome, **{account.name}**</p>', unsafe_allow_html=True)

    action = st.radio("Select an action", ["Deposit", "Withdraw", "Check Balance"], horizontal=True, key="action_select_radio")

    if action == "Deposit":
        st.markdown('<p class="subheader">Deposit Amount</p>', unsafe_allow_html=True)
        deposit_amount = st.number_input("Enter amount to deposit", min_value=1, step=1, key="deposit_amount")
        if st.button("Deposit", key="deposit_button"):
            msg = account.deposit(deposit_amount)
            st.success(msg)

    elif action == "Withdraw":
        st.markdown('<p class="subheader">Withdraw Amount</p>', unsafe_allow_html=True)
        withdraw_amount = st.number_input("Enter amount to withdraw", min_value=1, step=1, key="withdraw_amount")
        if st.button("Withdraw", key="withdraw_button"):
            msg = account.withdraw(withdraw_amount)
            if "Insufficient" in msg:
                st.markdown('<p class="error">{}</p>'.format(msg), unsafe_allow_html=True)
            else:
                st.success(msg)

    elif action == "Check Balance":
        st.markdown('<p class="subheader">Check Your Balance</p>', unsafe_allow_html=True)
        st.info(account.check_balance())

    st.markdown("---")
    if st.button("❌ Logout", key="logout_button"):
        st.session_state.clear()
        st.rerun()
