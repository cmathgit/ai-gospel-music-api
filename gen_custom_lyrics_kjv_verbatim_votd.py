import json
import random
import getpass
import os
from biblegateway_api import get_bible_votd_kjv #, get_bible_votd_amp, get_bible_votd_msg
import controlflow as cf
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# This file generates prompts for the Suno AI API using bible verses taken from the King James Version of the Bible verbatim to be used as lyrics or using Bible Gateway API to get the Verse of the Day. This is for custom prompts only.

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
    temperature=0.5,
)

# Get controlflow context from the environment variable
controlflow_context = os.getenv('CONTROL_FLOW_CONTEXT_KJV')

base_lib_file_path = 'datasets/'

with open(f'{base_lib_file_path}lyrical_adjectives.json') as f:
    lyrical_adjectives = json.load(f)

def get_random_bible_passage():
    # Load Bible-kjv library
    with open(f'{base_lib_file_path}bible_book_chapters.json') as f:
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
    with open(f'{base_lib_file_path}Bible-kjv/{bible_book_choice[0]}.json') as f:
        bible_verses = json.load(f)

    # Select the chosen chapter
    bible_verses_chapter = bible_verses["chapters"][bible_chapter_choice - 1]

    # Get all verses for the chapter
    verses = bible_verses_chapter["verses"]

    # Initialize empty string to store all verses
    verse_numbers = ""
    chapter_text = ""

    # Loop through all verses and concatenate their text
    for verse in verses:
        verse_numbers += verse["verse"] + ", "
        chapter_text += verse["text"] + " "  # Add space between verses

        # Remove trailing space
    chapter_text = chapter_text.strip()

    return chapter_text, bible_book_choice[0], bible_chapter_choice, verse_numbers

def get_citation_bible_book_and_chapter(bible_book_choice, bible_chapter_choice, verse_numbers, chapter_text):
    bible_citation = f'{bible_book_choice} {bible_chapter_choice}\nVerse numbers: {verse_numbers}\n{chapter_text}\n{bible_book_choice} {bible_chapter_choice}\nKing James Version\nPublic Domain'
    return bible_citation


def revise_prompt_with_control_flow_kjv_verbatim(lyrics_prompt):
    lyrics_prompt_revised = cf.run(controlflow_context,
        context=dict(prompt=lyrics_prompt),
    )

    return lyrics_prompt_revised

# Function to generate a random biblical song prompt less than 200 characters in string length
def generate_custom_bible_lyrics_kjv_verbatim_prompt():

    # Get a random bible passage
    chapter_text, bible_book_choice, bible_chapter_choice, verse_numbers = get_random_bible_passage()
    print(f"Bible book choice: {bible_book_choice}")
    print(f"Bible chapter choice: {bible_chapter_choice}")
    print(f"Verse numbers: {verse_numbers}")
    print(f"Chapter text: {chapter_text}")

    # Get a bible citation  
    bible_citation = get_citation_bible_book_and_chapter(bible_book_choice, bible_chapter_choice, verse_numbers, chapter_text)
    
    print(f"Bible citation: {bible_citation}")
    print(f"Length of lyrics prompt: {len(chapter_text)}")
    print(f"Original lyrics prompt: {chapter_text}")
    print("Trimmed lyrics prompt:")
    print(chapter_text[:2900])
    print("Revised lyrics prompt:")

    if len(chapter_text) > 2999:
        revised_lyrics_prompt = revise_prompt_with_control_flow_kjv_verbatim(chapter_text[:2900])
        return revised_lyrics_prompt, bible_citation, chapter_text[:2900]
    else:
        revised_lyrics_prompt = revise_prompt_with_control_flow_kjv_verbatim(chapter_text)
        return revised_lyrics_prompt, bible_citation, chapter_text
    

def generate_bible_gateway_votd_verbatim_custom():
    votd_revised_lyrics_prompt = ""

    # Use Bible Gateway Verse of the Day
    votds = get_bible_votd_kjv()
    biblecontent = votds['votd']['content']
    biblereference = votds['votd']['reference']
    bibleversion = votds['votd']['version']
    verselink = votds['votd']['permalink']

    votd_revised_lyrics_prompt = revise_prompt_with_control_flow_kjv_verbatim(biblecontent)

    return votd_revised_lyrics_prompt, biblecontent, biblereference, bibleversion, verselink

# test the function
# Romans Chapter 5
provide_verses_7 = "Therefore being justified by faith, we have peace with God through our Lord Jesus Christ: By whom also we have access by faith into this grace wherein we stand, and rejoice in hope of the glory of God. And not only so, but we glory in tribulations also: knowing that tribulation worketh patience; And patience, experience; and experience, hope: And hope maketh not ashamed; because the love of God is shed abroad in our hearts by the Holy Ghost which is given unto us. For when we were yet without strength, in due time Christ died for the ungodly. For scarcely for a righteous man will one die: yet peradventure for a good man some would even dare to die. But God commendeth his love toward us, in that, while we were yet sinners, Christ died for us. Much more then, being now justified by his blood, we shall be saved from wrath through him. For if, when we were enemies, we were reconciled to God by the death of his Son, much more, being reconciled, we shall be saved by his life. And not only so, but we also joy in God through our Lord Jesus Christ, by whom we have now received the atonement. Wherefore, as by one man sin entered into the world, and death by sin; and so death passed upon all men, for that all have sinned: (For until the law sin was in the world: but sin is not imputed when there is no law. Nevertheless death reigned from Adam to Moses, even over them that had not sinned after the similitude of Adam's transgression, who is the figure of him that was to come. But not as the offence, so also is the free gift. For if through the offence of one many be dead, much more the grace of God, and the gift by grace, which is by one man, Jesus Christ, hath abounded unto many. And not as it was by one that sinned, so is the gift: for the judgment was by one to condemnation, but the free gift is of many offences unto justification. For if by one man's offence death reigned by one; much more they which receive abundance of grace and of the gift of righteousness shall reign in life by one, Jesus Christ.) Therefore as by the offence of one judgment came upon all men to condemnation; even so by the righteousness of one the free gift came upon all men unto justification of life. For as by one man's disobedience many were made sinners, so by the obedience of one shall many be made righteous. Moreover the law entered, that the offence might abound. But where sin abounded, grace did much more abound: That as sin hath reigned unto death, even so might grace reign through righteousness unto eternal life by Jesus Christ our Lord."

revise_provided_verses_7 = revise_prompt_with_control_flow_kjv_verbatim(provide_verses_7)
# print(provide_verses_5)
print(revise_provided_verses_7)