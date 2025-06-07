import streamlit as st
from scripts.query_handler import get_answer
from scripts.email_sender import send_email

# Owner's sender credentials (hardcoded)
FROM_EMAIL = ""
APP_PASSWORD = ""

st.set_page_config(page_title="AI Document Query and Email Bot")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("📄 AI Document Query and Email Bot")

if not st.session_state.logged_in:
    st.header("Login")
    email = st.text_input("Your Email Address (to receive answers)")
    if st.button("Login"):
        if email:
            st.session_state.logged_in = True
            st.session_state.email = email
            st.success("Logged in successfully!")
        else:
            st.error("Please enter your email address.")
else:
    st.header("Ask a Question")
    query = st.text_input("Type your question about your documents:")
    if st.button("Get Answer"):
        if query.strip():
            answers = get_answer(query, top_k=1)
            if answers:
                send_email(
                    subject="Your AI Document Answer",
                    body=answers[0],
                    to_email=st.session_state.email,
                    from_email=FROM_EMAIL,
                    password=APP_PASSWORD
                )
                st.success("Answer sent to your email!")
                st.write("**Answer:**")
                st.write(answers[0])
            else:
                st.warning("No relevant answers found for your query.")
        else:
            st.warning("Please enter a question.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()