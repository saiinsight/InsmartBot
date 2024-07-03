import streamlit as st

# Define a function to generate a report based on user input (dummy implementation)
def generate_report(user_input):
    # Dummy reports for sample purposes
    sample_reports = {
        "sales": "Sales report for Q2 2023: $100,000",
        "inventory": "Inventory report: 50 units in stock",
        # Add more sample reports as needed
    }

    # Check if the user input matches a report
    if user_input.lower() in sample_reports:
        return sample_reports[user_input.lower()]
    else:
        return "Report not found"

# Main function to run the Streamlit app
def main():
    st.markdown("<h1 style='text-align: center;'>Insmart Chatbot</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("")  # Adding an empty line
    st.markdown("Welcome to Insmart Chatbot! How can I help you today?")
    st.markdown("")  # Adding an empty line

    # User input field
    user_input = st.text_input("You:", key="user_input")

    # Button to generate report
    if st.button("Send"):
        if user_input.strip():  # Check if input is not empty
            # Generate and display report
            report = generate_report(user_input)
            st.markdown("---")
            st.markdown("")
            st.markdown(f"<div style='text-align: right;'><strong>Me:</strong> {user_input}</div>", unsafe_allow_html=True)
            st.markdown("")
            st.markdown(f"<div style='text-align: left;'><strong>Insmart:</strong> {report}</div>", unsafe_allow_html=True)
            st.markdown("")
        else:
            st.warning("Please enter a command.")

    # Clear button to reset details
    if st.button("Clear"):
        st.text_area("Conversation Window:", value="", key="clear")

if __name__ == "__main__":
    main()
