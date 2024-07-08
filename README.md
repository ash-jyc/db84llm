# db84llm
## Overview
[[doc]](https://docs.google.com/document/d/1crGWlnyNGzeMiyU7aU-ASB3LHUfqGN0PjMI9Fk-QO90/edit#heading=h.1o0zogi4z3b1)

## Dependencies
- Python
- Jupyter
- [openai/whisper](https://github.com/openai/whisper?tab=readme-ov-file)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

### Audio Files
```shell
# yt-dlp
yt-dlp -x --audio-format mp3 https://www.youtube.com/watch?v=example_video_id
```

### Transcripts
```shell
# whisper
pip install -U openai-whisper
```
Then run [openai-whisper.ipynb](./transcription/openai-whisper.ipynb) with the specified audio file.
```shell
# yt-dlp
yt-dlp --write-sub --skip-download --sub-lang en --convert-subs srt https://www.youtube.com/watch?v=example_video_id
```
Use [vtt_to_text.py](./transcription/vtt_to_text.py) to convert to plain text.

