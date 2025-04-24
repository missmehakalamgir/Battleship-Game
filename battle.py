import streamlit as st

# Initialize app and register users
app = ChatApp()

# Streamlit UI
st.title("Chat Application")
st.header("Login to Chat")

# Register or Login User
username = st.text_input("Username:")
email = st.text_input("Email:")
if st.button("Register"):
    user = app.register_user(username, email)

# Show user contacts and send messages
if username:
    st.subheader(f"Hello, {username}!")
    contact_username = st.text_input("Enter Contact Username:")
    message_content = st.text_area("Message Content")
    
    if st.button("Send Private Message"):
        receiver = next((u for u in app.users if u.username == contact_username), None)
        if receiver:
            app.send_private_message(user, receiver, message_content)
        else:
            st.error("Contact not found!")

# Group creation and messaging
group_name = st.text_input("Create Group Name:")
if st.button("Create Group"):
    group = Group(group_name, user)
    st.success(f"Group {group_name} created!")

if st.button("Send Group Message"):
    group_content = st.text_area("Group Message Content")
    app.send_group_message(user, group, group_content)
