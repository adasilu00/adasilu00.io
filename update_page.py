def update_text(new_text):
    # Leggi il file index.html
    with open('index.html', 'r', encoding='utf-8') as file:
        content = file.read()

    # Trova la parte del testo dinamico e la sostituisci
    start = content.find('<h1 id="dynamic-text">') + len('<h1 id="dynamic-text">')
    end = content.find('</h1>', start)
    new_content = content[:start] + new_text + content[end:]

    # Scrivi il nuovo contenuto nel file index.html
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(new_content)

# Esempio di uso
new_text = input("Inserisci il nuovo testo: ")
update_text(new_text)
