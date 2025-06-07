import streamlit as st
from scripts.query_handler import get_answer
from scripts.email_sender import send_email

st.set_page_config(page_title="AI Document Query and Email Bot")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("📄 AI Document Query and Email Bot")

if not st.session_state.logged_in:
    st.header("Login")
    email = st.text_input("Your Gmail Address")
    password = st.text_input("Your Gmail App Password", type="password")
    if st.button("Login"):
        # Simple check (you can add real validation if needed)
        if email and password:
            st.session_state.logged_in = True
            st.session_state.email = email
            st.session_state.password = password
            st.success("Logged in successfully!")
        else:
            st.error("Please enter both email and password.")
else:
    st.header("Ask a Question")
    query = st.text_input("Type your question about your documents:")
    if st.button("Get Answer"):
        if query.strip():
            answers = get_answer(query, top_k=1)
            if answers:
                st.success("Answer sent to your email!")
                # Automatically send answer to user's email
                send_email(
                    subject="Your AI Document Answer",
                    body=answers[0],
                    to_email=st.session_state.email,
                    from_email=st.session_state.email,
                    password=st.session_state.password
                )
                st.write("**Answer:**")
                st.write(answers[0])
            else:
                st.warning("No relevant answers found for your query.")
        else:
            st.warning("Please enter a question.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()