import os
from dotenv import load_dotenv
import datetime

# Import functions from the mnemonic generation script
from gen_custom_lyrics_mnemonic import (
    generate_mnemonic_topic_prompt,
    revise_prompt_with_control_flow_mnemonic
)

# Import functions from the style generation script
from gen_custom_rand_style_of_music import (
    generate_custom_random_style_of_music_prompt,
    generate_custom_random_drum_loop_prompt,
    generate_custom_random_concerto_prompt
)

# Load environment variables from .env file
# This is important for API keys and Control Flow contexts
load_dotenv()

# Define output directory and ensure it exists
output_dir = "outfiles/prompts"
os.makedirs(output_dir, exist_ok=True)
output_file_path = os.path.join(output_dir, "mnemonic_prompts.txt")

def write_output(file_handle, content):
    """Helper function to write content to the file."""
    file_handle.write(content + "\n")

def main():
    """
    Main function to generate music style prompts and mnemonic topic lyrics,
    writing the results to a file.
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

        write_output(f, "\n\n--- Generating Mnemonic Topic Lyrics ---")
        print("Generating Mnemonic Topic Lyrics...") # Keep console status

        # Generate lyrics from a randomly chosen topic
        try:
            write_output(f, "\nRandom Mnemonic Topic Lyrics:")
            # generate_mnemonic_topic_prompt internally calls the LLM for summary
            # and then revise_prompt_with_control_flow_mnemonic for lyrics
            mnemonic_topic, prompt, revised_lyrics, original_summary = generate_mnemonic_topic_prompt()
            write_output(f, f"  Chosen Topic: {mnemonic_topic}")
            write_output(f, f"  Prompt used for Summary: {prompt}")
            write_output(f, f"\n  Original Summary (AI Generated):\n{original_summary}")
            write_output(f, f"\n  Revised Lyrics (AI Structured):\n{revised_lyrics}")
        except FileNotFoundError as e:
             error_msg = f"\nError loading mnemonic topics: {e}\n  (Ensure 'datasets/random_mnemonic_topics_dict.json' exists)"
             print(error_msg)
             write_output(f, error_msg)
        except Exception as e:
            error_msg = f"\nError generating random mnemonic lyrics: {e}\n  (Ensure GOOGLE_API_KEY/contexts are set and model API is reachable)"
            print(error_msg)
            write_output(f, error_msg)

        # Generate lyrics from a provided example topic
        try:
            write_output(f, "\nProvided Mnemonic Topic Lyrics (Relativity Example):")
            # Example text similar to the one in gen_custom_lyrics_mnemonic.py
            mnemonic_topic_example = "Consider this analogy of Einstein's General Theory of Relativity. When you shoot a basket ball, you perceive an arc, but the ball is actually moving in a straight vector... (text truncated for brevity) ... This equivalence underpins the geometric interpretation of gravity as spacetime curvature."
            write_output(f, f"  Input Text (Truncated): {mnemonic_topic_example[:150]}...")

            # Revise the provided text directly using Control Flow
            revised_example_lyrics = revise_prompt_with_control_flow_mnemonic(mnemonic_topic_example)
            write_output(f, f"\n  Revised Lyrics (AI Structured):\n{revised_example_lyrics}")

        except Exception as e:
            error_msg = f"\nError generating provided mnemonic lyrics: {e}\n  (Ensure GOOGLE_API_KEY/contexts are set and model API is reachable)"
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
    if not os.getenv("CONTROL_FLOW_CONTEXT_LYRICIST"):
         print("Warning: CONTROL_FLOW_CONTEXT_LYRICIST not found. Mnemonic lyric structuring might fail.")
    if not os.getenv("CONTROL_FLOW_CONTEXT_STYLES"):
         print("Warning: CONTROL_FLOW_CONTEXT_STYLES not found. Style refinement might fail.")

    main()
