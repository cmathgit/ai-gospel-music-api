import json
import random
from datetime import datetime
from datetime import timedelta
from biblegateway_api import get_bible_votd_kjv #, get_bible_votd_amp, get_bible_votd_msg
from write_to_file import check_and_write_to_file

# This file generates prompts for the Suno AI API using bible verses taken from the King James Version of the Bible verbatim to be used as lyrics. This is for custom prompts only.

# Load Bible-kjv library
with open('Bible-kjv/Books.json') as f:
    bible_books = json.load(f)

# choose a random bible book
bible_book_choice = random.choice(bible_books)

# Add space if book name starts with digit
book_name = bible_book_choice[0]
if book_name[0].isdigit():
    book_name = book_name[0] + " " + book_name[1:]
    print(f"{book_name}")

# choose a random chapter from the chosen bible book
bible_chapter_choice = random.randint(1, bible_book_choice[1])
print(f"{bible_book_choice[0]} {bible_chapter_choice}")

# Load bible book and verses
with open(f'Bible-kjv/{bible_book_choice[0]}.json') as f:
    bible_verses = json.load(f)

# Select the chosen chapter
bible_verses_chapter = bible_verses["chapters"][bible_chapter_choice - 1]

# Get all verses for the chapter
verses = bible_verses_chapter["verses"]

# Initialize empty string to store all verses
chapter_text = ""

# Loop through all verses and concatenate their text
for verse in verses:
    chapter_text += verse["text"] + " "  # Add space between verses

# Remove trailing space
chapter_text = chapter_text.strip()

# Load data from JSON files
with open('lib/tempo_dict.json') as f:
    tempos = json.load(f)

with open('lib/music_key_dict.json') as f:
    musical_keys = json.load(f)

with open('lib/instrument_dict.json') as f:
    instruments = json.load(f)

with open('lib/vocalists_dict.json') as f:
    vocalists = json.load(f)

with open('lib/song_genre_dict.json') as f:
    song_genre = json.load(f)
    
with open('lib/bible_song_genre_dict.json') as f:
    bible_song_genre = json.load(f)

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
def generate_biblical_song_verbatim_custom():
    lyrics_prompt = ""
    style_of_music_prompt = ""
    #while True:
    song_genre_choice = random.choice(bible_song_genre)
    vocalist_choice = random.choice(vocalists)
    instrument_choice_1 = random.choice(instruments)
    instrument_choice_2 = random.choice(instruments)
    instrument_choice_3 = random.choice(instruments)
    tempo_choice = random.choice(tempos)
    tempo_choice_int = random.randint(tempo_choice[1], tempo_choice[2])
    musical_key_choice = random.choice(musical_keys)

    timestamp = datetime.now()
    timestamp_str = timestamp.strftime('%Y%m%d_%H%M%S')
    timestamp_plus_1_sec = (timestamp + timedelta(seconds=1)).strftime('%Y%m%d_%H%M%S')
    yt_title_1 = f"VERBATIM {book_name} {bible_chapter_choice} {song_genre_choice[0]} {timestamp_str} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
    check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', yt_title_1)
    print(yt_title_1)
    print("")
        
    yt_title_2 = f"VERBATIM {book_name} {bible_chapter_choice} {song_genre_choice[0]} {timestamp_plus_1_sec} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
    check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', yt_title_2)
    print(yt_title_2)
    print("")
        
    suno_song_title_1 = f"VERBATIM {book_name} {bible_chapter_choice} {song_genre_choice[0]} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_str}\n\n"
    suno_song_title_clean_1 = suno_song_title_1.replace(",", "")
    check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', suno_song_title_clean_1)
    print(suno_song_title_clean_1)
    print("")
        
    suno_song_title_2 = f"VERBATIM {book_name} {bible_chapter_choice} {song_genre_choice[0]} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_plus_1_sec}\n\n"
    suno_song_title_clean_2 = suno_song_title_2.replace(",", "")
    check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', suno_song_title_clean_2)
    print(suno_song_title_clean_2)
    print("")

    yt_descr = f"Using AI to generate {song_genre_choice[0]} songs and music videos with lyrics taken from the book of {bible_book_choice[0]} chapter {bible_chapter_choice} of The Holy Bible: King James Version verbatim.\n\n"
    check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', yt_descr)
    print(yt_descr)
    print("")
        
    lyrics_prompt = f'{chapter_text}\n\nKing James Version\nPublic Domain'
        
    style_of_music_prompt = f'{song_genre_choice[0]}, {vocalist_choice[0]} ({vocalist_choice[2]}), {instrument_choice_1}, {instrument_choice_2}, {instrument_choice_3}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        
    # if len(style_of_music_prompt) < 200 and len(lyrics_prompt) < 2999:
    concat_prompts = f"Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:\n{style_of_music_prompt}\n\nLyrics Prompt:\n{lyrics_prompt}\n"
    #break
    
    return concat_prompts
    
# Function to generate a random biblical song prompt less than 200 characters in string length
def bible_concerto_kjv_verbatim_custom():
    lyrics_prompt = ""
    style_of_music_prompt = ""
    
    # Remove while loop. Need to limit length of payload returned from end point first.
    # while True:
    concerto_variant_choice = random.choice(concerto_variants)
    concerto_variant_name = concerto_variant_choice['name']
    concerto_variant_ensemble = concerto_variant_choice['ensemble']
    vocalist_choice = random.choice(vocalists)

    tempo_choice = random.choice(tempos)
    tempo_choice_int = random.randint(tempo_choice[1], tempo_choice[2])
    musical_key_choice = random.choice(musical_keys)

    timestamp = datetime.now()
    timestamp_str = timestamp.strftime('%Y%m%d_%H%M%S')
    timestamp_plus_1_sec = (timestamp + timedelta(seconds=1)).strftime('%Y%m%d_%H%M%S')

    yt_title_1 = f"VERBATIM {book_name} {bible_chapter_choice} {concerto_variant_name} {timestamp_str} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
    check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', yt_title_1)
    print(yt_title_1)
    print("")

    yt_title_2 = f"VERBATIM {book_name} {bible_chapter_choice} {concerto_variant_name} {timestamp_plus_1_sec} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
    check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', yt_title_2)
    print(yt_title_2)
    print("")

    suno_song_title_1 = f"VERBATIM {book_name} {bible_chapter_choice} {concerto_variant_name} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_str}\n\n"
    suno_song_title_clean_1 = suno_song_title_1.replace(",", "")
    check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', suno_song_title_clean_1)
    print(suno_song_title_clean_1)
    print("")

    suno_song_title_2 = f"VERBATIM {book_name} {bible_chapter_choice} {concerto_variant_name} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_plus_1_sec}\n\n"
    suno_song_title_clean_2 = suno_song_title_2.replace(",", "")
    check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', suno_song_title_clean_2)
    print(suno_song_title_clean_2)
    print("")
        
    yt_descr = f"Using AI to generate {concerto_variant_name} songs and music videos with lyrics taken from the book of {bible_book_choice[0]} chapter {bible_chapter_choice} of The Holy Bible: King James Version verbatim.\n\n"
    check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', yt_descr)
    print(yt_descr)
    print("")
        
    lyrics_prompt = f'{chapter_text}\n\nKing James Version\nPublic Domain'
     
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
    concat_prompts = f"Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:\n{style_of_music_prompt}\n\nLyrics Prompt:\n{lyrics_prompt}\n\n"
            # break
            
    return concat_prompts

#generate exclude pop genres prompt and write to file
exclude_styles_pop_genres_prompt = f'\nExclude Styles:\n{exclude_pop_genres[0]}, {exclude_pop_genres[1]}, {exclude_pop_genres[2]}, {exclude_pop_genres[3]}, {exclude_pop_genres[4]}, {exclude_pop_genres[5]}, {exclude_pop_genres[6]}, {exclude_pop_genres[7]}, {exclude_pop_genres[8]}, {exclude_pop_genres[9]}'

new_prompt_div = "\n\n------------------------------New Prompt-------------------------------------\n"

# Generate and print the generate_biblical_song_verbatim_custom string
# print("Biblically inspired song prompt less than 200 characters in string length:")
check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', new_prompt_div)
print(new_prompt_div)
bible_song_prompt_custom = generate_biblical_song_verbatim_custom()
check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', bible_song_prompt_custom)
print(bible_song_prompt_custom)
check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history ', exclude_styles_pop_genres_prompt)
print(exclude_styles_pop_genres_prompt)
check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history ', "\n\n Lyrics_Here")
print("\n Lyrics_Here")
check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history ', "\n\nOwnership and commercial use rights is retained for any songs generated by my self using Suno during active subscription, even after cancelling. Proof of ownership is available upon request. For more information, please reference Suno Knowledge Base Articles at https://help.suno.com/en/articles/2421505")

# Generate and print the bible_gateway_concerto_verbatim_custom string
check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', new_prompt_div)
print(new_prompt_div)
bible_gateway_concerto_verbatim_prompt = bible_concerto_kjv_verbatim_custom()
check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', bible_gateway_concerto_verbatim_prompt)
print(bible_gateway_concerto_verbatim_prompt)
check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', exclude_styles_pop_genres_prompt)
print(exclude_styles_pop_genres_prompt)
check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', "\n\n Lyrics_Here")
print("\n Lyrics_Here")
check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', "\n\n[Concerto]")
print("\n[Concerto]")
check_and_write_to_file('log/verbatim_kjv_prompt_history.txt', 'verbatim_kjv_prompt_history', "\n\nOwnership and commercial use rights is retained for any songs generated by my self using Suno during active subscription, even after cancelling. Proof of ownership is available upon request. For more information, please reference Suno Knowledge Base Articles at https://help.suno.com/en/articles/2421505")