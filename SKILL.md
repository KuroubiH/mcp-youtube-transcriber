---
name: youtube-transcriber
description: Download YouTube audio/playlists (MP3 with ID3/cover), cut/merge segments, or hybrid transcribe (native subs -> Faster-Whisper).
---

# YouTube Transcriber (`ytmp3.py`)

Script: `C:/Users/jefec/.gemini/config/skills/youtube-transcriber/ytmp3.py`
Default output dir: `C:/Users/jefec/.gemini/config/skills/youtube-transcriber/output/`

## CLI Commands

```bash
# Hybrid Transcribe (Fast Path: YouTube captions -> Fallback: Faster-Whisper int8)
# Flags: -m (tiny|base|small|medium|large), -l (pt|en|es|auto), --timestamps, --force-whisper
python "C:/Users/jefec/.gemini/config/skills/youtube-transcriber/ytmp3.py" transcribe "<URL_OR_MP3>" -m small -l pt --timestamps

# Download single video MP3 (with ID3 metadata & embedded thumbnail)
python "C:/Users/jefec/.gemini/config/skills/youtube-transcriber/ytmp3.py" download "<URL>" -o "out.mp3"

# Download entire YouTube playlist (incremental archive skips already downloaded tracks; use --no-archive to force all)
python "C:/Users/jefec/.gemini/config/skills/youtube-transcriber/ytmp3.py" playlist "<PLAYLIST_URL>" -d "<OPTIONAL_OUTPUT_DIR>"

# Cut MP3 segment (time: mm:ss, hh:mm:ss, seconds, or 'end')
python "C:/Users/jefec/.gemini/config/skills/youtube-transcriber/ytmp3.py" cut "input.mp3" 0:00 2:30 -o "cut.mp3"

# Auto download + cut + merge segments
python "C:/Users/jefec/.gemini/config/skills/youtube-transcriber/ytmp3.py" auto "<URL>" 0:00-1:30 4:00-end -o "final.mp3"
```
