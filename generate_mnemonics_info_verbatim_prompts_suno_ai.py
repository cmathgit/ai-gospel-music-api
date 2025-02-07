import json
import random
from datetime import datetime
from datetime import timedelta
from write_to_file import check_and_write_to_file

# This file generates prompts for the Suno AI API using information verbatim to be used as lyrics to serve as mnemonic device. This is for custom prompts only.

# Load topics in Mathematics library
#with open('lib/math_topics.json') as f:
#    math_topics = json.load(f)

# choose a random math topic
#math_topic_choice = random.choice(math_topics)
#print(f"{math_topic_choice}")

# load topics in Computer Science library
#with open('lib/cs_topics.json') as f:
#    cs_topics = json.load(f)

# choose a random computer science topic
#cs_topic_choice = random.choice(cs_topics)
#print(f"{cs_topic_choice}")

# load topics in Cybersecurity library
#with open('lib/cybersecurity_topics.json') as f:
#    cybersecurity_topics = json.load(f)

# choose a random cybersecurity topic
#cybersecurity_topic_choice = random.choice(cybersecurity_topics)
#print(f"{cybersecurity_topic_choice}")

# choose a random topic from the three topics
#topic_choice = random.choice([math_topic_choice, cs_topic_choice, cybersecurity_topic_choice])
#print(f"{topic_choice}")

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

with open('lib/instrumental_song_genre_dict.json') as f:
    instrumental_song_genre = json.load(f)

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

# Function to generate a random mnemonic song prompt less than 200 characters in string length
def generate_mnemonic_song_verbatim_custom():
    lyrics_prompt = ""
    style_of_music_prompt = ""
    topic_choice_fill_in = "PASTEYOURTOPICHERE"
    lyrics_fill_in = "PASTEYOURINFORMATIONTOBEUSEDASLYRICSHERE"
    #while True:
    song_genre_choice = random.choice(song_genre)
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
    yt_title_1 = f"INFO VERBATIM {topic_choice_fill_in} {song_genre_choice[0]} {timestamp_str} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
    check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', yt_title_1)
    print(yt_title_1)
    print("")
        
    yt_title_2 = f"INFO VERBATIM {topic_choice_fill_in} {song_genre_choice[0]} {timestamp_plus_1_sec} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
    check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', yt_title_2)
    print(yt_title_2)
    print("")
        
    suno_song_title_1 = f"INFO VERBATIM {topic_choice_fill_in} {song_genre_choice[0]} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_str}\n\n"
    suno_song_title_clean_1 = suno_song_title_1.replace(",", "")
    check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', suno_song_title_clean_1)
    print(suno_song_title_clean_1)
    print("")
        
    suno_song_title_2 = f"INFO VERBATIM {topic_choice_fill_in} {song_genre_choice[0]} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_plus_1_sec}\n\n"
    suno_song_title_clean_2 = suno_song_title_2.replace(",", "")
    check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', suno_song_title_clean_2)
    print(suno_song_title_clean_2)
    print("")

    # YouTube description
    #yt_descr_temp = "The AI-Assisted Memory Mix. Using AI to commit information to memory via song. When we were kids, we learned many things through song, e.g., ABCs. I realized how effective this was back in 2015 as a mathematics tutor. I would freestyle MC to beats reading definitions before an exam which helped me commit the information to memory."
    yt_descr = f"Using AI to commit [{topic_choice_fill_in}] information to memory via song. When we were kids, we learned many things through song, e.g., ABCs.\n\n"
    check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', yt_descr)
    print(yt_descr)
    print("")
        
    lyrics_prompt = f'{lyrics_fill_in}'
        
    style_of_music_prompt = f'{song_genre_choice[0]}, {vocalist_choice[0]} ({vocalist_choice[2]}), {instrument_choice_1}, {instrument_choice_2}, {instrument_choice_3}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        
    # if len(style_of_music_prompt) < 200 and len(lyrics_prompt) < 2999:
    concat_prompts = f"Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:\n{style_of_music_prompt}\n\nLyrics Source:\n\nLyrics Prompt:\n{lyrics_prompt}\n"
    #break
    
    return concat_prompts
    
# Function to generate a random mnemonic song prompt less than 200 characters in string length
def mnemonic_concerto_song_verbatim_custom():
    lyrics_prompt = ""
    style_of_music_prompt = ""
    topic_choice_fill_in = "PASTEYOURTOPICHERE"
    lyrics_fill_in = "PASTEYOURINFORMATIONTOBEUSEDASLYRICSHERE"
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

    yt_title_1 = f"INFO VERBATIM {topic_choice_fill_in} {concerto_variant_name} {timestamp_str} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
    check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', yt_title_1)
    print(yt_title_1)
    print("")

    yt_title_2 = f"INFO VERBATIM {topic_choice_fill_in} {concerto_variant_name} {timestamp_plus_1_sec} [{musical_key_choice[0]}] [{tempo_choice[0]}] [AI Music]\n\n"
    check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', yt_title_2)
    print(yt_title_2)
    print("")

    suno_song_title_1 = f"INFO VERBATIM {topic_choice_fill_in} {concerto_variant_name} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_str}\n\n"
    suno_song_title_clean_1 = suno_song_title_1.replace(",", "")
    check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', suno_song_title_clean_1)
    print(suno_song_title_clean_1)
    print("")

    suno_song_title_2 = f"INFO VERBATIM {topic_choice_fill_in} {concerto_variant_name} {tempo_choice[0]} {tempo_choice_int} {musical_key_choice[0]} {timestamp_plus_1_sec}\n\n"
    suno_song_title_clean_2 = suno_song_title_2.replace(",", "")
    check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', suno_song_title_clean_2)
    print(suno_song_title_clean_2)
    print("")
        
    yt_descr = f"Using AI to commit [{topic_choice_fill_in}] information to memory via song. When we were kids, we learned many things through song, e.g., ABCs.\n\n"
    check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', yt_descr)
    print(yt_descr)
    print("")
        
    lyrics_prompt = f'{lyrics_fill_in}'
     
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
    concat_prompts = f"Generated using Suno AI\n Suno_Link_Here\n\nStyle of Music Prompt:\n{style_of_music_prompt}\n\nLyrics Source:\n\nLyrics Prompt:\n{lyrics_prompt}\n\n"
            # break
            
    return concat_prompts

#generate exclude pop genres prompt and write to file
exclude_styles_pop_genres_prompt = f'\n\nExclude Styles:\n{exclude_pop_genres[0]}, {exclude_pop_genres[1]}, {exclude_pop_genres[2]}, {exclude_pop_genres[3]}, {exclude_pop_genres[4]}, {exclude_pop_genres[5]}, {exclude_pop_genres[6]}, {exclude_pop_genres[7]}, {exclude_pop_genres[8]}, {exclude_pop_genres[9]}, {exclude_pop_genres[10]}, {exclude_pop_genres[11]}, {exclude_pop_genres[12]}, {exclude_pop_genres[13]}, {exclude_pop_genres[14]}, {exclude_pop_genres[15]}, {exclude_pop_genres[16]}, {exclude_pop_genres[17]}, {exclude_pop_genres[18]}, {exclude_pop_genres[19]}'

new_prompt_div = "\n\n------------------------------New Prompt-------------------------------------\n"

# Generate and print the generate_mnemonic_song_verbatim_custom string
# print("Biblically inspired song prompt less than 200 characters in string length:")
check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', new_prompt_div)
print(new_prompt_div)
mnemonic_song_prompt_custom = generate_mnemonic_song_verbatim_custom()
check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', mnemonic_song_prompt_custom)
print(mnemonic_song_prompt_custom)
check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', exclude_styles_pop_genres_prompt)
print(exclude_styles_pop_genres_prompt)
check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', "\n\nOwnership and commercial use rights is retained for any songs generated by my self using Suno during active subscription, even after cancelling. Proof of ownership is available upon request. For more information, please reference Suno Knowledge Base Articles at https://help.suno.com/en/articles/2421505")

# Generate and print the mnemonic_concerto_song_verbatim_custom string
check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', new_prompt_div)
print(new_prompt_div)
mnemonic_concerto_song_verbatim_prompt = mnemonic_concerto_song_verbatim_custom()
check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', mnemonic_concerto_song_verbatim_prompt)
print(mnemonic_concerto_song_verbatim_prompt)
check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', exclude_styles_pop_genres_prompt)
print(exclude_styles_pop_genres_prompt)
check_and_write_to_file('log/verbatim_info_prompt_history.txt', 'verbatim_info_prompt_history', "\n\nOwnership and commercial use rights is retained for any songs generated by my self using Suno during active subscription, even after cancelling. Proof of ownership is available upon request. For more information, please reference Suno Knowledge Base Articles at https://help.suno.com/en/articles/2421505")
