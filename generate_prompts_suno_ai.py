import json
import random
from datetime import datetime
from datetime import timedelta
from biblegateway_api import get_bible_votd_kjv #, get_bible_votd_amp, get_bible_votd_msg
from write_to_file import check_and_write_to_file

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

with open('lib/drum_loop_genres_dict.json') as f:
    drum_loop_genre = json.load(f)

with open('lib/drum_kits_dict.json') as f:
    drum_kits = json.load(f)

with open('lib/percussion_instruments_dict.json') as f:
    percussion_instruments = json.load(f)

with open('lib/anti_percussion_instruments_dict.json') as f:
    anti_percussion_instruments = json.load(f)

with open('lib/exclude_pop_genres_dict.json') as f:
    exclude_pop_genres = json.load(f)

# with open('lib/concerto_instrument_families_dict.json') as f:
#     concerto_instrument_families = json.load(f)

with open('lib/concerto_variants_dict.json') as f:
    concerto_variants = json.load(f)

with open('lib/concerto_instrument_family_woodwinds_dict.json') as f:
    concerto_instrument_family_woodwinds = json.load(f)

with open('lib/concerto_instrument_family_brass_dict.json') as f:
    concerto_instrument_family_brass = json.load(f) 

with open('lib/concerto_instrument_family_percussion_dict.json') as f:
    concerto_instrument_family_percussion = json.load(f)

with open('lib/concerto_instrument_family_string_dict.json') as f:
    concerto_instrument_family_strings = json.load(f)

with open('lib/concerto_instrument_family_keys_dict.json') as f:
    concerto_instrument_family_keys = json.load(f)

# Function to generate a random biblical song prompt less than 200 characters in string length
def generate_biblical_song_simple():
    song_descr_prompt = ""
    while True:
        bible_song_genre_choice = random.choice(song_genre)
        vocalist_choice = random.choice(vocalists)
        instrument_choice_1 = random.choice(instruments)
        instrument_choice_2 = random.choice(instruments)
        bible_book_choice = random.choice(bible_chapters)
        bible_chap_choice = random.randint(1, bible_book_choice[1])
        tempo_choice = random.choice(tempos)
        tempo_choice_int = random.randint(tempo_choice[1], tempo_choice[2])
        musical_key_choice = random.choice(musical_keys)
        
        timestamp = datetime.now()
        timestamp_str = timestamp.strftime('%Y%m%d_%H%M%S')
        timestamp_plus_1_sec = (timestamp + timedelta(seconds=1)).strftime('%Y%m%d_%H%M%S')

        yt_title_1 = f"Bible {bible_book_choice[0]} {bible_chap_choice} {bible_song_genre_choice[0]} {timestamp_str} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
        check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', yt_title_1)
        print(yt_title_1)
        print("")

        yt_title_2 = f"Bible {bible_book_choice[0]} {bible_chap_choice} {bible_song_genre_choice[0]} {timestamp_plus_1_sec} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
        check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', yt_title_2)
        print(yt_title_2)
        print("")

        suno_song_title = f"Bible {bible_book_choice[0]} {bible_chap_choice} {bible_song_genre_choice[0]} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_str}\n\n"
        suno_song_title_clean = suno_song_title.replace(",", "")
        check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', suno_song_title_clean)
        print(suno_song_title_clean)
        print("")

        suno_song_title_2 = f"Bible {bible_book_choice[0]} {bible_chap_choice} {bible_song_genre_choice[0]} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_plus_1_sec}\n\n"
        suno_song_title_clean_2 = suno_song_title_2.replace(",", "")
        check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', suno_song_title_clean_2)
        print(suno_song_title_clean_2)
        print("")
        
        yt_descr = f"Using AI to generate biblically accurate {bible_song_genre_choice[0]} songs and music videos.\n\n"
        check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', yt_descr)
        print(yt_descr)
        print("")
        
        song_descr_prompt = f'{bible_song_genre_choice[0]}, {vocalist_choice[0]} ({vocalist_choice[2]}), {instrument_choice_1}, {instrument_choice_2}, biblically inspired lyrics book of {bible_book_choice[0]} chapter {bible_chap_choice}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        
        if len(song_descr_prompt) < 200:
            check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', "Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:\n")
            print("Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:")
            break
    
    return song_descr_prompt
    
# Function to generate a random biblical song prompt less than 200 characters in string length
def generate_biblical_song_custom():
    lyrics_prompt = ""
    style_of_music_prompt = ""
    while True:
        song_genre_choice = random.choice(bible_song_genre)
        vocalist_choice = random.choice(vocalists)
        instrument_choice_1 = random.choice(instruments)
        instrument_choice_2 = random.choice(instruments)
        instrument_choice_3 = random.choice(instruments)
        bible_book_choice = random.choice(bible_chapters)
        bible_chap_choice = random.randint(1, bible_book_choice[1])
        tempo_choice = random.choice(tempos)
        tempo_choice_int = random.randint(tempo_choice[1], tempo_choice[2])
        musical_key_choice = random.choice(musical_keys)

        timestamp = datetime.now()
        timestamp_str = timestamp.strftime('%Y%m%d_%H%M%S')
        timestamp_plus_1_sec = (timestamp + timedelta(seconds=1)).strftime('%Y%m%d_%H%M%S')
        yt_title_1 = f"Bible {bible_book_choice[0]} {bible_chap_choice} {song_genre_choice[0]} {timestamp_str} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
        check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', yt_title_1)
        print(yt_title_1)
        print("")
        
        yt_title_2 = f"Bible {bible_book_choice[0]} {bible_chap_choice} {song_genre_choice[0]} {timestamp_plus_1_sec} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
        check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', yt_title_2)
        print(yt_title_2)
        print("")
        
        suno_song_title_1 = f"Bible {bible_book_choice[0]} {bible_chap_choice} {song_genre_choice[0]} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_str}\n\n"
        suno_song_title_clean_1 = suno_song_title_1.replace(",", "")
        check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', suno_song_title_clean_1)
        print(suno_song_title_clean_1)
        print("")
        
        suno_song_title_2 = f"Bible {bible_book_choice[0]} {bible_chap_choice} {song_genre_choice[0]} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_plus_1_sec}\n\n"
        suno_song_title_clean_2 = suno_song_title_2.replace(",", "")
        check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', suno_song_title_clean_2)
        print(suno_song_title_clean_2)
        print("")

        yt_descr = f"Using AI to generate biblically accurate {song_genre_choice[0]} songs and music videos.\n\n"
        check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', yt_descr)
        print(yt_descr)
        print("")
        
        lyrics_prompt = f'Generate biblically accurate lyrics inspired by the message of the book of {bible_book_choice[0]} chapter {bible_chap_choice} quoting verses taken from the King James Version bible'
        
        style_of_music_prompt = f'{song_genre_choice[0]}, {vocalist_choice[0]} ({vocalist_choice[2]}), {instrument_choice_1}, {instrument_choice_2}, {instrument_choice_3}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        
        if len(style_of_music_prompt) < 120 and len(lyrics_prompt) < 399:
            concat_prompts = f"Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:\n{style_of_music_prompt}\n\nLyrics Prompt:\n{lyrics_prompt}\n"
            #check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', concat_prompts)
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
        tempo_choice_int = random.randint(tempo_choice[1], tempo_choice[2])
        musical_key_choice = random.choice(musical_keys)
        
        timestamp = datetime.now()  
        timestamp_str = timestamp.strftime('%Y%m%d_%H%M%S')
        timestamp_plus_1_sec = (timestamp + timedelta(seconds=1)).strftime('%Y%m%d_%H%M%S')

        yt_title_1 = f"Instrumental {instrumental_song_genre_choice[0]} {timestamp_str} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
        check_and_write_to_file('log/instrumental_song_prompt_history.txt', 'instrumental_song_prompt_history', yt_title_1)
        print(yt_title_1)
        print("")

        yt_title_2 = f"Instrumental {instrumental_song_genre_choice[0]} {timestamp_plus_1_sec} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
        check_and_write_to_file('log/instrumental_song_prompt_history.txt', 'instrumental_song_prompt_history', yt_title_2)
        print(yt_title_2)
        print("")

        suno_song_title_1 = f"Instrumental {instrumental_song_genre_choice[0]} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_str}\n\n"
        suno_song_title_clean_1 = suno_song_title_1.replace(",", "")
        check_and_write_to_file('log/instrumental_song_prompt_history.txt', 'instrumental_song_prompt_history', suno_song_title_clean_1)
        print(suno_song_title_clean_1)
        print("")

        suno_song_title_2 = f"Instrumental {instrumental_song_genre_choice[0]} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_plus_1_sec}\n\n"
        suno_song_title_clean_2 = suno_song_title_2.replace(",", "")
        check_and_write_to_file('log/instrumental_song_prompt_history.txt', 'instrumental_song_prompt_history', suno_song_title_clean_2)
        print(suno_song_title_clean_2)
        print("")   
        
        yt_descr = f"Using AI to generate {instrumental_song_genre_choice[0]} instrumentals and loops for vocalists and musicians from a variety of genres, musical keys, and modes.\n\n"
        check_and_write_to_file('log/instrumental_song_prompt_history.txt', 'instrumental_song_prompt_history', yt_descr)
        print(yt_descr)
        print("")
        
        combination = f'{instrumental_song_genre_choice[0]}, {instrument_choice_1}, {instrument_choice_2}, {instrument_choice_3}, {instrument_choice_4}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        
        if len(combination) < 200:
            check_and_write_to_file('log/instrumental_song_prompt_history.txt', 'instrumental_song_prompt_history', "Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:\n")
            print("Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:")
            break
    
    return combination
    

# Function to generate a random biblical song prompt less than 200 characters in string length
def generate_bible_gateway_votd_song_custom():
    lyrics_prompt = ""
    style_of_music_prompt = ""
    
    # Remove while loop. Need to limit length of payload returned from end point first.
    # while True:
    song_genre_choice = random.choice(bible_song_genre)
    vocalist_choice = random.choice(vocalists)
    instrument_choice_1 = random.choice(instruments)
    instrument_choice_2 = random.choice(instruments)
    instrument_choice_3 = random.choice(instruments)
        
    #bible_book_choice = random.choice(bible_chapters)
    #bible_chap_choice = random.randint(1, bible_book_choice[1])
        
    # Use Bible Gateway Verse of the Day
    votds = get_bible_votd_kjv()
    print("Bible Verse Content: ", votds['votd']['content'])
    print("Bible Verse reference: ", votds['votd']['reference'])
    print("Bible Verse reference: ", votds['votd']['version'])
    biblecontent = votds['votd']['content']
    biblereference = votds['votd']['reference']
    biblereference_clean = biblereference.replace(":", "_")
    bibleversion = votds['votd']['version']
    verselink = votds['votd']['permalink']
    print(verselink)
        
    tempo_choice = random.choice(tempos)
    tempo_choice_int = random.randint(tempo_choice[1], tempo_choice[2])
    musical_key_choice = random.choice(musical_keys)

    timestamp = datetime.now()  
    timestamp_str = timestamp.strftime('%Y%m%d_%H%M%S')
    timestamp_plus_1_sec = (timestamp + timedelta(seconds=1)).strftime('%Y%m%d_%H%M%S')

    yt_title_1 = f"VOTD {biblereference} {song_genre_choice[0]} {timestamp_str} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
    check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', yt_title_1)
    print(yt_title_1)
    print("")

    yt_title_2 = f"VOTD {biblereference} {song_genre_choice[0]} {timestamp_plus_1_sec} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
    check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', yt_title_2)
    print(yt_title_2)
    print("")

    suno_song_title_1 = f"VOTD {biblereference_clean} {song_genre_choice[0]} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_str}\n\n"
    suno_song_title_clean_1 = suno_song_title_1.replace(",", "")
    check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', suno_song_title_clean_1)
    print(suno_song_title_clean_1)
    print("")

    suno_song_title_2 = f"VOTD {biblereference_clean} {song_genre_choice[0]} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_plus_1_sec}\n\n"
    suno_song_title_clean_2 = suno_song_title_2.replace(",", "")
    check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', suno_song_title_clean_2)
    print(suno_song_title_clean_2)
    print("")
        
    yt_descr = f"Using AI to generate biblically accurate {song_genre_choice[0]} songs and music videos.\n\n"
    check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', yt_descr)
    print(yt_descr)
    print("")
        
    lyrics_prompt = f'Generate biblically accurate lyrics inspired by the message of {biblereference} quoting this verse verbatim taken from the {bibleversion} bible: {biblecontent}'
    
    if len(lyrics_prompt) > 399:
        lyrics_prompt = {biblecontent}
        
    style_of_music_prompt = f'{song_genre_choice[0]}, {vocalist_choice[0]} ({vocalist_choice[2]}), {instrument_choice_1}, {instrument_choice_2}, {instrument_choice_3}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        
        # if len(style_of_music_prompt) < 120 and len(lyrics_prompt) < 399:
    concat_prompts = f"Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:\n{style_of_music_prompt}\n\nLyrics Prompt:\n{lyrics_prompt}\n\n{bibleversion}\nPublic Domain\n\nPrompt generated using Verse of the Day (votd) endpoint provided by BibleGateway\n{verselink}"
            # break
            
    return concat_prompts

def generate_drum_loop():
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
        
        timestamp = datetime.now()
        timestamp_str = timestamp.strftime('%Y%m%d_%H%M%S')
        timestamp_plus_1_sec = (timestamp + timedelta(seconds=1)).strftime('%Y%m%d_%H%M%S')

        yt_title_1 = f"{drum_loop_genre_choice[0]} {timestamp_str} [{drum_kit_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
        check_and_write_to_file('log/drum_loop_prompt_history.txt', 'drum_loop_prompt_history', yt_title_1)
        print(yt_title_1)
        print("")

        yt_title_2 = f"{drum_loop_genre_choice[0]} {timestamp_plus_1_sec} [{drum_kit_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
        check_and_write_to_file('log/drum_loop_prompt_history.txt', 'drum_loop_prompt_history', yt_title_2)
        print(yt_title_2)
        print("")

        suno_song_title_1 = f"{drum_loop_genre_choice[0]} {drum_kit_choice[0]} {tempo_choice[0]} {tempo_choice_int} {timestamp_str}\n\n"
        suno_song_title_clean_1 = suno_song_title_1.replace(",", "")
        check_and_write_to_file('log/drum_loop_prompt_history.txt', 'drum_loop_prompt_history', suno_song_title_clean_1)
        print(suno_song_title_clean_1)
        print("")
        
        suno_song_title_2 = f"{drum_loop_genre_choice[0]} {drum_kit_choice[0]} {tempo_choice[0]} {tempo_choice_int} {timestamp_plus_1_sec}\n\n"
        suno_song_title_clean_2 = suno_song_title_2.replace(",", "")
        check_and_write_to_file('log/drum_loop_prompt_history.txt', 'drum_loop_prompt_history', suno_song_title_clean_2)
        print(suno_song_title_clean_2)
        print("")
        
        yt_descr = f"Using AI to generate {drum_loop_genre_choice[0]} drum loops from a variety of genres, musical keys, and modes for musicians to rehearse with.\n\n"
        check_and_write_to_file('log/drum_loop_prompt_history.txt', 'drum_loop_prompt_history', yt_descr)
        print(yt_descr)
        print("")
        
        combination = f'{drum_loop_genre_choice[0]}, {drum_kit_choice[0]}, {drum_kit_choice[1]}, {drum_kit_choice[2]}, {drum_kit_choice[3]}, {drum_kit_choice[4]}, {percussion_instrument_choice_1[0]}, {percussion_instrument_choice_2[0]}, {percussion_instrument_choice_3[0]}, {percussion_instrument_choice_4[0]}, {style_choice}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        
        if len(combination) < 200:
            check_and_write_to_file('log/drum_loop_prompt_history.txt', 'drum_loop_prompt_history', "Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:\n")
            print("Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:")
            break
        
    return combination

def generate_concerto_prompt():
    combination = ""
    while True:
        concerto_variant_choice = random.choice(concerto_variants)
        concerto_variant_name = concerto_variant_choice['name']
        concerto_variant_number_of_soloists = concerto_variant_choice['soloists']
        concerto_variant_ensemble = concerto_variant_choice['ensemble']
        #concerto_variant_description = concerto_variant_choice['description']
        tempo_choice = random.choice(tempos)
        tempo_choice_int = random.randint(tempo_choice[1], tempo_choice[2])
        musical_key_choice = random.choice(musical_keys)
        
        timestamp = datetime.now()
        timestamp_str = timestamp.strftime('%Y%m%d_%H%M%S')
        timestamp_plus_1_sec = (timestamp + timedelta(seconds=1)).strftime('%Y%m%d_%H%M%S')

        yt_title_1 = f"{concerto_variant_name} {concerto_variant_ensemble} {timestamp_str} [{tempo_choice[0]}] [{musical_key_choice[0]}] [AI Music]\n\n"
        check_and_write_to_file('log/concerto_prompt_history.txt', 'concerto_prompt_history', yt_title_1)
        print(yt_title_1)
        print("")

        yt_title_2 = f"{concerto_variant_name} {concerto_variant_ensemble} {timestamp_plus_1_sec} [{tempo_choice[0]}] [{musical_key_choice[0]}] [AI Music]\n\n"
        check_and_write_to_file('log/concerto_prompt_history.txt', 'concerto_prompt_history', yt_title_2)
        print(yt_title_2)
        print("")

        suno_song_title_1 = f"{concerto_variant_name} {concerto_variant_ensemble} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_str}\n\n"
        suno_song_title_clean_1 = suno_song_title_1.replace(",", "")
        check_and_write_to_file('log/concerto_prompt_history.txt', 'concerto_prompt_history', suno_song_title_clean_1)
        print(suno_song_title_clean_1)
        print("")

        suno_song_title_2 = f"{concerto_variant_name} {concerto_variant_ensemble} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_plus_1_sec}\n\n"
        suno_song_title_clean_2 = suno_song_title_2.replace(",", "")
        check_and_write_to_file('log/concerto_prompt_history.txt', 'concerto_prompt_history', suno_song_title_clean_2)
        print(suno_song_title_clean_2)
        print("")
        
        yt_descr = f"Using AI to generate concertos in spite of Geoffrey Jefferson's reflections on artificial intelligence.\n\nOn June 9, at Manchester University’s Lister Oration, British brain surgeon Geoffrey Jefferson states, \"Not until a machine can write a sonnet or compose a concerto because of thoughts and emotions felt, and not by the chance fall of symbols, could we agree that machine equals brain – that is, not only write it but know that it had written it. No mechanism could feel (and not merely artificially signal, an easy contrivance) pleasure at its successes, grief when its valves fuse, be warmed by flattery, be made miserable by its mistakes, be charmed by sex, be angry or miserable when it cannot get what it wants.\""
        check_and_write_to_file('log/concerto_prompt_history.txt', 'concerto_prompt_history', yt_descr)
        print(yt_descr)
        print("")

        if concerto_variant_number_of_soloists < 4:
            concerto_number_of_soloist_choice = concerto_variant_number_of_soloists
        else:
            concerto_number_of_soloist_choice = random.randint(2, concerto_variant_number_of_soloists)

        print(concerto_number_of_soloist_choice)
        print(concerto_variant_ensemble)
        print("\n")

        if concerto_variant_ensemble == "Symphony":
            if concerto_number_of_soloist_choice == 1:
                combination = f'{concerto_variant_name}, {random.choice(concerto_instrument_family_woodwinds)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # single soloist
            elif concerto_number_of_soloist_choice == 2:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_woodwinds)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # double soloists
            elif concerto_number_of_soloist_choice == 3:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_woodwinds)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # triple soloists
            elif concerto_number_of_soloist_choice == 4:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_woodwinds)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # quadruple soloists
            else:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {concerto_instrument_family_woodwinds[0]["name"]}, {concerto_instrument_family_woodwinds[1]["name"]}, {concerto_instrument_family_woodwinds[2]["name"]}, {concerto_instrument_family_woodwinds[3]["name"]}, {concerto_instrument_family_woodwinds[4]["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        elif concerto_variant_ensemble == "Baroque Ensemble":
            if concerto_number_of_soloist_choice == 1:
                combination = f'{concerto_variant_name}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # single soloist
            elif concerto_number_of_soloist_choice == 2:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # double soloists
            elif concerto_number_of_soloist_choice == 3:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # triple soloists
            elif concerto_number_of_soloist_choice == 4:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # quadruple soloists
            else:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(concerto_instrument_family_strings)["name"]}, Harpsichord, {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        elif concerto_variant_ensemble == "Baroque Orchestra":
            if concerto_number_of_soloist_choice == 1:
                combination = f'{concerto_variant_name}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # single soloist
            elif concerto_number_of_soloist_choice == 2:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # double soloists
            elif concerto_number_of_soloist_choice == 3:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # triple soloists
            elif concerto_number_of_soloist_choice == 4:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # quadruple soloists
            else:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(["Trumpet","Horn"])}, {random.choice(["Harpsichord","Organ"])}, {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        elif concerto_variant_ensemble == "Classical Orchestra":
            if concerto_number_of_soloist_choice == 1:
                combination = f'{concerto_variant_name}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # single soloist
            elif concerto_number_of_soloist_choice == 2:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # double soloists
            elif concerto_number_of_soloist_choice == 3:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # triple soloists
            elif concerto_number_of_soloist_choice == 4:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # quadruple soloists
            else:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(concerto_instrument_family_brass)["name"]}, {random.choice(["Harpsichord","Fortepiano"])}, {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        elif concerto_variant_ensemble == "Romantic Orchestra":
            if concerto_number_of_soloist_choice == 1:
                combination = f'{concerto_variant_name}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # single soloist
            elif concerto_number_of_soloist_choice == 2:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # double soloists
            elif concerto_number_of_soloist_choice == 3:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # triple soloists
            elif concerto_number_of_soloist_choice == 4:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # quadruple soloists
            else:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(concerto_instrument_family_brass)["name"]}, {random.choice(["Piano","Organ"])}, {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        else:
            if concerto_number_of_soloist_choice == 1:
                combination = f'{concerto_variant_name}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # single soloist
            elif concerto_number_of_soloist_choice == 2:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # double soloists
            elif concerto_number_of_soloist_choice == 3:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # triple soloists
            elif concerto_number_of_soloist_choice == 4:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # quadruple soloists
            else:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(concerto_instrument_family_brass)["name"]}, {random.choice(concerto_instrument_family_keys)["name"]}, {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
  
        if len(combination) < 200:
            check_and_write_to_file('log/concerto_prompt_history.txt', 'concerto_prompt_history', "\n\nGenerated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:\n")
            print("Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:")
            break
        
    return combination

# Function to generate a random biblical song prompt less than 200 characters in string length
def bible_gateway_votd_concerto_song_custom():
    lyrics_prompt = ""
    style_of_music_prompt = ""
    
    # Remove while loop. Need to limit length of payload returned from end point first.
    # while True:
    concerto_variant_choice = random.choice(concerto_variants)
    concerto_variant_name = concerto_variant_choice['name']
    concerto_variant_ensemble = concerto_variant_choice['ensemble']
    vocalist_choice = random.choice(vocalists)

    # Use Bible Gateway Verse of the Day
    votds = get_bible_votd_kjv()
    print("Bible Verse Content: ", votds['votd']['content'])
    print("Bible Verse reference: ", votds['votd']['reference'])
    print("Bible Verse reference: ", votds['votd']['version'])
    biblecontent = votds['votd']['content']
    biblereference = votds['votd']['reference']
    biblereference_clean = biblereference.replace(":", "_")
    bibleversion = votds['votd']['version']
    verselink = votds['votd']['permalink']
    print(verselink)
        
    tempo_choice = random.choice(tempos)
    tempo_choice_int = random.randint(tempo_choice[1], tempo_choice[2])
    musical_key_choice = random.choice(musical_keys)

    timestamp = datetime.now()
    timestamp_str = timestamp.strftime('%Y%m%d_%H%M%S')
    timestamp_plus_1_sec = (timestamp + timedelta(seconds=1)).strftime('%Y%m%d_%H%M%S')

    yt_title_1 = f"VOTD {biblereference} {concerto_variant_name} {timestamp_str} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
    check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', yt_title_1)
    print(yt_title_1)
    print("")

    yt_title_2 = f"VOTD {biblereference} {concerto_variant_name} {timestamp_plus_1_sec} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
    check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', yt_title_2)
    print(yt_title_2)
    print("")

    suno_song_title_1 = f"VOTD {biblereference_clean} {concerto_variant_name} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_str}\n\n"
    suno_song_title_clean_1 = suno_song_title_1.replace(",", "")
    check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', suno_song_title_clean_1)
    print(suno_song_title_clean_1)
    print("")

    suno_song_title_2 = f"VOTD {biblereference_clean} {concerto_variant_name} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_plus_1_sec}\n\n"
    suno_song_title_clean_2 = suno_song_title_2.replace(",", "")
    check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', suno_song_title_clean_2)
    print(suno_song_title_clean_2)
    print("")
        
    yt_descr = f"Using AI to generate biblically accurate {concerto_variant_name} songs and music videos.\n\n"
    check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', yt_descr)
    print(yt_descr)
    print("")
        
    lyrics_prompt = f'Generate biblically accurate lyrics inspired by the message of {biblereference} quoting this verse verbatim taken from the {bibleversion} bible: {biblecontent}'
    
    if len(lyrics_prompt) > 399:
        lyrics_prompt = {biblecontent}
    
    if concerto_variant_ensemble == "Symphony":
        style_of_music_prompt = f'{concerto_variant_ensemble}, {vocalist_choice[0]} ({vocalist_choice[2]}), {concerto_instrument_family_woodwinds[0]["name"]}, {concerto_instrument_family_woodwinds[1]["name"]}, {concerto_instrument_family_woodwinds[2]["name"]}, {concerto_instrument_family_woodwinds[3]["name"]}, {concerto_instrument_family_woodwinds[4]["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
    elif concerto_variant_ensemble == "Baroque Ensemble":
        style_of_music_prompt = f'{concerto_variant_ensemble}, {vocalist_choice[0]} ({vocalist_choice[2]}), {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(concerto_instrument_family_brass)["name"]}, Harpsichord, {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
    elif concerto_variant_ensemble == "Baroque Orchestra":
        style_of_music_prompt = f'{concerto_variant_ensemble}, {vocalist_choice[0]} ({vocalist_choice[2]}), {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(["Trumpet","Horn"])}, {random.choice(["Organ","Harpsichord"])}, {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
    elif concerto_variant_ensemble == "Classical Orchestra":
        style_of_music_prompt = f'{concerto_variant_ensemble}, {vocalist_choice[0]} ({vocalist_choice[2]}), {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(concerto_instrument_family_brass)["name"]}, {random.choice(["Fortepiano","Harpsichord"])}, {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
    elif concerto_variant_ensemble == "Romantic Orchestra":
        style_of_music_prompt = f'{concerto_variant_ensemble}, {vocalist_choice[0]} ({vocalist_choice[2]}), {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(concerto_instrument_family_brass)["name"]}, {random.choice(["Piano","Organ"])}, {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
    elif concerto_variant_ensemble == "Variable":
        style_of_music_prompt = f'Concertante Works, {vocalist_choice[0]} ({vocalist_choice[2]}), {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(concerto_instrument_family_brass)["name"]}, {random.choice(concerto_instrument_family_keys)["name"]}, {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
    elif concerto_variant_ensemble == "Orchestral or Experimental":
        style_of_music_prompt = f'Orchestral, Experimental, {vocalist_choice[0]} ({vocalist_choice[2]}), {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(concerto_instrument_family_brass)["name"]}, {random.choice(concerto_instrument_family_keys)["name"]}, {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
    elif concerto_variant_ensemble == "Orchestral or Piano Accompaniment":
        style_of_music_prompt = f'Orchestral, {vocalist_choice[0]} ({vocalist_choice[2]}), {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(concerto_instrument_family_brass)["name"]}, {random.choice(concerto_instrument_family_keys)["name"]}, {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
    else:
        style_of_music_prompt = f'{concerto_variant_ensemble}, {vocalist_choice[0]} ({vocalist_choice[2]}), {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(concerto_instrument_family_brass)["name"]}, {random.choice(concerto_instrument_family_keys)["name"]}, {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        
    # if len(style_of_music_prompt) < 120 and len(lyrics_prompt) < 399:
    concat_prompts = f"Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:\n{style_of_music_prompt}\n\nLyrics Prompt:\n{lyrics_prompt}\n\n{bibleversion}\nPublic Domain\n\nPrompt generated using Verse of the Day (votd) endpoint provided by BibleGateway\n{verselink}"
            # break
            
    return concat_prompts

#generate exclude pop genres prompt and write to file
exclude_styles_pop_genres_prompt = f'\n\nExclude Styles:\n{exclude_pop_genres[0]}, {exclude_pop_genres[1]}, {exclude_pop_genres[2]}, {exclude_pop_genres[3]}, {exclude_pop_genres[4]}, {exclude_pop_genres[5]}, {exclude_pop_genres[6]}, {exclude_pop_genres[7]}, {exclude_pop_genres[8]}, {exclude_pop_genres[9]}, {exclude_pop_genres[10]}, {exclude_pop_genres[11]}, {exclude_pop_genres[12]}, {exclude_pop_genres[13]}, {exclude_pop_genres[14]}, {exclude_pop_genres[15]}, {exclude_pop_genres[16]}, {exclude_pop_genres[17]}, {exclude_pop_genres[18]}, {exclude_pop_genres[19]}'

#generate exclude anti percussion instruments prompt and write to file
exclude_styles_drum_prompt = f'\n\nExclude Styles:\n{anti_percussion_instruments[0]}, {anti_percussion_instruments[1]}, {anti_percussion_instruments[2]}, {anti_percussion_instruments[3]}, {anti_percussion_instruments[4]}, {anti_percussion_instruments[5]}, {anti_percussion_instruments[6]}, {anti_percussion_instruments[7]}, {anti_percussion_instruments[8]}, {anti_percussion_instruments[9]}, {anti_percussion_instruments[10]}, {anti_percussion_instruments[11]}, {anti_percussion_instruments[12]}, {anti_percussion_instruments[13]}'

new_prompt_div = "\n\n------------------------------New Prompt-------------------------------------\n"

check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', new_prompt_div)
print("\n------------------------------New Prompt-------------------------------------\n")
# Generate and print the generate_biblical_song_simple string
# print("Biblically inspired song prompt less than 200 characters in string length:")
bible_song_prompt = generate_biblical_song_simple()
check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', bible_song_prompt)
print(bible_song_prompt)
check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', exclude_styles_pop_genres_prompt)
print(exclude_styles_pop_genres_prompt)
check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', "\n\n Lyrics_Here")
print("\n Lyrics_Here")
check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', "\n\nOwnership and commercial use rights is retained for any songs generated by my self using Suno during active subscription, even after cancelling. Proof of ownership is available upon request. For more information, please reference Suno Knowledge Base Articles at https://help.suno.com/en/articles/2421505")

check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', new_prompt_div)
print("\n------------------------------New Prompt-------------------------------------\n")
# Generate and print the generate_biblical_song_simple string
# print("Biblically inspired song prompt less than 200 characters in string length:")
bible_song_prompt_custom = generate_biblical_song_custom()
check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history', bible_song_prompt_custom)
print(bible_song_prompt_custom)
check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history ', exclude_styles_pop_genres_prompt)
print(exclude_styles_pop_genres_prompt)
check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history ', "\n\n Lyrics_Here")
print("\n Lyrics_Here")
check_and_write_to_file('log/bible_song_prompt_history.txt', 'bible_song_prompt_history ', "\n\nOwnership and commercial use rights is retained for any songs generated by my self using Suno during active subscription, even after cancelling. Proof of ownership is available upon request. For more information, please reference Suno Knowledge Base Articles at https://help.suno.com/en/articles/2421505")

check_and_write_to_file('log/instrumental_song_prompt_history.txt', 'instrumental_song_prompt_history', new_prompt_div)
print("\n------------------------------New Prompt-------------------------------------\n")
# Generate and print the generate_instrumental_song_simple string
# print("Instrumental song prompt less than 200 characters in string length:")
instrumental_song_prompt = generate_instrumental_song_simple()
check_and_write_to_file('log/instrumental_song_prompt_history.txt', 'instrumental_song_prompt_history', instrumental_song_prompt)
print(instrumental_song_prompt)
check_and_write_to_file('log/instrumental_song_prompt_history.txt', 'instrumental_song_prompt_history', exclude_styles_pop_genres_prompt)
print(exclude_styles_pop_genres_prompt)
check_and_write_to_file('log/instrumental_song_prompt_history.txt', 'instrumental_song_prompt_history', "\n\n[Instrumental]")
print("\n[Instrumental]")
check_and_write_to_file('log/instrumental_song_prompt_history.txt', 'instrumental_song_prompt_history', "\n\nOwnership and commercial use rights is retained for any songs generated by my self using Suno during active subscription, even after cancelling. Proof of ownership is available upon request. For more information, please reference Suno Knowledge Base Articles at https://help.suno.com/en/articles/2421505")

check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', new_prompt_div)
print("\n------------------------------New Prompt-------------------------------------\n")
# Generate and print the generate_biblical_song_simple string
# print("Biblically inspired song prompt less than 200 characters in string length:")
bible_gateway_votd_song_prompt_custom = generate_bible_gateway_votd_song_custom()
check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', bible_gateway_votd_song_prompt_custom)
print(bible_gateway_votd_song_prompt_custom)
check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', exclude_styles_pop_genres_prompt)
print(exclude_styles_pop_genres_prompt)
check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', "\n\n Lyrics_Here")
print("\n Lyrics_Here")
check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', "\n\nOwnership and commercial use rights is retained for any songs generated by my self using Suno during active subscription, even after cancelling. Proof of ownership is available upon request. For more information, please reference Suno Knowledge Base Articles at https://help.suno.com/en/articles/2421505")

check_and_write_to_file('log/drum_loop_prompt_history.txt', 'drum_loop_prompt_history', new_prompt_div)
print("\n------------------------------New Prompt-------------------------------------\n")
# Generate and print the drum_loop_simple string
# print("Drum loop prompt less than 200 characters in string length:")
drum_loop_prompt = generate_drum_loop()
check_and_write_to_file('log/drum_loop_prompt_history.txt', 'drum_loop_prompt_history', drum_loop_prompt)
print(drum_loop_prompt)
check_and_write_to_file('log/drum_loop_prompt_history.txt', 'drum_loop_prompt_history', exclude_styles_drum_prompt)
print(exclude_styles_drum_prompt)
check_and_write_to_file('log/drum_loop_prompt_history.txt', 'drum_loop_prompt_history', "\n\n[Drum Loop]")
print("\n[Drum Loop]")
check_and_write_to_file('log/drum_loop_prompt_history.txt', 'drum_loop_prompt_history', "\n\nOwnership and commercial use rights is retained for any songs generated by my self using Suno during active subscription, even after cancelling. Proof of ownership is available upon request. For more information, please reference Suno Knowledge Base Articles at https://help.suno.com/en/articles/2421505")

check_and_write_to_file('log/concerto_prompt_history.txt', 'concerto_prompt_history', new_prompt_div)
print("\n------------------------------New Prompt-------------------------------------\n")
# Generate and print the generate_concerto_prompt string
# print("Concerto prompt less than 200 characters in string length:")
concerto_prompt = generate_concerto_prompt()
check_and_write_to_file('log/concerto_prompt_history.txt', 'concerto_prompt_history', concerto_prompt)
print(concerto_prompt)
check_and_write_to_file('log/concerto_prompt_history.txt', 'concerto_prompt_history', exclude_styles_pop_genres_prompt)
print(exclude_styles_pop_genres_prompt)
check_and_write_to_file('log/concerto_prompt_history.txt', 'concerto_prompt_history', "\n\n[Concerto]")
print("\n[Concerto]")
check_and_write_to_file('log/concerto_prompt_history.txt', 'concerto_prompt_history', "\n\nOwnership and commercial use rights is retained for any songs generated by my self using Suno during active subscription, even after cancelling. Proof of ownership is available upon request. For more information, please reference Suno Knowledge Base Articles at https://help.suno.com/en/articles/2421505")

check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', new_prompt_div)
print("\n------------------------------New Prompt-------------------------------------\n")
# Generate and print the generate_concerto_prompt string
bible_gateway_votd_concerto_song_prompt = bible_gateway_votd_concerto_song_custom()
check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', bible_gateway_votd_concerto_song_prompt)
print(bible_gateway_votd_concerto_song_prompt)
check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', exclude_styles_pop_genres_prompt)
print(exclude_styles_pop_genres_prompt)
check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', "\n\n Lyrics_Here")
print("\n Lyrics_Here")
check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', "\n\n[Concerto]")
print("\n[Concerto]")
check_and_write_to_file('log/votd_bible_song_prompt_history.txt', 'votd_bible_song_prompt_history', "\n\nOwnership and commercial use rights is retained for any songs generated by my self using Suno during active subscription, even after cancelling. Proof of ownership is available upon request. For more information, please reference Suno Knowledge Base Articles at https://help.suno.com/en/articles/2421505")