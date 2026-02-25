from fpdf import FPDF
import os

# Make sure folder exists
os.makedirs("data/docs", exist_ok=True)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

text = """
This is a test PDF document for our RAG system.
It contains information about AI, machine learning, and embeddings.

- AI is the field of building intelligent systems.
- Machine Learning is a subset of AI.
- Embeddings are numerical representations of text used for semantic search.
"""

pdf.multi_cell(0, 10, text)
pdf.output("data/docs/test.pdf")

print("Test PDF created at data/docs/test.pdf")