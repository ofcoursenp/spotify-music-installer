import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import winreg
import os
import subprocess
from time import sleep

# Define paths
if os.path.exists(r"C:\ffmpeg\ffmpeg_extract\ffmpeg-7.0.2-full_build\bin") == False:
    ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z"
    install_path = "C:/ffmpeg/ffmpeg_extract"
    ffmpeg_archive = os.path.join(install_path, "ffmpeg-release-full.7z")
    seven_zip_path = "C:/Program Files/7-Zip/7z.exe"  # Adjust if necessary

    # Ensure the installation directory exists
    os.makedirs(install_path, exist_ok=True)

    # Download the FFmpeg archive
    print("Downloading FFmpeg...")
    import requests
    response = requests.get(ffmpeg_url)
    if response.status_code == 200:
        with open(ffmpeg_archive, 'wb') as file:
            file.write(response.content)
        print("Download complete.")
    else:
        print("Failed to download FFmpeg.")
        exit(1)

    # Extract the FFmpeg archive using 7-Zip
    print("Extracting FFmpeg...")
    subprocess.run([seven_zip_path, 'x', ffmpeg_archive, f'-o{install_path}', '-y'])

    print("Extraction complete.")

import os
import sys
import subprocess
import platform

def add_to_path(path):
    print(f"Adding {path} to PATH...")
    if platform.system() == "Windows":
        # Add the directory to the user PATH environment variable
        current_path = os.environ.get('PATH', '')
        if path not in current_path:
            os.environ['PATH'] = path + os.pathsep + current_path
            # You might need to update the PATH in the system environment variables as well
            result = subprocess.run(['setx', 'PATH', os.environ['PATH']], capture_output=True, text=True)
            print(f"setx output: {result.stdout}")
            print(f"setx error: {result.stderr}")

def main():
    # Path to FFmpeg binary directory
    ffmpeg_bin_path = r"C:\ffmpeg\ffmpeg_extract\ffmpeg-7.0.2-full_build\bin"

    # Add FFmpeg to PATH
    print("Adding FFmpeg to PATH...")
    add_to_path(ffmpeg_bin_path)

    print("FFmpeg path added. You may continue.")

if __name__ == "__main__":
    main()

import re

def extract_playlist_id(url):
    # Regular expression to match Spotify playlist URL and extract the playlist ID
    pattern = r'spotify\.com/playlist/([^/?]+)'
    match = re.search(pattern, url)
    
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid Spotify playlist URL")

# Example usage
playlist_url = input("Playlist URL : ")
playlist_id = extract_playlist_id(playlist_url)
print("Playlist ID:", playlist_id)



# Spotify API credentials
client_id = 'your spotify client id'
client_secret = 'your spotify client secret'

# Spotify playlist URL or ID
playlist_url = playlist_id

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_playlist_tracks(playlist_url, output_file):
    # Extract playlist ID from the URL
    playlist_id = playlist_url.split('/')[-1].split('?')[0]

    # Fetch the playlist's tracks
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']

    # If the playlist has more than 100 songs, fetch them in batches
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    # Write the track details to the file
    with open(output_file, 'w', encoding='utf-8') as file:
        for idx, item in enumerate(tracks):
            track = item['track']
            # Handle NoneType by checking and replacing None with an empty string or 'Unknown Artist'
            artist_names = [artist['name'] if artist['name'] is not None else 'Unknown Artist' for artist in track['artists']]
            file.write(f"{idx + 1}. {track['name']} by {', '.join(artist_names)}\n")

# Specify the output file path
output_file = 'playlist_tracks.txt'

# Run the function
get_playlist_tracks(playlist_url, output_file)

print(f"Track details have been saved to {output_file}")

import yt_dlp


def download_audio(title, artist):
    search_query = f"{title} {artist}"
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'E:\\spotifymusicinstaller\\music\\{title} - {artist}',
        'noplaylist': True,
        'ffmpeg_location': r"C:\ffmpeg\ffmpeg_extract\ffmpeg-7.0.2-full_build\bin"
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch:{search_query}"])

# Read the text file
input_file = 'playlist_tracks.txt'
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Process each line
for line in lines:
    print("--------------------------------------------------------")
    try:
        # Example line: "1. Wishing Well by Juice WRLD"
        sleep(1)
        parts = line.split(' by ')
        title = parts[0].split('. ')[1]
        artist = parts[1].strip()
        download_audio(title, artist)
    except IndexError:
        print(f"Skipping line due to format error: {line}")

print("--------------------------------------------------------")
print("Download process completed.")
print("--------------------------------------------------------")
