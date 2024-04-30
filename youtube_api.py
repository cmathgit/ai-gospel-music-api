import requests
import json

# base_url = 'https://www.biblegateway.com/votd/get/?format=JSON'

def print_lyric_video_descr_custom(id, suno_user, song_title, song_lyrics, style, genre, key, mode, reference, version, gen_lyrics, song):
    # data for text file
    vid_descr_file = f"{song_title}_{id}_vid_descr.txt"
    vid_descr_file_data = f"{song_title} [{reference}] [{key} ({mode})] [AI Lyric Video]\n\nUsing AI to generate biblically accurate {genre} songs and music videos. Generate meaningful lyrics to a song devoted to preserving the message of {reference} taken directly from the {version} bible with remnants of the Gospel of Jesus Christ.\n\nTitle: {song_title} by {suno_user}\n\nCreated: {song['created_at']}\n\nStyle of Music Prompt: {style}.\n\nLyrics and video inspired by {reference} of the {version} bible.\n\nSong and Lyrics generated using Suno AI\n\naudio url: {song['audio_url']}\nvideo url: {song['video_url']}\n\nGPT Prompt: {song['gpt_description_prompt']}\n\nLyrics Prompt: {gen_lyrics}\n\nLyrics:\n{song_lyrics}"
    
    # data for YouTube API
    yt_vid_descr_data_file = f"{song_title}_{id}_vid_descr.json"
    yt_vid_descr_data = [
        (id, song_title, song_lyrics, style, genre, key, mode, reference, version, gen_lyrics, song),
        (f"{song_title} [{reference}] [{key} ({mode})] [AI Lyric Video]",f"Using AI to generate biblically accurate {genre} songs and music videos. Generate meaningful lyrics to a song devoted to preserving the message of {reference} taken directly from the {version} bible with remnants of the Gospel of Jesus Christ.",f"Title: {song_title} by {suno_user}",f"Created: {song['created_at']}",f"Style of Music Prompt: {style}.",f"Lyrics and video inspired by {reference} of the {version} bible.",f"Song and Lyrics generated using Suno AI",f"audio url: {song['audio_url']}",f"video url: {song['video_url']}",f"GPT Prompt: {song['gpt_description_prompt']}",f"Lyrics Prompt: {gen_lyrics}",f"Lyrics:\n{song_lyrics}")
    ]
    
    print(f"Writing data to video description text file: {vid_descr_file}")
    try:
        with open(vid_descr_file, "w") as file:
            file.write(vid_descr_file_data)
    except IOError as e:
        print(f"Error writing to {vid_descr_file}: ", e)
        
    # Writing to JSON file with error handling
    print(f"Writing data to video description json file for YouTube API: {yt_vid_descr_data_file}")
    try:
        with open(yt_vid_descr_data_file, 'w') as yt_vid_descr_data_dump_file:
            json.dump(yt_vid_descr_data, yt_vid_descr_data_dump_file)
    except IOError as e:
        print("Error writing to file:", e)
        
        
def print_lyric_video_descr_simple(id, suno_user, genre, key, mode, reference, version, prompt, song):
    vid_descr_file = f"{song['title']}_{id}_vid_descr.txt"
    vid_descr_file_data = f"{song['title']} [{reference}] [{key} ({mode})] [AI Lyric Video]\n\nUsing AI to generate biblically accurate {genre} songs and music videos.\n\nTitle: {song['title']} by {suno_user}\n\nCreated: {song['created_at']}\n\nStyle of Music: {genre} in the key of {key} ({mode}).\n\nLyrics and video inspired by {reference} of the {version} bible.\n\nSong and Lyrics generated using Suno AI\n\naudio url: {song['audio_url']}\nvideo url: {song['video_url']}\n\n\n\nGPT Prompt: {song['gpt_description_prompt']}\n\nLyrics Prompt: {prompt}\n\nLyrics:\n{song['lyric']}"
    
    print(f"Writing Description file: {vid_descr_file}")
    try:
        with open(vid_descr_file, "w") as file:
            file.write(vid_descr_file_data)
    except IOError as e:
        print(f"Error writing to {vid_descr_file}: ", e)
        
        
def print_instrumental_video_descr_simple(id, suno_user, genre, instrument, key, mode, prompt, song):
    vid_descr_file = f"{song['title']}_{id}_descr.txt"
    vid_descr_file_data = f"{song['title']} [{key} ({mode})] [AI Lyric Video]\n\nUsing AI to generate {genre} instrumentals for vocalists.\n\nTitle: {song['title']} by {suno_user}\n\nCreated: {song['created_at']}\n\nInstrument(s) Used: {instrument}\n\nStyle of Music: {genre} in the key of {key} ({mode}).\n\nSong generated using Suno AI\n\nGPT Prompt: {song['gpt_description_prompt']}\n\nSong Prompt: {prompt}\n\n"
    
    print(f"Writing Description file: {vid_descr_file}")
    try:
        with open(vid_descr_file, "w") as file:
            file.write(vid_descr_file_data)
    except IOError as e:
        print(f"Error writing to {vid_descr_file}: ", e)

