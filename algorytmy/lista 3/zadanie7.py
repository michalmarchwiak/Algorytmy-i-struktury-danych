import re

class Empty(Exception):
    pass

class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

def check_html_syntax(html):
    stack = Stack()

    # Regex do znajdowania znaczników HTML
    tags = re.findall(r'<(/?[\w]+)>', html)
    print(tags)
    for tag in tags:
        if not tag.startswith('/'):  # Jeśli jest to znacznik otwierający
            stack.push(tag)
        else:  # Jeśli jest to znacznik zamykający
            if stack.is_empty():
                return f"Błąd: Znacznik zamykający {tag} nie ma pasującego otwierającego."
            top_tag = stack.pop()
            if top_tag != tag[1:]:  # Usuwamy '/' z zamykającego i porównujemy
                return f"Błąd: Znacznik zamykający {tag} nie pasuje do {top_tag}."

    # Sprawdzanie, czy zostały niezamknięte znaczniki
    if not stack.is_empty():
        unclosed_tags = []
        while not stack.is_empty():
            unclosed_tags.append(stack.pop())
        return f"Błąd: Niezamknięte znaczniki: {', '.join(unclosed_tags)}."

    return "Dokument HTML jest poprawny."

# Przykład użycia
html_document = """
<html>
    <body>
        <h1>Witaj, świecie!</h1>
        <p>To jest testowy dokument HTML.
        </p>
        <div>
            <span>Przykładowy tekst.</span>
        </div>
    </body>
</html>
"""

result = check_html_syntax(html_document)
print(result)