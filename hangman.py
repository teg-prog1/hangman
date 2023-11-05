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

        # Kontrollera om alla bokstäver i ordet har gissats
        has_won = True
        for word_letter in word:
            # Varje bokstav måste kollas, om nån inte gissats är vi inte klara
            if word_letter not in guessed_correct:
                has_won = False
                break

        # Skriv ut ett grattismeddelande vid vinst
        if has_won:
            print("Snyggt jobbat! Du klarade att gissa ordet!")
            # Avsluta programmet
            break

    else:
        guessed_wrong.append(letter)
        print("Tyvärr! Den bokstaven ingår inte i ordet.")
    

