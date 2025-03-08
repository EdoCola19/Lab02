import ast

import dictionary as dic
d = dic.Dictionary("dictionary.txt")
class Translator:

    def __init__(self,filename):
        self.filename = filename

    def printMenu(self):
        frasi = ["Aggiungi nuova parola", "Cerca una traduzione", "Cerca con wildcard", "Exit"]
        print("------------------------------------")
        print("      Translator Alien-Italian     ")
        print("------------------------------------")

        for i,frase in enumerate(frasi, start=1):
            print(f"{i}. {frase}")
        print("------------------------------------")
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit


    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        dictionary = {}
        try:
            with open(dict, "r" , encoding="utf-8") as file:
                for line in file:
                    data = line.strip().split(" ", 1)
                    alienWord = data[0]

                    if data[1].startswith("[") and data[1].endswith("]"):
                        clean_data = clean_data = data[1][1:-1]
                        traduzioni = [item.strip() for item in clean_data.split(",")]
                        dictionary[alienWord] = traduzioni
                    else:
                        traduzioni = data[1]
                        dictionary[alienWord] = traduzioni
            return dictionary
        except Exception as e:
            print(f"Il file non esiste o non è raggiungibile, errore: {e}")



    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parti = entry.lower().split(" ")
        if len(parti) <2:
            return "Errore nel formato"
        parolaAliena = parti[0]
        traduzioni = parti[1:]
        filename = "dictionary.txt"
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
        update = []
        new_lines = []
        for line in lines:
            parts = line.strip().split(" ")
            if parts[0] == parolaAliena:
                traduzioni_esistenti = [parts[1]]
                traduzioni_esistenti.extend(traduzioni)
                update.append((parts[0], traduzioni_esistenti))
            else:
                new_lines.append(line)

        with open(filename, "w")as f:
            for line in new_lines:
                f.write(line)

        if update:
            try:
                with open(filename, "a") as file:
                    for up in update:
                       parola, traduzioni = up
                       file.write(f"{parola} [{', '.join(traduzioni)}]\n")
                print("Parole aggiunte con successo!")
            except Exception as e:
                print(f"Errore: {e}")



    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass