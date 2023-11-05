import random
# I den egna filen graphics ligger textgrafiken för den hängda gubben
from graphics import hanging_man

def hide_letters(word, guesses):
    """Returnerar en sträng där alla bokstäver som inte gissats är dolda."""
    new_word = ""
    # Bygg upp ordet bokstav för bokstav
    for letter in word:
        if letter in guesses:
            new_word += " " + letter.upper() + " "
        else:
            new_word += " _ "
    return new_word

# Skapa en ordlista
wordlist = [
    "programmering", "tangentbord", "dator",
    "studentmössa", "jultomte", "lektion",
    "matsedel", "mopedbil", "körkort",
    "gymnasium" ]

# Slumpa fram ett ord
word = random.choice(wordlist)

# Skapa listor för redan gissade bokstäver
guessed_correct = []
guessed_wrong = []
max_guesses = 10

# Skriv ut ett välkomstmeddelande
print("Välkommen till spelet Hänga Gubbe")

# Fortsätt tills vi bryter på annat sätt
while True:
    # Rita den hängande gubben
    print(hanging_man[len(guessed_wrong)])
    # Skriv ut ordet med okända bokstäver dolda
    print(f"      {hide_letters(word, guessed_correct)}")
    print()
    # Skriv ut felaktiga gissningar
    if len(guessed_wrong)>0:
        # join lägger ihop alla element i en lista till en sträng
        print(f" Fel: {' '.join(guessed_wrong).upper()}")
        print()

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

        # Kontrollera om max antalet gissningar har överskridits
        # dvs gubben är hängd
        # Eftersom hanging_man har ett element som motsvarar
        # inga gissningar måste vi lägga till ett
        if len(guessed_wrong)+1==len(hanging_man):
            print("Tyvärr! Du klarade det inte. Du blev hängd!")
            print(hanging_man[len(guessed_wrong)])
            # Avsluta programmet
            break
    