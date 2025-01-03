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
with open('lib/drum_loop_genres_dict.json') as f:
    drum_loop_genre = json.load(f)

with open('lib/drum_kits_dict.json') as f:
    drum_kits = json.load(f)

with open('lib/percussion_instruments_dict.json') as f:
        percussion_instruments = json.load(f)

with open('lib/anti_percussion_instruments_dict.json') as f:
        anti_percussion_instruments = json.load(f)

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
        backup_filename = f"log/drum_loop_prompt_history_{timestamp}.txt"
        
        # Copy the original file to the backup file
        shutil.copy2(filename, backup_filename)
        
        # Overwrite the original file with the new text
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(new_text)
            
        print(f"File size exceeded 5 KB. Prompt history cleared and data written. Created backup: {backup_filename}")

# Generate a drum loop prompt less than 200 characters in string length
def generate_drum_loop_simple():
    combination = ""
    while True:
        drum_loop_genre_choice = random.choice(drum_loop_genre)
        drum_kit_choice = random.choice(drum_kits)
        percussion_instrument_choice_1 = random.choice(percussion_instruments)
        percussion_instrument_choice_2 = random.choice(percussion_instruments)
        percussion_instrument_choice_3 = random.choice(percussion_instruments)
        percussion_instrument_choice_4 = random.choice(percussion_instruments)
        style_choice = random.choice(["Rhythm-Only", "Pitched Drum Elements", "Electronic"])
        tempo_choice = random.choice(tempos)
        tempo_choice_int = random.randint(tempo_choice[1], tempo_choice[2])
        musical_key_choice = random.choice(musical_keys)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        yt_title = f"{drum_loop_genre_choice[0]} {timestamp} [{drum_kit_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
        check_and_write_to_file('log/drum_loop_prompt_history.txt', yt_title)
        print(yt_title)
        print("")

        suno_song_title = f"{drum_loop_genre_choice[0]} {drum_kit_choice[0]} {tempo_choice[0]} {tempo_choice_int} {timestamp}\n\n"
        check_and_write_to_file('log/drum_loop_prompt_history.txt', suno_song_title)
        print(suno_song_title)
        print("")
        
        yt_descr = f"Using AI to generate {drum_loop_genre_choice[0]} drum loops from a variety of genres, musical keys, and modes for musicians to rehearse with.\n\n"
        check_and_write_to_file('log/drum_loop_prompt_history.txt', yt_descr)
        print(yt_descr)
        print("")

        combination = f'{drum_loop_genre_choice[0]}, {drum_kit_choice[0]}, {drum_kit_choice[1]}, {drum_kit_choice[2]}, {drum_kit_choice[3]}, {drum_kit_choice[4]}, {percussion_instrument_choice_1[0]}, {percussion_instrument_choice_2[0]}, {percussion_instrument_choice_3[0]}, {percussion_instrument_choice_4[0]}, {style_choice}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        
        if len(combination) < 200:
            check_and_write_to_file('log/drum_loop_prompt_history.txt', "Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:\n")
            print("Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:")
            break
        
    return combination

new_prompt_div = "\n\n------------------------------New Prompt-------------------------------------\n"

check_and_write_to_file('log/drum_loop_prompt_history.txt', new_prompt_div)
print("\n------------------------------New Prompt-------------------------------------\n")
# Generate and print the drum_loop_simple string
# print("Drum loop prompt less than 200 characters in string length:")
drum_loop_simple_prompt = generate_drum_loop_simple()
check_and_write_to_file('log/drum_loop_prompt_history.txt', drum_loop_simple_prompt)
print(drum_loop_simple_prompt)

#generate exclude styles prompt and write to file
exclude_styles_prompt = f'\n\nExclude Styles:\n{anti_percussion_instruments[0]}, {anti_percussion_instruments[1]}, {anti_percussion_instruments[2]}, {anti_percussion_instruments[3]}, {anti_percussion_instruments[4]}, {anti_percussion_instruments[5]}, {anti_percussion_instruments[6]}, {anti_percussion_instruments[7]}, {anti_percussion_instruments[8]}, {anti_percussion_instruments[9]}, {anti_percussion_instruments[10]}, {anti_percussion_instruments[11]}, {anti_percussion_instruments[12]}, {anti_percussion_instruments[13]}'
check_and_write_to_file('log/drum_loop_prompt_history.txt', exclude_styles_prompt)
print(exclude_styles_prompt)

check_and_write_to_file('log/drum_loop_prompt_history.txt', "\n\n[Instrumental Drum Loop]")
print("\n[Instrumental Drum Loop]")
check_and_write_to_file('log/drum_loop_prompt_history.txt', "\n\nOwnership and commercial use rights is retained for any songs generated by my self using Suno during active subscription, even after cancelling. Proof of ownership is available upon request. For more information, please reference Suno Knowledge Base Articles at https://help.suno.com/en/articles/2421505")
