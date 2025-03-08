import re
class Dictionary:
    def __init__(self, filename):
        self.filename = filename



    def addWord(self, file, parole):
        try:
            with open(file, "a", encoding="utf-8") as f:
                f.write(f"\n{parole}")
            print("Parole aggiunte con successo!")
        except Exception:
            print("Impossibile scrivere sul file")


    def translate(self, my_dict, word1):
        if word1 in my_dict.keys():
            traduzioni = my_dict[word1]

            if isinstance(traduzioni, list):
                print(f"{', '.join(traduzioni)}")
            else:
                print(traduzioni)
        else:
            return f"La parola Aliena {word1} non esiste sul database, prova ad aggiungerla!"



    def translateWordWildCard(self, dictionary, word):
        word = word.lower()
        regex_word = word.replace("?", ".")
        results = []
        for key in dictionary.keys():
            if re.search(regex_word, key):
                results.append(dictionary[key])
        if results:
                    print(", ".join(results))  # Stampa tutte le traduzioni trovate
        else:
                    print("Nessuna corrispondenza trovata.")






