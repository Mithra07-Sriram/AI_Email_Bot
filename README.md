# AI Document Query and Email Bot

This project is an AI-powered bot that lets users ask questions about PDF documents (such as user guides or manuals) and receive relevant answers by email. It uses modern NLP (transformers) and vector search (FAISS) for semantic search, and provides both a command-line and a Streamlit web UI.

---

## Features

- Extracts and chunks text from PDF documents.
- Embeds document chunks using Sentence Transformers.
- Fast semantic search using FAISS.
- Users can ask questions and get the most relevant answer.
- Answers can be sent to any email address.
- Streamlit web UI for interactive use.

---

## Folder Structure

```
ai_email_bot/
│
├── app.py                # Streamlit web UI
├── main.py               # Command-line interface
├── requirements.txt      # Python dependencies
│
├── scripts/
│   ├── extract_text.py
│   ├── embed_store.py
│   ├── query_handler.py
│   └── email_sender.py
│
├── docs/                 # Place your PDF files here
│
├── embeddings/           # Generated embeddings and index
│
└── ...
```

---

## Setup

1. **Clone the repository and navigate to the folder:**

    ```sh
    git clone <your-repo-url>
    cd ai_email_bot
    ```

2. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Add your PDF files to the `docs/` folder.**

4. **Build the embeddings and index:**

    ```sh
    python scripts/embed_store.py
    ```

---

## Usage

### Command-Line Interface

1. **Set your sender Gmail and app password in `main.py`:**

    ```python
    FROM_EMAIL = "your_gmail@gmail.com"
    APP_PASSWORD = "your_app_password"
    ```

2. **Run the CLI:**

    ```sh
    python main.py
    ```

3. **Ask questions and send answers to any recipient email.**

---

### Streamlit Web UI

1. **Set your sender Gmail and app password in `app.py`:**

    ```python
    FROM_EMAIL = "your_gmail@gmail.com"
    APP_PASSWORD = "your_app_password"
    ```

2. **Run the app:**

    ```sh
    streamlit run app.py
    ```

3. **Open [http://localhost:8501](http://localhost:8501) in your browser.**
4. **Users log in with their email (for receiving answers), ask questions, and answers are automatically sent to their email.**

---

## Gmail App Password

- You must use a [Gmail App Password](https://support.google.com/accounts/answer/185833) (not your regular Gmail password).
- Enable 2-Step Verification on your Google account to create an app password.

---

## Dependencies

- PyPDF2
- sentence-transformers
- faiss-cpu
- numpy
- streamlit (for web UI)

---

## Notes

- Re-run `python scripts/embed_store.py` whenever you add or update PDFs in the `docs/` folder.
- For production, consider securing credentials and using OAuth for Gmail.

---

## License

MIT License

---

## Credits

- [Sentence Transformers](https://www.sbert.net/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Streamlit](https://streamlit.io/)