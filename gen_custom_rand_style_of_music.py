import json
import random
import getpass
import os
import controlflow as cf
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Get api key from the environment variable
api_key = os.getenv('GOOGLE_API_KEY')

# Ensure your Google AI API key is configured
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")
    
# Get the model from the environment variable
model = os.getenv('MODEL_NAME')

# set the default model
cf.defaults.model = ChatGoogleGenerativeAI(
    model=model, 
    temperature=0.3,
)

# Get controlflow context from the environment variable
controlflow_context = os.getenv('CONTROL_FLOW_CONTEXT_STYLES')
controlflow_context_concise = os.getenv('CONTROL_FLOW_CONTEXT_CONCISE_STYLES')

base_lib_file_path = 'datasets/'

def get_random_style_of_music_elements():
    # Load data from JSON files
    with open(f'{base_lib_file_path}tempos.json') as f:
        tempos = json.load(f)

    with open(f'{base_lib_file_path}music_keys.json') as f:
        musical_keys = json.load(f)

    with open(f'{base_lib_file_path}instruments.json') as f:
        instruments = json.load(f)

    with open(f'{base_lib_file_path}vocalists.json') as f:
        vocalists = json.load(f)

    with open(f'{base_lib_file_path}adjectives.json') as f:
        adjectives = json.load(f)

    with open(f'{base_lib_file_path}song_genres.json') as f:
        song_genre = json.load(f)
    
    with open(f'{base_lib_file_path}drum_loop_genres_dict.json') as f:
        drum_loop_genre = json.load(f)

    with open(f'{base_lib_file_path}drum_kits_dict.json') as f:
        drum_kits = json.load(f)

    with open(f'{base_lib_file_path}percussion_instruments_dict.json') as f:
        percussion_instruments = json.load(f)

    with open(f'{base_lib_file_path}anti_percussion_instruments_dict.json') as f:
        anti_percussion_instruments = json.load(f)

    with open(f'{base_lib_file_path}exclude_pop_genres_dict.json') as f:
        exclude_pop_genres = json.load(f)

    with open(f'{base_lib_file_path}concerto_variants_dict.json') as f:
        concerto_variants = json.load(f)

    with open(f'{base_lib_file_path}concerto_instrument_family_woodwinds_dict.json') as f:
        concerto_instrument_family_woodwinds = json.load(f)

    with open(f'{base_lib_file_path}concerto_instrument_family_brass_dict.json') as f:
        concerto_instrument_family_brass = json.load(f) 

    with open(f'{base_lib_file_path}concerto_instrument_family_percussion_dict.json') as f:
        concerto_instrument_family_percussion = json.load(f)

    with open(f'{base_lib_file_path}concerto_instrument_family_string_dict.json') as f:
        concerto_instrument_family_strings = json.load(f)

    with open(f'{base_lib_file_path}concerto_instrument_family_keys_dict.json') as f:
        concerto_instrument_family_keys = json.load(f)

    return tempos, musical_keys, instruments, vocalists, adjectives, song_genre, drum_loop_genre, drum_kits, percussion_instruments, anti_percussion_instruments, exclude_pop_genres, concerto_variants, concerto_instrument_family_woodwinds, concerto_instrument_family_brass, concerto_instrument_family_percussion, concerto_instrument_family_strings, concerto_instrument_family_keys

def revise_prompt_with_control_flow(combo=""):
    combination_revised = ""

    combination_revised = cf.run(
        controlflow_context,
        context=dict(prompt=combo),
    )

    return combination_revised

def shorten_prompt_with_control_flow(combo=""):
    combination_revised = ""

    combination_revised = cf.run(
        controlflow_context_concise,
        context=dict(prompt=combo),
    )

    return combination_revised

def generate_custom_exclude_styles_prompt(exclude_pop_genres):
    #generate exclude pop genres prompt and write to file
    exclude_styles_pop_genres_prompt = f'{exclude_pop_genres[0]}, {exclude_pop_genres[1]}, {exclude_pop_genres[2]}, {exclude_pop_genres[3]}, {exclude_pop_genres[4]}, {exclude_pop_genres[5]}, {exclude_pop_genres[6]}, {exclude_pop_genres[7]}, {exclude_pop_genres[8]}, {exclude_pop_genres[9]}, {exclude_pop_genres[10]}, {exclude_pop_genres[11]}, {exclude_pop_genres[12]}, {exclude_pop_genres[13]}, {exclude_pop_genres[14]}, {exclude_pop_genres[15]}, {exclude_pop_genres[16]}, {exclude_pop_genres[17]}, {exclude_pop_genres[18]}, {exclude_pop_genres[19]}'

    return exclude_styles_pop_genres_prompt

def generate_custom_exclude_drum_prompt(anti_percussion_instruments):
    #generate exclude anti percussion instruments prompt and write to file
    exclude_styles_drum_prompt = f'{anti_percussion_instruments[0]}, {anti_percussion_instruments[1]}, {anti_percussion_instruments[2]}, {anti_percussion_instruments[3]}, {anti_percussion_instruments[4]}, {anti_percussion_instruments[5]}, {anti_percussion_instruments[6]}, {anti_percussion_instruments[7]}, {anti_percussion_instruments[8]}, {anti_percussion_instruments[9]}, {anti_percussion_instruments[10]}, {anti_percussion_instruments[11]}, {anti_percussion_instruments[12]}, {anti_percussion_instruments[13]}'

    return exclude_styles_drum_prompt

def generate_custom_random_style_of_music_prompt(instrumental=True):
    revised_combination = ""
    combination = ""
    exclude_styles_pop_genres_prompt =""

    tempos, musical_keys, instruments, vocalists, adjectives, song_genre, drum_loop_genre, drum_kits, percussion_instruments, anti_percussion_instruments, exclude_pop_genres, concerto_variants, concerto_instrument_family_woodwinds, concerto_instrument_family_brass, concerto_instrument_family_percussion, concerto_instrument_family_strings, concerto_instrument_family_keys = get_random_style_of_music_elements()

    while True:
        song_genre_choice = random.choice(song_genre)
        instrument_choice_1 = random.choice(instruments)
        instrument_choice_2 = random.choice(instruments)
        instrument_choice_3 = random.choice(instruments)
        instrument_choice_4 = random.choice(instruments)
        tempo_choice = random.choice(tempos)
        tempo_choice_int = random.randint(tempo_choice[1], tempo_choice[2])
        musical_key_choice = random.choice(musical_keys)

        if instrumental:
            combination = f'{song_genre_choice}, {random.choice(adjectives)} {instrument_choice_1}, {random.choice(adjectives)} {instrument_choice_2}, {random.choice(adjectives)} {instrument_choice_3}, {random.choice(adjectives)} {instrument_choice_4}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        else:
            vocalist_choice = random.choice(vocalists)
            combination = f'{song_genre_choice}, {vocalist_choice[0]} ({vocalist_choice[2]}), {random.choice(adjectives)} {instrument_choice_1}, {random.choice(adjectives)} {instrument_choice_2}, {random.choice(adjectives)} {instrument_choice_3}, {random.choice(adjectives)} {instrument_choice_4}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        
        if len(combination) < 200:
            # exit the loop
            break
    
    revised_combination = revise_prompt_with_control_flow(combination)
    exclude_styles_pop_genres_prompt = generate_custom_exclude_styles_prompt(exclude_pop_genres)

    return revised_combination, combination, exclude_styles_pop_genres_prompt
    
def generate_custom_random_drum_loop_prompt():
    # drum loops are always instrumentals
    revised_combination = ""
    combination = ""
    exclude_styles_drum_prompt =""

    tempos, musical_keys, instruments, vocalists, adjectives, song_genre, drum_loop_genre, drum_kits, percussion_instruments, anti_percussion_instruments, exclude_pop_genres, concerto_variants, concerto_instrument_family_woodwinds, concerto_instrument_family_brass, concerto_instrument_family_percussion, concerto_instrument_family_strings, concerto_instrument_family_keys = get_random_style_of_music_elements()

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
        
        combination = f'{drum_loop_genre_choice[0]}, {drum_kit_choice[0]}, {drum_kit_choice[1]}, {drum_kit_choice[2]}, {drum_kit_choice[3]}, {drum_kit_choice[4]}, {random.choice(adjectives)} {percussion_instrument_choice_1[0]}, {random.choice(adjectives)} {percussion_instrument_choice_2[0]}, {random.choice(adjectives)} {percussion_instrument_choice_3[0]}, {random.choice(adjectives)} {percussion_instrument_choice_4[0]}, {style_choice}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        
        if len(combination) < 200:
            # exit the loop
            break

    revised_combination = revise_prompt_with_control_flow(combination)
    exclude_styles_drum_prompt = generate_custom_exclude_drum_prompt(anti_percussion_instruments)
    
    return revised_combination, combination, exclude_styles_drum_prompt

def generate_custom_random_concerto_prompt():
    revised_combination = ""
    combination = ""
    exclude_styles_pop_genres_prompt =""

    tempos, musical_keys, instruments, vocalists, adjectives, song_genre, drum_loop_genre, drum_kits, percussion_instruments, anti_percussion_instruments, exclude_pop_genres, concerto_variants, concerto_instrument_family_woodwinds, concerto_instrument_family_brass, concerto_instrument_family_percussion, concerto_instrument_family_strings, concerto_instrument_family_keys = get_random_style_of_music_elements()
    while True:
        concerto_variant_choice = random.choice(concerto_variants)
        concerto_variant_name = concerto_variant_choice['name']
        concerto_variant_number_of_soloists = concerto_variant_choice['soloists']
        concerto_variant_ensemble = concerto_variant_choice['ensemble']
        #concerto_variant_description = concerto_variant_choice['description']
        tempo_choice = random.choice(tempos)
        tempo_choice_int = random.randint(tempo_choice[1], tempo_choice[2])
        musical_key_choice = random.choice(musical_keys)
        
        if concerto_variant_number_of_soloists < 4:
            concerto_number_of_soloist_choice = concerto_variant_number_of_soloists
        else:
            concerto_number_of_soloist_choice = random.randint(2, concerto_variant_number_of_soloists)

        if concerto_variant_ensemble == "Symphony":
            if concerto_number_of_soloist_choice == 1:
                combination = f'{concerto_variant_name},  {random.choice(adjectives)} {random.choice(concerto_instrument_family_woodwinds)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # single soloist
            elif concerto_number_of_soloist_choice == 2:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_woodwinds)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # double soloists
            elif concerto_number_of_soloist_choice == 3:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_woodwinds)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # triple soloists
            elif concerto_number_of_soloist_choice == 4:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_woodwinds)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # quadruple soloists
            else:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {concerto_instrument_family_woodwinds[0]["name"]}, {random.choice(adjectives)} {concerto_instrument_family_woodwinds[1]["name"]}, {random.choice(adjectives)} {concerto_instrument_family_woodwinds[2]["name"]}, {random.choice(adjectives)} {concerto_instrument_family_woodwinds[3]["name"]}, {random.choice(adjectives)} {concerto_instrument_family_woodwinds[4]["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        elif concerto_variant_ensemble == "Baroque Ensemble":
            if concerto_number_of_soloist_choice == 1:
                combination = f'{concerto_variant_name}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # single soloist
            elif concerto_number_of_soloist_choice == 2:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # double soloists
            elif concerto_number_of_soloist_choice == 3:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # triple soloists
            elif concerto_number_of_soloist_choice == 4:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],"Harpsichord"])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # quadruple soloists
            else:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_strings)["name"]}, Harpsichord, {random.choice(adjectives)} {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        elif concerto_variant_ensemble == "Baroque Orchestra":
            if concerto_number_of_soloist_choice == 1:
                combination = f'{concerto_variant_name}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # single soloist
            elif concerto_number_of_soloist_choice == 2:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # double soloists
            elif concerto_number_of_soloist_choice == 3:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # triple soloists
            elif concerto_number_of_soloist_choice == 4:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(["Trumpet","Horn"]),random.choice(["Harpsichord","Organ"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # quadruple soloists
            else:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(["Trumpet","Horn"])}, {random.choice(adjectives)} {random.choice(["Harpsichord","Organ"])}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        elif concerto_variant_ensemble == "Classical Orchestra":
            if concerto_number_of_soloist_choice == 1:
                combination = f'{concerto_variant_name}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # single soloist
            elif concerto_number_of_soloist_choice == 2:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # double soloists
            elif concerto_number_of_soloist_choice == 3:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # triple soloists
            elif concerto_number_of_soloist_choice == 4:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Harpsichord","Fortepiano"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # quadruple soloists
            else:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_brass)["name"]}, {random.choice(adjectives)} {random.choice(["Harpsichord","Fortepiano"])}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        elif concerto_variant_ensemble == "Romantic Orchestra":
            if concerto_number_of_soloist_choice == 1:
                combination = f'{concerto_variant_name}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # single soloist
            elif concerto_number_of_soloist_choice == 2:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # double soloists
            elif concerto_number_of_soloist_choice == 3:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # triple soloists
            elif concerto_number_of_soloist_choice == 4:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(["Organ","Piano"])])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # quadruple soloists
            else:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(concerto_instrument_family_brass)["name"]}, {random.choice(adjectives)} {random.choice(["Piano","Organ"])}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
        else:
            if concerto_number_of_soloist_choice == 1:
                combination = f'{concerto_variant_name}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # single soloist
            elif concerto_number_of_soloist_choice == 2:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # double soloists
            elif concerto_number_of_soloist_choice == 3:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # triple soloists
            elif concerto_number_of_soloist_choice == 4:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {random.choice(adjectives)} {random.choice([random.choice(concerto_instrument_family_woodwinds)["name"],random.choice(concerto_instrument_family_strings)["name"],random.choice(concerto_instrument_family_percussion)["name"],random.choice(concerto_instrument_family_brass)["name"],random.choice(concerto_instrument_family_keys)["name"]])}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}' # quadruple soloists
            else:
                combination = f'{concerto_variant_name}, {concerto_variant_ensemble}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_woodwinds)["name"]}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_strings)["name"]}, {random.choice(concerto_instrument_family_brass)["name"]}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_keys)["name"]}, {random.choice(adjectives)} {random.choice(concerto_instrument_family_percussion)["name"]}, {tempo_choice[0]} {tempo_choice_int} bpm, {musical_key_choice[0]}'
  
        if len(combination) < 200:
            # exit the loop
            break
        
    revised_combination = revise_prompt_with_control_flow(combination)
    exclude_styles_pop_genres_prompt = generate_custom_exclude_styles_prompt(exclude_pop_genres)

    return revised_combination, combination, exclude_styles_pop_genres_prompt


# test the functions
'''
revised_combination_6, combination_6, exclude_styles_pop_genres_prompt_6 = generate_custom_random_style_of_music_prompt()
original_prompt_6 = combination_6
revised_prompt_6 = revised_combination_6
print("Original Prompt: ", original_prompt_6)
print("Revised Prompt: ", revised_prompt_6)

original_prompt_7="Freestyle EDM, crisp triangle, simmering clarinet, rich basslines Harmonium, tingling french horn, Andante 90 bpm, B Locrian"
revised_prompt_7=revise_prompt_with_control_flow(original_prompt_7)
print("Compare Revised Prompt using ControlFlow with Original Prompt which is a random combination from the library values. Notice how the adjectives make more sense than the random selected adjectives.")
print("Original Prompt: ", original_prompt_7)
print("Revised Prompt: ", revised_prompt_7)

original_prompt_8="A polished fusion of aggressive alt-metal guitar riffs and crisp, punchy hip-hop-inspired beats, wrapped in a sleek, cinematic production. The vocals oscillate between raw, emotional screams and introspective, melodic hooks, often contrasted with rhythmic, spoken-word verses. Electronic textures — glitchy samples, ambient pads, and industrial accents — weave through the mix, enhancing the atmosphere with a sense of digital tension and inner conflict. Lyrics deal with alienation, self-doubt, and emotional resilience, delivered with anthemic intensity. Every track feels like a cathartic release — heavy yet accessible, with explosive choruses designed to hit both heart and gut."
revised_prompt_8=shorten_prompt_with_control_flow(original_prompt_8)
print("Compare Revised Prompt using ControlFlow with Original Prompt which is a random combination from the library values. Notice how the adjectives make more sense than the random selected adjectives.")
print("Original Prompt: ", original_prompt_8)
print("Revised Prompt: ", revised_prompt_8)
'''
