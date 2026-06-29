def search_text(text, query):
    paragraphs = text.split("\n\n")

    query = query.lower()

    results = []

    for paragraph in paragraphs:
        if query in paragraph.lower():
            results.append(paragraph.strip())

    if not results:
        return "No relevant information found."

    output = ""

    for index, result in enumerate(results, start=1):
        output += f"\n========== Result {index} ==========\n"
        output += result
        output += "\n"

    return output