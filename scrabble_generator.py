def word_combo(word,letter,sana):
    for i in range(len(sana)):
        if sana[i] != word[i] and word[i]!= "_":
            return False
        elif word[i] == "_":
            if sana[i] in letter:
                letter.remove(sana[i])
            elif "/" in letter:
                letter.remove("/")
            else:
                return False

    return True
def print_words(end):
    if len(end) == 0:
        print("There were no matches :(")
    else:
        print(f"There were {len(end)} matches.")
def main():
    words = []
    length = []
    end = []
    ammount = 0
    name = input("Enter the name of the file.\n")
    try:
        file = open(name, "r")
        print("Welcome to the scrabble generator!")
        word = input("Enter the word with all the known letters (eg. 's___nt'):\n")

        tiles = input("Enter your game tiles (eg. '/,c,r,a,b,b,l,e').\n")
        rivi = tiles.split(",")
        words.append(rivi)

        for i in file:
            i = i.rstrip()
            if len(word) == len(i):
                length.append(i)
        print()
        for sana in length:
            rivi = tiles.split(",")
            if word_combo(word, rivi, sana):
                end.append(sana)
                print(sana)



        print_words(end)

    except OSError:
        print(f"Error in reading the file {name}\n")








main()