import os
from dotenv import load_dotenv
import datetime

# Import functions from the custom generation scripts
from gen_custom_rand_style_of_music import (
    generate_custom_random_style_of_music_prompt,
    generate_custom_random_drum_loop_prompt,
    generate_custom_random_concerto_prompt
)
from gen_custom_lyrics_kjv_verbatim_votd import (
    generate_bible_gateway_votd_verbatim_custom,
    get_random_bible_passage,
    revise_prompt_with_control_flow_kjv_verbatim,
    get_citation_bible_book_and_chapter
)

# Load environment variables from .env file
# This is important to ensure the imported functions have access to API keys and contexts
load_dotenv()

# Define output directory and ensure it exists
output_dir = "outfiles/prompts"
os.makedirs(output_dir, exist_ok=True)
output_file_path = os.path.join(output_dir, "bible_prompts.txt")

def write_output(file_handle, content):
    """Helper function to write content to the file."""
    file_handle.write(content + "\n")

def main():
    """
    Main function to generate and write various prompts and lyrics
    to a file using the imported generation functions.
    """
    print(f"Generating prompts and writing to: {output_file_path}")

    # Open the output file in append mode
    with open(output_file_path, "a+", encoding="utf-8") as f:
        # Write a timestamp for this run
        f.write(f"\n--- Run executed at: {datetime.datetime.now()} ---\n")

        write_output(f, "\n--- Generating Music Style Prompts ---")
        print("Generating Music Style Prompts...") # Keep console status

        # Generate a general music style prompt (with vocals)
        try:
            revised_style, original_style, exclude_pop = generate_custom_random_style_of_music_prompt(instrumental=False)
            write_output(f, "\nGeneral Music Style (Vocals):")
            write_output(f, f"  Original Combination: {original_style}")
            write_output(f, f"  Revised Prompt (AI Refined): {revised_style}")
            write_output(f, f"  Exclude Styles String: {exclude_pop}")
        except Exception as e:
            error_msg = f"\nError generating general music style: {e}"
            print(error_msg) # Print error to console
            write_output(f, error_msg) # Also log error to file

        # Generate a drum loop style prompt
        try:
            revised_drums, original_drums, exclude_drums = generate_custom_random_drum_loop_prompt()
            write_output(f, "\nDrum Loop Style:")
            write_output(f, f"  Original Combination: {original_drums}")
            write_output(f, f"  Revised Prompt (AI Refined): {revised_drums}")
            write_output(f, f"  Exclude Styles String: {exclude_drums}")
        except Exception as e:
            error_msg = f"\nError generating drum loop style: {e}"
            print(error_msg)
            write_output(f, error_msg)

        # Generate a concerto style prompt
        try:
            revised_concerto, original_concerto, exclude_concerto_pop = generate_custom_random_concerto_prompt()
            write_output(f, "\nConcerto Style:")
            write_output(f, f"  Original Combination: {original_concerto}")
            write_output(f, f"  Revised Prompt (AI Refined): {revised_concerto}")
            write_output(f, f"  Exclude Styles String: {exclude_concerto_pop}")
        except Exception as e:
            error_msg = f"\nError generating concerto style: {e}"
            print(error_msg)
            write_output(f, error_msg)

        write_output(f, "\n\n--- Generating KJV Bible Lyrics ---")
        print("Generating KJV Bible Lyrics...") # Keep console status

        # Generate lyrics from KJV Verse of the Day
        try:
            write_output(f, "\nKJV Verse of the Day Lyrics:")
            votd_revised_lyrics, bible_content, bible_reference, bible_version, _ = generate_bible_gateway_votd_verbatim_custom()
            write_output(f, f"  Source: {bible_reference} ({bible_version})")
            write_output(f, f"  Original Content: {bible_content}")
            write_output(f, f"  Revised Lyrics (AI Structured):\n{votd_revised_lyrics}")
        except Exception as e:
            error_msg = f"\nError generating VotD lyrics: {e}\n  (Ensure Bible Gateway API is accessible and GOOGLE_API_KEY/contexts are set)"
            print(error_msg)
            write_output(f, error_msg)

        # Generate lyrics from a random KJV chapter
        try:
            write_output(f, "\nRandom KJV Chapter Lyrics:")
            # Get random passage text
            chapter_text, book, chapter, verses = get_random_bible_passage()
            write_output(f, f"  Source: {book} {chapter} (Verses: {verses.strip(', ')})")
            write_output(f, f"  Original Chapter Text (First 500 chars):\n{chapter_text[:500]}...")
            write_output(f, f"\n  Original Chapter Text Length: {len(chapter_text)}")

            # Generate citation
            citation = get_citation_bible_book_and_chapter(book, chapter, verses, chapter_text)
            write_output(f, f"\n  Full Citation:\n{citation}")

            # Revise the text using AI (handle potential length issues)
            max_len = 2900 # Define a max length for safety, similar to the original script
            input_text = chapter_text[:max_len] if len(chapter_text) > max_len else chapter_text
            write_output(f, f"\n  Revising text (length: {len(input_text)})...")
            print(f"Revising {book} {chapter} text (length: {len(input_text)})...") # Console status

            revised_chapter_lyrics = revise_prompt_with_control_flow_kjv_verbatim(input_text)
            write_output(f, f"\n  Revised Lyrics (AI Structured):\n{revised_chapter_lyrics}")

        except FileNotFoundError as e:
             error_msg = f"\nError loading Bible data: {e}\n  (Ensure the 'datasets/Bible-kjv' directory and JSON files exist)"
             print(error_msg)
             write_output(f, error_msg)
        except Exception as e:
            error_msg = f"\nError generating random chapter lyrics: {e}\n  (Ensure 'datasets/' files exist and GOOGLE_API_KEY/contexts are set)"
            print(error_msg)
            write_output(f, error_msg)

    # Inform user upon completion
    print(f"\nGeneration complete. Results appended to: {output_file_path}")


if __name__ == "__main__":
    # Ensure API keys and contexts are loaded from .env
    # Check for essential keys if needed
    if not os.getenv("GOOGLE_API_KEY"):
        print("Warning: GOOGLE_API_KEY not found in environment variables or .env file.")
        print("AI-powered generation steps might fail.")
    # Check for contexts used in this script
    if not os.getenv("CONTROL_FLOW_CONTEXT_KJV"):
         print("Warning: CONTROL_FLOW_CONTEXT_KJV not found. KJV lyric structuring might fail.")
    if not os.getenv("CONTROL_FLOW_CONTEXT_STYLES"):
         print("Warning: CONTROL_FLOW_CONTEXT_STYLES not found. Style refinement might fail.")

    main()
