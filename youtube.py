import sys
import yt_dlp

def progress_hook(d):
    if d['status'] == 'downloading':
        percentage = d['_percent_str'].strip()
        print(f"Download Progress: {percentage}", end="\r")

def download_video(url, audio_only):
    try:
        ydl_opts = {
            'progress_hooks': [progress_hook],
            'format': 'bestaudio/best' if audio_only else 'bestvideo+bestaudio/best'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\nDownload complete!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python youtube_downloader.py <video_url> [audio_only: true/false]")
    else:
        url = " ".join(sys.argv[1:]).split()[0]  # Ensure link works without quotes
        audio_only = sys.argv[-1].lower() == 'true' if len(sys.argv) > 2 else False
        download_video(url, audio_only)
