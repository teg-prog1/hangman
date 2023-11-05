# Skapa ett exempelord
word = "programmering"

# Skapa listor för redan gissade bokstäver
guessed_correct = []
guessed_wrong = []

# Fortsätt tills vi bryter på annat sätt
while True:
    while True:
        # Be användaren om en bokstav
        letter = input("Gissa på en bokstav: ").lower()
        # Kontroller att gissningen är exakt en bokstav
        if len(letter)==1 and letter.isalpha():
            break
        else:
            print("Felaktig inmatning, försök igen.")

    # Kontrollera först så att det inte är en gammal gissning
    if letter in guessed_correct or letter in guessed_wrong:
        print("Den bokstaven har du redan gissat på.")
    elif letter in word:
        guessed_correct.append(letter)
        print("Bra jobbat! Bokstaven ingår i ordet.")
    else:
        guessed_wrong.append(letter)
        print("Tyvärr! Den bokstaven ingår inte i ordet.")
    

