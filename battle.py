import streamlit as st

# --- Coffee Machine Class ---
class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,  # in ml
            "milk": 200,  # in ml
            "coffee_beans": 100,  # in grams
            "money": 0,  # in dollars
        }
        self.menu = {
            "Espresso": {"water": 50, "milk": 0, "coffee_beans": 18, "cost": 1.5},
            "Latte": {"water": 200, "milk": 150, "coffee_beans": 24, "cost": 2.5},
            "Cappuccino": {"water": 250, "milk": 100, "coffee_beans": 24, "cost": 3.0},
        }

    def is_resource_sufficient(self, coffee_type):
        """Check if the machine has enough resources to make the selected coffee"""
        coffee = self.menu[coffee_type]
        for resource, amount in coffee.items():
            if resource != "cost" and self.resources[resource] < amount:
                return False
        return True

    def make_coffee(self, coffee_type):
        """Make the selected coffee and deduct resources"""
        if self.is_resource_sufficient(coffee_type):
            coffee = self.menu[coffee_type]
            for resource, amount in coffee.items():
                if resource != "cost":
                    self.resources[resource] -= amount
            self.resources["money"] += coffee["cost"]
            return f"Here is your {coffee_type} ☕. Enjoy!"
        else:
            return "Sorry, not enough resources!"

    def add_resources(self, resource, amount):
        """Admin can add resources to the machine"""
        if resource in self.resources:
            self.resources[resource] += amount
            return f"{amount} ml of {resource} added successfully!"
        else:
            return "Invalid resource!"

    def get_status(self):
        """Display the current status of resources"""
        status = f"Water: {self.resources['water']} ml\n"
        status += f"Milk: {self.resources['milk']} ml\n"
        status += f"Coffee Beans: {self.resources['coffee_beans']} g\n"
        status += f"Money: ${self.resources['money']}\n"
        return status

# --- Streamlit Interface ---
def main():
    st.title("Coffee Machine")
    coffee_machine = CoffeeMachine()

    st.sidebar.title("Menu")
    coffee_choice = st.sidebar.radio("Choose your coffee", ["Espresso", "Latte", "Cappuccino"])
    action = st.sidebar.radio("What would you like to do?", ["Make Coffee", "Check Status", "Add Resources"])

    # --- Coffee Buttons ---
    if action == "Make Coffee":
        if st.button("Make Espresso"):
            message = coffee_machine.make_coffee("Espresso")
            st.write(message)
            st.image("https://www.thecoffeebean.com/sites/default/files/styles/large/public/2020-11/Espresso.jpg?itok=HtPBVJHh", width=300)
        
        if st.button("Make Latte"):
            message = coffee_machine.make_coffee("Latte")
            st.write(message)
            st.image("https://www.thecoffeebean.com/sites/default/files/styles/large/public/2020-11/Latte.jpg?itok=9TbT3mti", width=300)
        
        if st.button("Make Cappuccino"):
            message = coffee_machine.make_coffee("Cappuccino")
            st.write(message)
            st.image("https://www.thecoffeebean.com/sites/default/files/styles/large/public/2020-11/Cappuccino.jpg?itok=ecV8YFcN", width=300)

    elif action == "Check Status":
        st.subheader("Current Resources")
        status = coffee_machine.get_status()
        st.text(status)

    elif action == "Add Resources":
        resource = st.selectbox("Choose resource to add", ["water", "milk", "coffee_beans"])
        amount = st.number_input(f"Enter amount of {resource} to add", min_value=1, step=1)
        if st.button(f"Add {amount} ml of {resource}"):
            message = coffee_machine.add_resources(resource, amount)
            st.write(message)

if __name__ == "__main__":
    main()
