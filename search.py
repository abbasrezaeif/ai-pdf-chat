def search_text(text, query):
    lines = text.split("\n")

    query = query.lower()

    for i, line in enumerate(lines):
        if query in line.lower():

            start = max(0, i - 3)
            end = min(len(lines), i + 4)

            context = "\n".join(lines[start:end])

            return context

    return "No relevant information found."