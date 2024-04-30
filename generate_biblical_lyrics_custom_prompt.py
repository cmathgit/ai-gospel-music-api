import time
import requests
import random
import json
from suno_api import custom_generate_audio, generate_song_lyrics, get_audio_information, download_mp3_file, wait_for_song
from youtube_api import print_lyric_video_descr_custom
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


    #Use Bible Gateway Verse of the Day
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
    
    #random_book, testament, max_chapters = random.choice(bible_chapters)
        

    # Randomly select a chapter from the chosen book
    random_chapter = random.randint(1, max_chapters)

    print(f"Randomly selected book: {random_book}")
    print(f"Randomly selected chapter: {random_chapter}")
    
    biblereference = f"{random_book} {random_chapter}"
    bibleversion = "King James Version"

    gen_lyric_prompts = [
        f"Generate passionate, meaningful, heartfelt, and profound lyrics to a song inspired by and devoted to preserving the message of {biblereference} taken directly from the {bibleversion} bible with remnants of the Gospel of Jesus Christ"
    ]
    
    #gen_lyric_prompts = [f"Generate passionate, meaningful, heartfelt, and profound lyrics to a song inspired by the Biblical exegesis and devoted to preserving the message of {biblereference} taken directly from the {bibleversion} bible incorporating elements of and parallels to the Gospel of Jesus Christ found in the New Testament"]
    
    # if testament is "Old Testament":
        #gen_lyric_prompts = [f"Generate passionate, meaningful, heartfelt, and profound lyrics to a song inspired by the Biblical exegesis and devoted to preserving the message of {biblereference} of the {testament} bible taken directly from the {bibleversion} detailing the relationship between elements of the Old Testament with aspects of and parallels to the Gospel of Jesus Christ as depicted in the New Testament"]
    #else: 
        #gen_lyric_prompts = [f"Generate passionate, meaningful, heartfelt, and profound lyrics to a song inspired by the Biblical exegesis and devoted to preserving the message of {biblereference} of the {testament} bible taken directly from the {bibleversion} emphasizing the significance of the Gospel of Jesus Christ as depicted in the New Testament"]
    
    #gen_lyric_prompts = [f"Generate passionate, meaningful, heartfelt, and profound lyrics to a song inspired by the Biblical exegesis and devoted to preserving the message of {biblereference} taken directly from the {bibleversion} bible incorporating elements of prefiguration with surviving traces of and parallels to the Gospel of Jesus Christ found in the New Testament"]
    
    #gen_lyric_prompts = [f"Generate passionate, meaningful, heartfelt, and profound lyrics to a song inspired by the Biblical exegesis and devoted to preserving the message of {biblereference} taken directly from the {bibleversion} bible incorporating elements of prefiguration with surviving traces of and parallels to the Gospel of Jesus Christ"]

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
    
    style_of_music_prompt = f"{random_genre}, {random_key} ({majorminor}), {lead_vocalist} singer, {random_instrument}"
    print("Style of Music Prompt: ", style_of_music_prompt)
    
    for gen_lyric_prompt in gen_lyric_prompts:

        print("===== PROMPTING SUNO FOR LYRICS =====")
        print("Lyrics Prompt: ", gen_lyric_prompt)
        
        lyrics = generate_song_lyrics({
           "prompt": gen_lyric_prompt
         })
        
        print("Generate Lyrics Response Body: ", lyrics)
        print("Lyrics generated: ", lyrics['text'])
        print("Title generated: ", lyrics['title'])
        print("Genre Chosen: ", random_genre)
        print("Mode Chosen: ", majorminor)
        
        # write api responses to log file
        if lyrics is not None:
            print("Response received from Suno api/generate_lyrics: ", lyrics)
            suno_api_generate_lyrics_response_file = 'log/last_response_received_from_suno_api_generate_lyrics.txt'
            try:
                with open(suno_api_generate_lyrics_response_file, "w") as file:
                    file.write(f"{lyrics}")
            except IOError as e:
                print(f"Error writing to {suno_api_generate_lyrics_response_file}: ", e)
        else: 
            print("Request to Suno api/generate_lyrics failed.")
        
        
        text = lyrics['text']
        title = lyrics['title']

        print("===== PROMPTING SUNO FOR SONG =====")
        print("Style of Music Prompt: ", style_of_music_prompt)
        
        # print prompts for debugging
        dbug_prompt_file = 'log/last_prompts_sent_to_suno_api_custom_generate.txt'
        py_script_used = "generate_biblical_lyrics_custom_prompt.py"
        gen_lyric_prompt_len = len(gen_lyric_prompt)
        title_prompt_len = len(title)
        lyrics_prompt_len = len(text)
        style_of_music_prompt_len = len(style_of_music_prompt)
        
        try:
            with open(dbug_prompt_file, "w") as file:
                file.write(f"Python Script: {py_script_used}\nFor debugging prompts\n\nGenerate Lyrics Prompt sent to Suno /api/generate_lyrics: {gen_lyric_prompt}\nGenerate Lyrics Prompt String Length: {gen_lyric_prompt_len}\nGenerate Lyrics Prompt Max Allotted String Length: 399\n\nSong Title Prompt sent to Suno /api/custom_generate:\n{title}\nSong Title Prompt String Length: {title_prompt_len}\nSong Title Prompt Max Allotted String Length: 80\n\nLyrics Prompt sent to Suno /api/custom_generate:\n{text}\nLyrics Prompt Length: {lyrics_prompt_len}\nLyrics Prompt Max Allotted String Length: 1250\n\nCustom Style of Music Prompt sent to Suno /api/custom_generate: {style_of_music_prompt}\nCustom Style of Music Prompt String Length: {style_of_music_prompt_len}\nCustom Style of Music Max Allotted String Length: 120")
        except IOError as e:
            print(f"Error writing to {dbug_prompt_file}: ", e)

        data = custom_generate_audio({
           "prompt": text,
           "tags": style_of_music_prompt,
           "title": title,
           "make_instrumental": instrumental,
           "wait_audio": False
        })
        
        # write api responses to log file
        if data is not None:
            print("Response received from Suno api/custom_generate: ", data)
            suno_api_custom_generate_response_file = 'log/last_response_received_from_suno_api_custom_generate.txt'
            try:
                with open(suno_api_custom_generate_response_file, "w") as file:
                    file.write(f"{data}")
            except IOError as e:
                print(f"Error writing to {suno_api_custom_generate_response_file}: ", e)
        else: 
            print("Request to Suno api/custom_generate failed.")
        
        ids = [data[0]['id'], data[1]['id']]
        print(f"Pending IDs: {ids}")

        for id in ids:
            wait_for_song(id)
            data_audio_info = get_audio_information(id)
            song_info = data_audio_info[0]
            print_lyric_video_descr_custom(id, user, title, text, style_of_music_prompt, random_genre, random_key, majorminor, biblereference, bibleversion, gen_lyric_prompt, song_info)

