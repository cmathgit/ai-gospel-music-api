import time
import requests
import random
import json
from suno_api import generate_audio_by_prompt, get_audio_information, wait_for_song, download_mp3_file
from youtube_api import print_lyric_video_descr_simple
#from biblegateway_api import get_bible_votd_kjv, get_bible_votd_amp, get_bible_votd_msg

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

   
    # Use Bible Gateway Verse of the Day
    #votds = get_bible_votd_kjv()
    #print("Bible Verse Content: ", votds['votd']['content'])
    #print("Bible Verse reference: ", votds['votd']['reference'])
    #print("Bible Verse reference: ", votds['votd']['version'])
    #biblecontent = votds['votd']['content']
    #biblereference = votds['votd']['reference']
    #bibleversion = votds['votd']['version']
    
    # Randomly select a book of the bible
    bible_book_file_path = 'lib/bible_book_dict.json'
    try:
        with open(bible_book_file_path, 'r') as bible_book_file:
            bible_chapters = json.load(bible_book_file)
    except IOError as e:
        print("Error reading from file:", e)
    
    #print(bible_chapters)
    # Randomly select a book of the bible and total chapters
    random_book, max_chapters = random.choice(bible_chapters)

    # Randomly select a chapter from the chosen book
    random_chapter = random.randint(1, max_chapters)

    print(f"Randomly selected book: {random_book}")
    print(f"Randomly selected chapter: {random_chapter}")
    
    biblereference = f"{random_book} {random_chapter}"
    bibleversion = "King James Version"
    
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
    
    
    # Randomly select a vocalist
    vocalists_data_file_path = 'lib/vocalists_dict.json'
    try:
        with open(vocalists_data_file_path, 'r') as vocalists_file:
            vocalists = json.load(vocalists_file)
    except IOError as e:
        print("Error reading from file:", e)
        
    # print(vocalists)
    random_vocal_range, voice_type, vocalist_gender = random.choice(vocalists)
    lead_vocalist = f"{vocalist_gender} {voice_type} {random_vocal_range}"
    print(f"Randomly selected vocalist (gender, range, and type): {lead_vocalist}")
    
    
    # Randomly select a genre
    song_genre_data_file_path = 'lib/bible_song_genre_dict.json'
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
        f"{random_genre}, {random_key} ({majorminor}), lead {lead_vocalist} singer, {random_instrument}, lyrics inspired by the message of {biblereference} from the {bibleversion} bible"
        #f"Starting with these exact words {biblecontent} generate lyrics inspired by the message of {biblereference} directly taken from the {bibleversion} bible"
    ]

    for prompt in prompts:
        if len(prompt) > 200:
            print("Prompt too long, max character limit is 200, yours is: ", len(prompt))
            continue

        # print prompts for debugging
        print("===== PROMPTING SUNO =====")
        print(prompt)
        
        # print prompts for debugging
        dbug_prompt_file = 'log/last_prompts_sent_to_suno_api_generate.txt'
        py_script_used = "generate_biblical_lyrics_simple_prompts.py"
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
        
        if data is not None:
            print("Response received from Suno /api/generate: ", data)
            suno_api_generate_response_file = 'log/last_response_received_from_suno_api_generate.txt'
            try:
                with open(suno_api_generate_response_file, "w") as file:
                    file.write(f"{data}")
            except IOError as e:
                print(f"Error writing to {suno_api_generate_response_file}: ", e)
        else: 
            print("Request to Suno /api/generate failed.")
        
        ids = [data[0]['id'], data[1]['id']]
        print(f"Pending IDs: {ids}")
        
        for id in ids:
            wait_for_song(id)
            data_audio_info = get_audio_information(id)
            song_info = data_audio_info[0]
            print_lyric_video_descr_simple(id, user, random_genre, random_key, majorminor, biblereference, bibleversion, prompt, song_info)
