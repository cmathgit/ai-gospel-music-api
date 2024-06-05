import json
import random

# Load data from JSON files
with open('lib/tempo_dict.json') as f:
    tempos = json.load(f)

with open('lib/music_key_dict.json') as f:
    musical_keys = json.load(f)

with open('lib/bible_book_dict.json') as f:
    bible_chapters = json.load(f)

with open('lib/instrument_dict.json') as f:
    instruments = json.load(f)

with open('lib/vocalists_dict.json') as f:
    vocalists = json.load(f)

with open('lib/song_genre_dict.json') as f:
    song_genre = json.load(f)

# Function to generate a random combination string
'''
def generate_combination():
    combination = ""
    while len(combination) < 200:
        song_genre_choice = random.choice(song_genre)
        vocalist_choice = random.choice(vocalists)
        instrument_choice = random.choice(instruments)
        bible_choice = random.choice(bible_chapters)
        tempo_choice = random.choice(tempos)
        musical_key_choice = random.choice(musical_keys)
        
        combination += f'("{song_genre_choice[0]}", {vocalist_choice[0]} ({vocalist_choice[2]}), {instrument_choice}, bible lyrics {bible_choice[0]} {random.randint(1, bible_choice[1])}, {tempo_choice[0]} {random.randint(tempo_choice[1], tempo_choice[2])}, {musical_key_choice[0]}), '
    
    return combination[:-2]  # Remove the trailing comma and space
    
'''

def generate_combination():
    combination = ""
    while True:
        song_genre_choice = random.choice(song_genre)
        vocalist_choice = random.choice(vocalists)
        instrument_choice = random.choice(instruments)
        bible_choice = random.choice(bible_chapters)
        tempo_choice = random.choice(tempos)
        musical_key_choice = random.choice(musical_keys)
        
        combination = f'"{song_genre_choice[0]}, {vocalist_choice[0]} ({vocalist_choice[2]}), {instrument_choice}, biblical lyrics {bible_choice[0]} {random.randint(1, bible_choice[1])}, {tempo_choice[0]} {random.randint(tempo_choice[1], tempo_choice[2])}, {musical_key_choice[0]}"'
        
        if len(combination) < 200:
            break
    
    return combination

# Generate and print the combination string
print(generate_combination())
    
    
