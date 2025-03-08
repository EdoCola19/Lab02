import translator as tr
from dictionary import Dictionary

t = tr.Translator("dictionary.txt")


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input("Inserisci qui il comando: ")
    dic = Dictionary("dictionary.txt")

    # Add input control here!

    if int(txtIn) == 1:

        txtIn2 = input("Inserisci la parola da aggiungere in lingua aliena e separa con uno spazio la traduzione italiana: ")
        parti = txtIn2.split(" ")
        parolaAliena = parti[0]
        traduzione = [parte for parte in parti[1]]
        dictionar = t.loadDictionary("dictionary.txt")

        if parolaAliena not in dictionar:
            dic.addWord("dictionary.txt", txtIn2)
        else:
            t.handleAdd(txtIn2)



    if int(txtIn) == 2:
        txtIn2 = input("Inserisci la parola da cercare: ")
        dic.translate(t.loadDictionary("dictionary.txt"), txtIn2)


    if int(txtIn) == 3:
        txtIn2 = input("Inserisci la parola da cercare con wildcard(se non conosci una lettera inserisci '?': ")
        dic.translateWordWildCard(t.loadDictionary("dictionary.txt"), txtIn2)
    if int(txtIn) == 4:
        print("Grazie per aver utilizzato il traduttore!")
        break