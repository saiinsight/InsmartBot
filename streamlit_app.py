import streamlit as st

# Define a function to generate a response based on user input (dummy implementation)
def generate_response(user_input):
    # Dummy function for generating a response
    # You can replace this with actual logic to process user input
    # and generate meaningful responses
    return f"Processing: {user_input}"

# Main function to run the Streamlit app
def main():
    st.markdown("<h1 style='text-align: center;'>Insmart Chatbot</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("")  # Adding an empty line
    st.markdown("Welcome to Insmart Chatbot! How can I help you today?")
    st.markdown("")  # Adding an empty line

    # Initialize conversation history list
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

    # User input field
    user_input = st.text_input("You:", key="user_input")

    # Button to send user input
    if st.button("Send"):
        if user_input.strip():  # Check if input is not empty
            # Generate and store response
            response = generate_response(user_input)
            
            # Append user input and response to conversation history
            st.session_state.conversation_history.append((user_input, response))

    # Display conversation history
    st.markdown("---")
    st.markdown("")  # Adding an empty line
    for user_message, bot_message in st.session_state.conversation_history:
        st.markdown(f"<div style='text-align: right;'><strong>Me:</strong> {user_message}</div>", unsafe_allow_html=True)
        st.markdown("")
        st.markdown(f"<div style='text-align: left;'><strong>Insmart:</strong> {bot_message}</div>", unsafe_allow_html=True)
        st.markdown("")

    # Clear button to reset conversation
    if st.button("Clear History"):
        st.session_state.conversation_history.clear()

if __name__ == "__main__":
    main()
