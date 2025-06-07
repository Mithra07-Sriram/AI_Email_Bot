from scripts.query_handler import get_answer
from scripts.email_sender import send_email

# Hardcoded sender credentials
FROM_EMAIL = "mithrasriram07@gmail.com"
APP_PASSWORD = "lwdvwbozzqtfylth"

def main():
    print("\nWelcome to AI Document Query and Email Bot!")
    while True:
        print("\n🤖 Ask a question about your documents (type 'exit' to quit)\n")
        query = input("Ask: ")
        if query.lower() == "exit":
            print("Exiting. Goodbye!")
            break

        answers = get_answer(query, top_k=1)

        if not answers:
            print("❌ No answers found for your query.")
            continue

        print("\nAnswer:\n", answers[0])

        send_option = input("\n📧 Do you want to send this answer to your email? (yes/no): ").strip().lower()
        if send_option == "yes":
            to_email = input("Recipient Email: ").strip()
            subject = "Your AI Answer"
            body = answers[0]
            send_email(subject, body, to_email, FROM_EMAIL, APP_PASSWORD)

if __name__ == "__main__":
    main()