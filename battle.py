import streamlit as st
import random
import datetime

# Class to manage tasks
class Task:
    def __init__(self, task_name, due_date):
        self.task_name = task_name
        self.due_date = due_date

    def display_task(self):
        return f"Task: {self.task_name} | Due Date: {self.due_date}"

# Class to manage reminders
class Reminder:
    def __init__(self, reminder_text, reminder_time):
        self.reminder_text = reminder_text
        self.reminder_time = reminder_time

    def display_reminder(self):
        return f"Reminder: {self.reminder_text} | Time: {self.reminder_time}"

# Class to get the weather
class Weather:
    def __init__(self, location):
        self.location = location

    def get_weather(self):
        # Simulate a simple weather fetch (could be extended with actual API calls)
        weather_conditions = ["Sunny", "Cloudy", "Rainy", "Windy"]
        temperature = random.randint(15, 30)  # Random temperature
        condition = random.choice(weather_conditions)
        return f"The weather in {self.location} is {condition} with a temperature of {temperature}°C."

# Class to manage personal calendar
class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, event_name, event_date):
        event = {"event": event_name, "date": event_date}
        self.events.append(event)

    def display_events(self):
        if self.events:
            return "\n".join([f"Event: {event['event']} on {event['date']}" for event in self.events])
        else:
            return "No events scheduled."

# Parent class for conversations
class PersonalAssistantBot:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.reminders = []
        self.calendar = Calendar()

    def greet(self):
        return f"Hello! I'm {self.name}, your personal assistant. How can I help you today?"

    def set_task(self, task_name, due_date):
        task = Task(task_name, due_date)
        self.tasks.append(task)
        return f"Task '{task_name}' has been set for {due_date}."

    def set_reminder(self, reminder_text, reminder_time):
        reminder = Reminder(reminder_text, reminder_time)
        self.reminders.append(reminder)
        return f"Reminder set: {reminder_text} at {reminder_time}."

    def ask_weather(self, location):
        weather = Weather(location)
        return weather.get_weather()

    def add_event(self, event_name, event_date):
        self.calendar.add_event(event_name, event_date)
        return f"Event '{event_name}' added to calendar on {event_date}."

    def display_tasks(self):
        if self.tasks:
            return "\n".join([task.display_task() for task in self.tasks])
        else:
            return "No tasks found."

    def display_reminders(self):
        if self.reminders:
            return "\n".join([reminder.display_reminder() for reminder in self.reminders])
        else:
            return "No reminders found."

    def display_calendar(self):
        return self.calendar.display_events()

# Streamlit App Layout
st.title("Personal Assistant Bot")

# Create bot instance
bot = PersonalAssistantBot(name="Buddy")

# Greet the user
st.subheader(bot.greet())

# User input fields
task_name = st.text_input("Enter task name:")
due_date = st.date_input("Enter due date for task:")
reminder_text = st.text_input("Enter reminder text:")
reminder_time = st.time_input("Enter reminder time:")
location = st.text_input("Enter location for weather:")
event_name = st.text_input("Enter event name:")
event_date = st.date_input("Enter event date for calendar:")

# Button for setting task
if st.button("Set Task"):
    if task_name and due_date:
        response = bot.set_task(task_name, str(due_date))
        st.success(response)
    else:
        st.error("Please enter both task name and due date.")

# Button for setting reminder
if st.button("Set Reminder"):
    if reminder_text and reminder_time:
        response = bot.set_reminder(reminder_text, str(reminder_time))
        st.success(response)
    else:
        st.error("Please enter both reminder text and reminder time.")

# Button for asking weather
if st.button("Get Weather"):
    if location:
        response = bot.ask_weather(location)
        st.success(response)
    else:
        st.error("Please enter a location.")

# Button for adding event to calendar
if st.button("Add Event"):
    if event_name and event_date:
        response = bot.add_event(event_name, str(event_date))
        st.success(response)
    else:
        st.error("Please enter both event name and event date.")

# Displaying tasks
if st.button("Display Tasks"):
    tasks = bot.display_tasks()
    st.text_area("Your Tasks:", tasks)

# Displaying reminders
if st.button("Display Reminders"):
    reminders = bot.display_reminders()
    st.text_area("Your Reminders:", reminders)

# Displaying calendar
if st.button("Display Calendar"):
    calendar = bot.display_calendar()
    st.text_area("Your Events:", calendar)
