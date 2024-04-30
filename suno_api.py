import requests
import time

base_url = 'http://localhost:3000'


def custom_generate_audio(payload):
    url = f"{base_url}/api/custom_generate"
    response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
    return response.json()


def generate_audio_by_prompt(payload):
    url = f"{base_url}/api/generate"
    response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
    return response.json()


def generate_song_lyrics(payload):
    url = f"{base_url}/api/generate_lyrics"
    response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
    return response.json()


def get_audio_information(audio_id):
    url = f"{base_url}/api/get?ids={audio_id}"
    response = requests.get(url)
    return response.json()


def get_audio_informations(audio_ids):
    url = f"{base_url}/api/get?ids={audio_ids}"
    response = requests.get(url)
    return response.json()


def get_quota_information():
    url = f"{base_url}/api/get_limit"
    response = requests.get(url)
    return response.json()
    
def download_mp3_file(filename: str, url: str):
    print()
    print(f"===== DOWNLOADING MP3 FILE =====")
    print(f"Requesting: {url}")
    response = requests.get(url)
    print(f"Response Status: {response.status_code}")

    # write it locally
    if response.status_code == 200:
        file = f"{filename}.mp3"
        print(f"Writing file: {file}")
        with open(file, 'wb') as f:
            f.write(response.content)
        print(f"File successfully downloaded: {file}")
    else:
        print(f"Failed to download the file.")

def wait_for_song(id: str):
    periods = 60
    period_len = 3
    print()
    print(f"===== WAITING FOR {id} =====")
    for _ in range(periods):
        data = get_audio_information(id)
        
        if data is not None:
            #print("Response received from Suno api/custom_generate: ", data)
            suno_api_get_audio_info_response_file = 'log/last_response_received_from_suno_api_audio_get_info.txt'
            try:
                with open(suno_api_get_audio_info_response_file, "w") as file:
                    file.write(f"{data}")
            except IOError as e:
                print(f"Error writing to {suno_api_get_audio_info_response_file}: ", e)
        else:
            print(f"Request to Suno /api/get?ids={id} failed.")
            
        if data:
            song = data[0]
            if song["status"] in ['streaming', 'complete']:
                print(f"READY: {song['id']} ==> {song['audio_url']}")
                download_mp3_file(f"{song['title']}_{id}", song['audio_url'])
                break
        print(".", end="")
        time.sleep(period_len)