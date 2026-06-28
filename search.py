def search_text(text, query):
    paragraphs = text.split("\n\n")

    query = query.lower()

    for paragraph in paragraphs:
        if query in paragraph.lower():
            return paragraph

    return "No relevant information found."