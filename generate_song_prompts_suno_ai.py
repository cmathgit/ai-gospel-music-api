import json
import random
import os
import shutil
from datetime import datetime

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
    
with open('lib/bible_song_genre_dict.json') as f:
    bible_song_genre = json.load(f)
    
with open('lib/instrumental_song_genre_dict.json') as f:
    instrumental_song_genre = json.load(f)

def check_and_write_to_file(filename, new_text):
    # Define the maximum file size in bytes (5 KB)
    max_size = 5 * 1024 * 10
    
    # Get the size of the file
    file_size = os.path.getsize(filename)
    
    if file_size < max_size:
        # Append the new text if the file size is less than 5 KB
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(new_text)
    else:
        # Create a backup with a timestamp if the file size is 5 KB or more
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = f"log/prompt_history_{timestamp}.txt"
        
        # Copy the original file to the backup file
        shutil.copy2(filename, backup_filename)
        
        # Overwrite the original file with the new text
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(new_text)
            
        print(f"File size exceeded 5 KB. Prompt history cleared and data written. Created backup: {backup_filename}")

# Example usage
# new_text = "This is the new text to be appended or written."
# check_and_write_to_file('log/History.txt', new_text)

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

# Function to generate a random biblical song prompt less than 200 characters in string length
def generate_biblical_song_simple():
    song_descr_prompt = ""
    while True:
        bible_song_genre_choice = random.choice(bible_song_genre)
        vocalist_choice = random.choice(vocalists)
        instrument_choice_1 = random.choice(instruments)
        instrument_choice_2 = random.choice(instruments)
        bible_book_choice = random.choice(bible_chapters)
        bible_chap_choice = random.randint(1, bible_book_choice[1])
        tempo_choice = random.choice(tempos)
        musical_key_choice = random.choice(musical_keys)
        
        yt_title = f"Song_Title_Here [{bible_book_choice[0]} {bible_chap_choice}] [{bible_song_genre_choice[0]}] [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
        check_and_write_to_file('log/prompt_history.txt', yt_title)
        print(yt_title)
        print("")
        
        yt_descr = f"Using AI to generate biblically accurate {bible_song_genre_choice[0]} songs and music videos.\n\n"
        check_and_write_to_file('log/prompt_history.txt', yt_descr)
        print(yt_descr)
        print("")
        
        song_descr_prompt = f'{bible_song_genre_choice[0]}, {vocalist_choice[0]} ({vocalist_choice[2]}), {instrument_choice_1}, {instrument_choice_2}, biblically inspired lyrics book of {bible_book_choice[0]} chapter {bible_chap_choice}, {tempo_choice[0]} {random.randint(tempo_choice[1], tempo_choice[2])} bpm, {musical_key_choice[0]}'
        
        if len(song_descr_prompt) < 200:
            check_and_write_to_file('log/prompt_history.txt', "Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:\n")
            print("Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:")
            break
    
    return song_descr_prompt
    
# Function to generate a random biblical song prompt less than 200 characters in string length
def generate_biblical_song_custom():
    lyrics_prompt = ""
    style_of_music_prompt = ""
    while True:
        song_genre_choice = random.choice(song_genre)
        vocalist_choice = random.choice(vocalists)
        instrument_choice_1 = random.choice(instruments)
        instrument_choice_2 = random.choice(instruments)
        instrument_choice_3 = random.choice(instruments)
        bible_book_choice = random.choice(bible_chapters)
        bible_chap_choice = random.randint(1, bible_book_choice[1])
        tempo_choice = random.choice(tempos)
        musical_key_choice = random.choice(musical_keys)
        
        yt_title = f"Song_Title_Here [{bible_book_choice[0]} {bible_chap_choice}] [{song_genre_choice[0]}] [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
        check_and_write_to_file('log/prompt_history.txt', yt_title)
        print(yt_title)
        print("")
        
        yt_descr = f"Using AI to generate biblically accurate {song_genre_choice[0]} songs and music videos.\n\n"
        check_and_write_to_file('log/prompt_history.txt', yt_descr)
        print(yt_descr)
        print("")
        
        lyrics_prompt = f'Generate biblically accurate lyrics inspired by the message of the book of {bible_book_choice[0]} chapter {bible_chap_choice} quoting verses taken from the King James Version bible'
        
        style_of_music_prompt = f'{song_genre_choice[0]}, {vocalist_choice[0]} ({vocalist_choice[2]}), {instrument_choice_1}, {instrument_choice_2}, {instrument_choice_3}, {tempo_choice[0]} {random.randint(tempo_choice[1], tempo_choice[2])} bpm, {musical_key_choice[0]}'
        
        if len(style_of_music_prompt) < 120 and len(lyrics_prompt) < 399:
            concat_prompts = f"Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:\n{style_of_music_prompt}\n\nLyrics Prompt:\n{lyrics_prompt}\n"
            #check_and_write_to_file('log/prompt_history.txt', concat_prompts)
            #print(concat_prompts)
            break
    
    return concat_prompts
    
def generate_instrumental_song_simple():
    combination = ""
    while True:
        instrumental_song_genre_choice = random.choice(instrumental_song_genre)
        instrument_choice_1 = random.choice(instruments)
        instrument_choice_2 = random.choice(instruments)
        instrument_choice_3 = random.choice(instruments)
        instrument_choice_4 = random.choice(instruments)
        tempo_choice = random.choice(tempos)
        musical_key_choice = random.choice(musical_keys)
        
        yt_title = f"Song_Title_Here [Instrumental] [{instrumental_song_genre_choice[0]}] [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
        check_and_write_to_file('log/prompt_history.txt', yt_title)
        print(yt_title)
        print("")
        
        yt_descr = f"Using AI to generate {instrumental_song_genre_choice[0]} instrumentals for vocalists from a variety of genres, musical keys, and modes.\n\n"
        check_and_write_to_file('log/prompt_history.txt', yt_descr)
        print(yt_descr)
        print("")
        
        combination = f'{instrumental_song_genre_choice[0]}, {instrument_choice_1}, {instrument_choice_2}, {instrument_choice_3}, {instrument_choice_4}, {tempo_choice[0]} {random.randint(tempo_choice[1], tempo_choice[2])} bpm, {musical_key_choice[0]}'
        
        if len(combination) < 200:
            check_and_write_to_file('log/prompt_history.txt', "Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:\n")
            print("Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:")
            break
    
    return combination
    
new_prompt_div = "\n\n------------------------------New Prompt-------------------------------------\n"

check_and_write_to_file('log/prompt_history.txt', new_prompt_div)
print("\n------------------------------New Prompt-------------------------------------\n")
# Generate and print the generate_biblical_song_simple string
# print("Biblically inspired song prompt less than 200 characters in string length:")
bible_song_prompt = generate_biblical_song_simple()
check_and_write_to_file('log/prompt_history.txt', bible_song_prompt)
print(bible_song_prompt)
check_and_write_to_file('log/prompt_history.txt', "\n\n Lyrics_Here")
print("\n Lyrics_Here")

check_and_write_to_file('log/prompt_history.txt', new_prompt_div)
print("\n------------------------------New Prompt-------------------------------------\n")
# Generate and print the generate_biblical_song_simple string
# print("Biblically inspired song prompt less than 200 characters in string length:")
bible_song_prompt_custom = generate_biblical_song_custom()
check_and_write_to_file('log/prompt_history.txt', bible_song_prompt_custom)
print(bible_song_prompt_custom)
check_and_write_to_file('log/prompt_history.txt', "\n\n Lyrics_Here")
print("\n Lyrics_Here")

check_and_write_to_file('log/prompt_history.txt', new_prompt_div)
print("\n------------------------------New Prompt-------------------------------------\n")
# Generate and print the generate_instrumental_song_simple string
# print("Instrumental song prompt less than 200 characters in string length:")
instrumental_song_prompt = generate_instrumental_song_simple()
check_and_write_to_file('log/prompt_history.txt', instrumental_song_prompt)
print(instrumental_song_prompt)
check_and_write_to_file('log/prompt_history.txt', "\n\n[Instrumental]")
print("\n[Instrumental]")