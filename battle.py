import streamlit as st

# --- In-Memory Account Storage ---
if "accounts" not in st.session_state:
    st.session_state.accounts = {}

# --- BankAccount OOP Class ---
class BankAccount:
    def __init__(self, name, username, password, balance=0):
        self.name = name
        self.username = username
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"✅ ₹{amount} deposited successfully. New balance: ₹{self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"✅ ₹{amount} withdrawn successfully. New balance: ₹{self.balance}"
        else:
            return "❌ Insufficient balance!"

    def check_balance(self):
        return f"💰 Current Balance: ₹{self.balance}"


# --- Streamlit Setup ---
st.set_page_config(page_title="🏦 MyBank App", layout="centered")
st.markdown("<h1 style='text-align: center;'>🏦 MyBank - Digital Banking</h1>", unsafe_allow_html=True)
st.markdown("---")

# Session states
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# --- Step 1: Create Account ---
with st.expander("📝 Create Account"):
    name = st.text_input("Full Name", key="create_name")
    username = st.text_input("Username", key="create_user")
    password = st.text_input("Password", type="password", key="create_pass")
    if st.button("Create Account"):
        if username in st.session_state.accounts:
            st.warning("⚠️ Username already exists.")
        elif not username or not password or not name:
            st.warning("⚠️ All fields are required.")
        else:
            account = BankAccount(name, username, password)
            st.session_state.accounts[username] = account
            st.success("✅ Account created successfully! You can now log in.")


# --- Step 2: Login Form ---
if not st.session_state.logged_in:
    with st.expander("🔐 Login to Your Account", expanded=True):
        login_user = st.text_input("Username", key="login_user")
        login_pass = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):
            accounts = st.session_state.accounts
            if login_user in accounts and accounts[login_user].password == login_pass:
                st.session_state.logged_in = True
                st.session_state.active_user = login_user
                st.success(f"✅ Logged in as {login_user}")
                st.experimental_rerun()
            else:
                st.error("❌ Invalid username or password.")


# --- Step 3: Banking Dashboard ---
if st.session_state.logged_in:
    acc = st.session_state.accounts[st.session_state.active_user]
    st.markdown(f"### 👋 Welcome, **{acc.name}** (`@{acc.username}`)")
    st.markdown("#### 💼 What would you like to do today?")
    option = st.radio("", ["💰 Deposit", "💸 Withdraw", "📊 Check Balance"], horizontal=True)

    if option == "💰 Deposit":
        amount = st.number_input("Enter deposit amount", min_value=1, step=1, key="deposit_amt")
        if st.button("Deposit"):
            st.success(acc.deposit(amount))

    elif option == "💸 Withdraw":
        amount = st.number_input("Enter withdrawal amount", min_value=1, step=1, key="withdraw_amt")
        if st.button("Withdraw"):
            msg = acc.withdraw(amount)
            if "Insufficient" in msg:
                st.error(msg)
            else:
                st.success(msg)

    elif option == "📊 Check Balance":
        st.info(acc.check_balance())

    st.markdown("---")
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.active_user = None
        st.experimental_rerun()
