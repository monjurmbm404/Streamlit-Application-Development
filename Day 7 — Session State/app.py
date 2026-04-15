import streamlit as st

st.set_page_config(page_title="Session State App", layout="centered")

st.title("📝 To-Do List App (Session State)")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input
new_task = st.text_input("Enter a new task:")

# Add task
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success("Task added!")

# Show tasks
st.subheader("📌 Your Tasks")

if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(f"{i+1}. {task}")

        with col2:
            if st.button("❌", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.experimental_rerun()
else:
    st.info("No tasks yet. Add one!")

# Clear all tasks
if st.button("Clear All"):
    st.session_state.tasks = []
    st.warning("All tasks cleared!")