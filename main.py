from pdf_reader import extract_text
from search import search_text


def main():
    pdf_path = "thesis.pdf"

    text = extract_text(pdf_path)

    question = input("Ask a question: ")

    answer = search_text(text, question)

    print("\nAnswer:")
    print(answer)


if __name__ == "__main__":
    main()