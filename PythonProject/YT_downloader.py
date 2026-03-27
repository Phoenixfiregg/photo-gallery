#!/usr/bin/env python3
"""
YouTube Downloader using yt-dlp
Install dependency first: pip install yt-dlp
"""

import subprocess
import sys
import os


def install_yt_dlp():
    """Install yt-dlp if not already installed."""
    try:
        import yt_dlp
    except ImportError:
        print("Installing yt-dlp...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
        print("yt-dlp installed successfully!\n")


def download_video(url: str, output_dir: str = ".", quality: str = "best"):
    """
    Download a YouTube video.

    Args:
        url:        YouTube video or playlist URL
        output_dir: Folder to save downloaded files (default: current directory)
        quality:    'best', 'worst', or a specific height like '720', '1080'
    """
    import yt_dlp

    os.makedirs(output_dir, exist_ok=True)

    # Build format string
    if quality == "best":
        fmt = "bestvideo+bestaudio/best"
    elif quality == "worst":
        fmt = "worstvideo+worstaudio/worst"
    else:
        # e.g. quality = "720" → prefer that height
        fmt = f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]"

    ydl_opts = {
        "format": fmt,
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
        "noplaylist": False,          # set True to skip playlists
        "progress_hooks": [progress_hook],
        "quiet": False,
        "no_warnings": False,
    }

    print(f"\n📥 Starting download...")
    print(f"   URL      : {url}")
    print(f"   Quality  : {quality}")
    print(f"   Save to  : {os.path.abspath(output_dir)}\n")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_audio_only(url: str, output_dir: str = "."):
    """Download only the audio track as an MP3."""
    import yt_dlp

    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "progress_hooks": [progress_hook],
        "quiet": False,
    }

    print(f"\n🎵 Downloading audio only (MP3)...")
    print(f"   URL      : {url}")
    print(f"   Save to  : {os.path.abspath(output_dir)}\n")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def get_video_info(url: str):
    """Print info about a video without downloading it."""
    import yt_dlp

    ydl_opts = {"quiet": True, "no_warnings": True}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    print(f"\n📋 Video Info")
    print(f"   Title    : {info.get('title', 'N/A')}")
    print(f"   Uploader : {info.get('uploader', 'N/A')}")
    print(f"   Duration : {info.get('duration', 0) // 60}m {info.get('duration', 0) % 60}s")
    print(f"   Views    : {info.get('view_count', 'N/A'):,}" if isinstance(info.get('view_count'), int) else f"   Views    : N/A")
    print(f"   Upload   : {info.get('upload_date', 'N/A')}")

    # Show available formats (resolutions)
    formats = info.get("formats", [])
    heights = sorted(
        {f["height"] for f in formats if f.get("height") and f.get("vcodec") != "none"},
        reverse=True,
    )
    print(f"   Available resolutions: {', '.join(str(h) + 'p' for h in heights)}\n")
    return info


def progress_hook(d):
    """Display a simple progress indicator."""
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "?%").strip()
        speed   = d.get("_speed_str", "?").strip()
        eta     = d.get("_eta_str", "?").strip()
        print(f"\r   ⬇  {percent}  |  speed: {speed}  |  ETA: {eta}   ", end="", flush=True)
    elif d["status"] == "finished":
        print(f"\n   ✅ Download finished: {d['filename']}")
    elif d["status"] == "error":
        print(f"\n   ❌ Error: {d.get('error')}")


# ── Interactive CLI ──────────────────────────────────────────────────────────

def main():
    install_yt_dlp()

    print("=" * 55)
    print("         🎬  YouTube Downloader (yt-dlp)         ")
    print("=" * 55)

    url = input("\nPaste YouTube URL: ").strip()
    if not url:
        print("No URL provided. Exiting.")
        return

    # Show info first
    try:
        get_video_info(url)
    except Exception as e:
        print(f"Could not fetch info: {e}")

    print("Choose an option:")
    print("  1. Download video (best quality)")
    print("  2. Download video (custom resolution)")
    print("  3. Download audio only (MP3)")
    print("  4. Exit")

    choice = input("\nEnter choice [1-4]: ").strip()

    output_dir = input("Save to folder [press Enter for current directory]: ").strip() or "."

    try:
        if choice == "1":
            download_video(url, output_dir, quality="best")
        elif choice == "2":
            res = input("Enter max resolution (e.g. 1080, 720, 480): ").strip()
            download_video(url, output_dir, quality=res)
        elif choice == "3":
            download_audio_only(url, output_dir)
        elif choice == "4":
            print("Goodbye!")
        else:
            print("Invalid choice.")
    except Exception as e:
        print(f"\n❌ Download failed: {e}")
        print("Tip: Make sure yt-dlp is up to date: pip install -U yt-dlp")


if __name__ == "__main__":
    main()