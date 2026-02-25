# main.py
from src.loader import load_pdf
from src.chunker import chunk_text
from src.embedder import create_index, save_index
from src.search import search
from src.query_llm import query_llm
import re
from datetime import datetime
import os

# Directory to save logs
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def build_index(pdf_path):
    """
    Load a PDF, split into chunks, create FAISS index, and save it.
    """
    text = load_pdf(pdf_path)
    chunks = chunk_text(text)
    index, _ = create_index(chunks)
    save_index(index, chunks)
    print("Index built successfully!")

def ask_question_session(pdf_name):
    """
    Allow multiple questions in a session, save answers to a text file.
    """
    log_file = os.path.join(LOG_DIR, f"{pdf_name}_answers.txt")
    print("\nYou can now ask multiple questions. Type 'exit' to quit.\n")

    while True:
        question = input("Enter your question: ").strip()
        if question.lower() in ["exit", "quit"]:
            print("Ending session.")
            break

        top_chunks = search(question)
        raw_answer = query_llm(top_chunks, question)

        # Extract text if SDK returned dict
        if isinstance(raw_answer, dict):
            answer_text = raw_answer.get("answer", "")
        else:
            answer_text = raw_answer

        # Clean output
        answer_text = re.sub(r"\[conversation_history:\d+\]", "", answer_text)
        answer_text = re.sub(r"\[web:\d+\]", "", answer_text)
        answer_text = "\n".join([line.strip() for line in answer_text.splitlines() if line.strip()])

        # Format output
        formatted_answer = f"\n===== Question =====\n{question}\n\n===== Answer =====\n{answer_text}\n====================\n"
        print(formatted_answer)

        # Append to log file
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}]{formatted_answer}\n")

    print(f"All answers saved to: {log_file}")

if __name__ == "__main__":
    mode = input("Type 'build' to index a PDF or 'ask' to query: ").strip().lower()

    if mode == "build":
        path = input("Enter PDF path (e.g., data/docs/test.pdf): ").strip()
        build_index(path)
        pdf_name = os.path.splitext(os.path.basename(path))[0]

        # Ask questions right after building
        ask_question_session(pdf_name)

    elif mode == "ask":
        pdf_name = input("Enter PDF name (without extension, used for logs): ").strip()
        ask_question_session(pdf_name)

    else:
        print("Invalid option. Type 'build' or 'ask'.")