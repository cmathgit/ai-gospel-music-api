import time
import requests
import random
import json
from suno_api import generate_audio_by_prompt, get_audio_information, download_mp3_file, wait_for_song
from youtube_api import print_instrumental_video_descr_simple


if __name__ == '__main__':

    user = "crossofthemessiah"
    # Randomly select a music key
    music_key_file_path = 'lib/music_key_dict.json'
    try:
        with open(music_key_file_path, 'r') as music_key_file:
            music_key_data = json.load(music_key_file)
    except IOError as e:
        print("Error reading from file:", e)

    #print(music_key_data) 
    random_key, tonic, majorminor, mode = random.choice(music_key_data)
    print(f"Randomly selected key: {random_key}")
    print(f"Randomly selected tonic note: {tonic}")
    print(f"Randomly selected whether major or minor: {majorminor}")
    print(f"Randomly selected mode: {mode}")


    # Randomly select an instrument
    instrument_data_file_path = 'lib/instrument_dict.json'
    try:
        with open(instrument_data_file_path, 'r') as instrument_file:
            instruments = json.load(instrument_file)
    except IOError as e:
        print("Error reading from file:", e)
    
    #print(instruments)
    random_instrument = random.choice(instruments)
    print(f"Randomly selected instrument: {random_instrument}")


    # Randomly select a genre
    song_genre_data_file_path = 'lib/instrumental_song_genre_dict.json'
    try:
        with open(song_genre_data_file_path, 'r') as song_genre_file:
            song_genre = json.load(song_genre_file)
    except IOError as e:
        print("Error reading from file:", e)
 
    #print(song_genre)
    
    random_genre, instrumental = random.choice(song_genre)
    print(f"Randomly selected genre: {random_genre}")
    print(f"Instrumental: {instrumental}")
    
    prompts = [ 
        f"{random_genre}, {random_instrument}, in the key of {random_key} ({majorminor})"
        #f"Popular {random_genre} song in key of {random_key} ({majorminor})"
        #f"Starting with these exact words {biblecontent} generate lyrics inspired by the message of {biblereference} directly taken from the {bibleversion} bible"
    ]

    for prompt in prompts:
        if len(prompt) > 200:
            print("Prompt too long, max character limit is 200, yours is: ", len(prompt))
            continue

        print()
        # print prompt for debugging
        print("===== PROMPTING SUNO =====")
        print(prompt)
        
        # print prompts for debugging
        dbug_prompt_file = 'log/last_prompts_sent_to_suno_api_generate.txt'
        py_script_used = "generate_instrumental_simple_prompt.py"
        simple_prompt_len = len(prompt)
        
        try:
            with open(dbug_prompt_file, "w") as file:
                file.write(f"Python Script: {py_script_used}\nFor debugging prompts\n\nPrompt sent to Suno /api/generate: {prompt}\nSimple Song Description String Length: {simple_prompt_len}\nSimple Song Description Max Allotted String Length: 200")
        except IOError as e:
            print(f"Error writing to {dbug_prompt_file}: ", e)
        
        data = generate_audio_by_prompt({
            "prompt": prompt,
            "make_instrumental": instrumental,
            "wait_audio": False
        })
        
        ids = [data[0]['id'], data[1]['id']]
        print(f"Pending IDs: {ids}")
        
        for id in ids:
            wait_for_song(id)
            data_audio_info = get_audio_information(id)
            song_info = data_audio_info[0]
            print_instrumental_video_descr_simple(id, user, random_genre, random_instrument, random_key, majorminor, prompt, song_info)
