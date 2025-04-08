# AI Gospel Music API & Suno Prompt Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) <!-- Added a license badge example -->

Leverages AI (Google Gemini via Control Flow/LangChain) and various data sources to generate randomized, structured prompts (lyrics and music styles) for the Suno AI music generation platform. Focuses on biblically accurate gospel songs (using KJV text) and mnemonic topic-based lyrics.

**My Suno Profile:** <https://suno.com/@crossofthemessiah>

*Disclaimer: Ownership and commercial use rights are retained for songs generated by the maintainer using Suno during an active subscription. See [Suno EULA](https://help.suno.com/en/articles/2421505).*

*LLM Code Generation Notice: Portions of this codebase were generated or refined using large language models. Final code was reviewed and adapted by the project maintainer. Use at your own risk.*

*Limitation of Liability/Copyright: For the complete statement, please visit [cmathgit.github.io](https://cmathgit.github.io).*

## Featured Suno Work

Here are some examples of playlists created using prompts generated by this project, showcasing various styles and themes:

*   **Mixed Interpretations: An Insult to Life Itself \[My DnB Mixes Extended by Suno]**
    *   **Link:** [https://suno.com/playlist/6af6d714-7d6c-4a25-983b-00cab2fef923](https://suno.com/playlist/6af6d714-7d6c-4a25-983b-00cab2fef923)
    *   *Description:* A blend of original human-authored Drum & Bass tracks (marked "[Uploaded]") and AI interpretations/extensions based on them, demonstrating meaningful human authorship in AI collaboration.

*   **(VOTD) Verse of the Day**
    *   **Link:** [https://suno.com/playlist/d4a4c866-f4c8-4c88-8c56-bec078acee90](https://suno.com/playlist/d4a4c866-f4c8-4c88-8c56-bec078acee90)
    *   *Description:* Songs generated using the KJV Verse of the Day fetched via the Bible Gateway API.

*   **The KJV Bible Verbatim**
    *   **Link:** [https://suno.com/playlist/809429aa-fe7d-4e6b-9e98-83ae42741809](https://suno.com/playlist/809429aa-fe7d-4e6b-9e98-83ae42741809)
    *   *Description:* Music generated with lyrics taken verbatim from various passages of the King James Version Bible.

*   **Christian Worship**
    *   **Link:** [https://suno.com/playlist/19555fda-26ad-4f14-82de-52b02b5bcdf0](https://suno.com/playlist/19555fda-26ad-4f14-82de-52b02b5bcdf0)
    *   *Description:* Biblically accurate ambient Christian worship songs.

*   **Bluegrass Gospel**
    *   **Link:** [https://suno.com/playlist/2f287c89-5148-4df0-b230-6624aa3a7bf0](https://suno.com/playlist/2f287c89-5148-4df0-b230-6624aa3a7bf0)
    *   *Description:* AI-generated bluegrass gospel songs with biblically accurate themes.

*   **Gospel Rap**
    *   **Link:** [https://suno.com/playlist/67aa4eb4-81a8-4309-9c92-bf01cdc4beb2](https://suno.com/playlist/67aa4eb4-81a8-4309-9c92-bf01cdc4beb2)
    *   *Description:* Biblically accurate Gospel Rap and Christian Hip Hop.

*   **Mnemonics Information Verbatim**
    *   **Link:** [https://suno.com/playlist/9b018e23-095d-4ac8-93af-38b7c6168091](https://suno.com/playlist/9b018e23-095d-4ac8-93af-38b7c6168091)
    *   *Description:* Using song to aid memory, transforming various informational topics into lyrics.

*   **Mathcraft OST | C418 Aria Math Handpan Tribute**
    *   **Link:** [https://suno.com/playlist/2414feb3-ef82-4bf6-a1af-dfc935adb135](https://suno.com/playlist/2414feb3-ef82-4bf6-a1af-dfc935adb135)
    *   *Description:* An AI-generated instrumental tribute (minimalist concerto handpan) inspired by C418's "Aria Math".

## Featured YouTube Content

Check out these YouTube playlists featuring music and videos created using this project:
*   **Mixed Interpretations: An Insult to Life Itself [My DnB Mixes Extended by Suno]:** [https://youtube.com/playlist?list=PLuggBNq5l-IsrKl5ogyQivcIjCp_gD32k&feature=shared](https://youtube.com/playlist?list=PLuggBNq5l-IsrKl5ogyQivcIjCp_gD32k&feature=shared)
*   **AILLM Adaptations of My Music:** [https://youtube.com/playlist?list=PLuggBNq5l-Iv0_G8xtGkgeLFQCyx4XgM5&feature=shared](https://youtube.com/playlist?list=PLuggBNq5l-Iv0_G8xtGkgeLFQCyx4XgM5&feature=shared)
*   **Verse of the Day (VOTD) [AILLMusic]:** [https://www.youtube.com/watch?v=6VVU10BxIqQ&list=PLuggBNq5l-Itv6gJfY73v9dpji350LTKI](https://www.youtube.com/watch?v=6VVU10BxIqQ&list=PLuggBNq5l-Itv6gJfY73v9dpji350LTKI)
*   **The KJV Bible Verbatim [AILLMusic]:** [https://youtube.com/playlist?list=PLuggBNq5l-IsLKLQp5SmTUqLtNBvDDUxu&feature=shared](https://youtube.com/playlist?list=PLuggBNq5l-IsLKLQp5SmTUqLtNBvDDUxu&feature=shared)
*   **AILLMusic - Progressive Metal Djent:** [https://youtube.com/playlist?list=PLuggBNq5l-ItCgXjKnAyuJdTebHvwbvOD&feature=shared](https://youtube.com/playlist?list=PLuggBNq5l-ItCgXjKnAyuJdTebHvwbvOD&feature=shared)
*   **AILLMusic - EDM:** [https://youtube.com/playlist?list=PLuggBNq5l-Iv2IcBVW-5D-kZak9A8O_9d&feature=shared](https://youtube.com/playlist?list=PLuggBNq5l-Iv2IcBVW-5D-kZak9A8O_9d&feature=shared)
*   **🎵 Mathcraft OST | C418 Aria Math Handpan Tribute | Andante G Lydian | [AILLMusic]:** [https://youtube.com/playlist?list=PLuggBNq5l-IviBoRYexrX-RvwO18BBCps&feature=shared](https://youtube.com/playlist?list=PLuggBNq5l-IviBoRYexrX-RvwO18BBCps&feature=shared)
*   **AILLMusic - Bluegrass Gospel:** [https://youtube.com/playlist?list=PLuggBNq5l-ItgaDYlJDxIYz3GaZ0OJiVl&feature=shared](https://youtube.com/playlist?list=PLuggBNq5l-ItgaDYlJDxIYz3GaZ0OJiVl&feature=shared)
*   **AILLMusic - Christian Worship:** [https://youtube.com/playlist?list=PLuggBNq5l-ItyS0l-oLws3wALegOIRolU&feature=shared](https://youtube.com/playlist?list=PLuggBNq5l-ItyS0l-oLws3wALegOIRolU&feature=shared)
*   **AILLMusic - Gospel Rap:** [https://youtube.com/playlist?list=PLuggBNq5l-It6UGYjotgYQ0iD8ErtT25o&feature=shared](https://youtube.com/playlist?list=PLuggBNq5l-It6UGYjotgYQ0iD8ErtT25o&feature=shared)
*   **If Any Man Have an Ear, Let Him Hear: A Journey Through Revelation 13 & 14 | Song Cycle | AI Music:** [https://youtube.com/playlist?list=PLuggBNq5l-IvB6Syv28OK7_AyuQOQDOyN&feature=shared](https://youtube.com/playlist?list=PLuggBNq5l-IvB6Syv28OK7_AyuQOQDOyN&feature=shared)
*   **AILLMusic - Geoffrey's Concertos:** [https://youtube.com/playlist?list=PLuggBNq5l-ItSRpBlZgRNZ3MqfEC_TWjE&feature=shared](https://youtube.com/playlist?list=PLuggBNq5l-ItSRpBlZgRNZ3MqfEC_TWjE&feature=shared)
*   **Mnemonics Information Verbatim [AILLMusic]:** [https://youtube.com/playlist?list=PLuggBNq5l-IsEzFty77YebeugMxM1fwGj&feature=shared](https://youtube.com/playlist?list=PLuggBNq5l-IsEzFty77YebeugMxM1fwGj&feature=shared)
*   **AILLM Short Films (Non-Narrative Mostly):** [https://youtube.com/playlist?list=PLuggBNq5l-Iu46eFfg7diFSkUM5kaXEPf&feature=shared](https://youtube.com/playlist?list=PLuggBNq5l-Iu46eFfg7diFSkUM5kaXEPf&feature=shared)

## Core Dependency: Suno API Wrapper
*   Python 3.7+
*   Access to the running `suno-api` wrapper instance.
*   API Key for an LLM provider supported by LangChain (e.g., Google Gemini, OpenAI, Anthropic) for AI-powered features.
*   Git (for cloning repositories).

## Setup and Installation

1.  **Clone this Repository:**
    ```bash
    git clone <your-repo-url> # Replace with the actual URL
    cd ai-gospel-music-api # Or your repo directory name
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    # Create
    python -m venv env

    # Activate (Windows CMD)
    .\env\Scripts\activate.bat
    # Activate (Windows PowerShell - might require policy adjustment)
    # .\env\Scripts\Activate.ps1
    # Activate (Linux/macOS)
    # source env/bin/activate
    ```
    *(Your prompt should now show `(env)`)*

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Obtain Bible Data (for random KJV passage generation):**
    *   Clone the `Bible-kjv` repository into the `datasets/` directory:
    ```bash
        cd datasets
        git clone https://github.com/aruljohn/Bible-kjv.git
        cd ..
    ```
    *   *Alternatively, download the ZIP from the GitHub page and extract its contents into `datasets/Bible-kjv`.*
    *   This step is *not* required if you only plan to use the Bible Gateway Verse of the Day feature.

## Configuration: Environment Variables (`.env`)

Create a file named `.env` in the project's root directory to store necessary API keys and configuration for the AI features.

# Example using Google Generative AI (Gemini)
        GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"
MODEL_NAME="gemini-1.5-flash" # Or another compatible Google model (e.g., gemini-pro)

# Control Flow Contexts (Required for specific AI refinement tasks)
# These identifiers tell the AI how to structure the output.
# You may need to define these contexts via the Control Flow library or service if not pre-configured.
CONTROL_FLOW_CONTEXT_KJV="your_kjv_verbatim_lyric_structure_context"
CONTROL_FLOW_CONTEXT_LYRICIST="your_mnemonic_lyric_structure_context"
CONTROL_FLOW_CONTEXT_STYLES="your_music_style_refinement_context"

# --- OR --- Example using OpenAI ---
# OPENAI_API_KEY="YOUR_OPENAI_API_KEY_HERE"
# MODEL_NAME="gpt-4" # Or another compatible OpenAI model

# --- OR --- Example using Anthropic ---
# ANTHROPIC_API_KEY="YOUR_ANTHROPIC_API_KEY_HERE"
# MODEL_NAME="claude-3-opus-20240229" # Or another compatible Anthropic model

# Note: Ensure you install the correct LangChain package for your chosen provider
# e.g., pip install langchain-openai langchain-anthropic

**Important:**
*   Use the correct environment variable name for your chosen LLM provider (`GOOGLE_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, etc.).
*   Consult the [ControlFlow LLM Configuration Guide](https://controlflow.ai/guides/configure-llms) and [LangChain Chat Model Integrations](https://python.langchain.com/docs/integrations/chat/) for details on providers and required variables.
*   The scripts default to `ChatGoogleGenerativeAI`. To use a different provider, you'll need to:
    1.  Install the provider's package (e.g., `pip install langchain-openai`).
    2.  Set the correct API key in `.env`.
    3.  Modify the model initialization in the relevant Python scripts (e.g., change `ChatGoogleGenerativeAI(...)` to `ChatOpenAI(...)` in `gen_custom_lyrics_kjv_verbatim_votd.py`, etc.).

## Running the Examples

Ensure your virtual environment is active and your `.env` file is configured.

1.  **Generate Bible-Based Prompts:**
    *   This script combines random music style generation with KJV lyric generation (either from the Bible Gateway Verse of the Day or a random passage from the `Bible-kjv` dataset) using AI for structuring.
    ```bash
    python generate_prompts_bible.py
    ```
    *   *(Requires `GOOGLE_API_KEY` or equivalent and relevant `CONTROL_FLOW_CONTEXT_...` variables in `.env`)*.
    *   *(Requires `datasets/Bible-kjv` if using random passages)*.

2.  **Generate Mnemonic Topic Prompts:**
    *   This script combines random music style generation with lyrics generated from a random topic (fetched from `datasets/random_mnemonic_topics_dict.json`) using AI for summarization and structuring.
    ```bash
    python generate_prompts_mnemonic.py
    ```
    *   *(Requires `GOOGLE_API_KEY` or equivalent and relevant `CONTROL_FLOW_CONTEXT_...` variables in `.env`)*.

3.  **Batch Generation (Windows Example):**
    *   Runs `generate_prompts_suno_ai.py` (adjust script name if needed) multiple times. Inspect the `.bat` file for details.
    ```batch
    runpy_gen_prompts_suno.bat
    ```

## Key Features & Technologies

*   **AI Prompt Refinement:** Uses Google Gemini (or other LLMs via LangChain/Control Flow) to:
    *   Structure verbatim KJV Bible text into song formats ([Intro], [Verse], [Chorus], etc.). See `gen_custom_lyrics_kjv_verbatim_votd.py`.
    *   Generate summaries from topics and structure them into mnemonic lyrics. See `gen_custom_lyrics_mnemonic.py`.
    *   Refine randomly combined musical elements into coherent style prompts. See `gen_custom_rand_style_of_music.py`.
*   **Bible Data Integration:**
    *   Fetches the KJV Verse of the Day via the Bible Gateway API (`biblegateway_api.py`).
    *   Reads random KJV chapters/passages from the `datasets/Bible-kjv` repository (`gen_custom_lyrics_kjv_verbatim_votd.py`).
*   **Randomized Prompt Elements:** Selects random items from internal datasets (genres, instruments, keys, tempos, vocals, etc.) to create diverse music style prompts. (See data structures within the `gen_...` scripts or potentially JSON files in `datasets/`).
*   **Suno API Interaction:** Sends generated prompts to a running instance of the `gcui-art/suno-api` wrapper to generate music. (Core interaction logic likely within scripts like `generate_prompts_suno_ai.py` or similar).

## Prompt History

Generated prompts and potentially other metadata are logged for history. Check the `log/` directory for these files.

*(Note: The extensive lists of musical keys, modes, tempos, instruments, genres, and Bible book details previously in this README have been removed for conciseness but are utilized internally by the scripts, often loaded from Python lists/tuples within the code or from JSON files in the `datasets/` directory.)*