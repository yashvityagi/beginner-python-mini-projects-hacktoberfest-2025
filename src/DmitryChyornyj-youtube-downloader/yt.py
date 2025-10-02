from pytube import YouTube

def download_video():
    url = input("🎥 Enter YouTube video URL: ")
    try:
        yt = YouTube(url)
        print(f"📦 Downloading: {yt.title}")
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("✅ Download complete!")
    except Exception as e:
        print(f"❌ Failed to download: {e}")

if __name__ == "__main__":
    download_video()
