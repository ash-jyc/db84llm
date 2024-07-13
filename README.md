# db84llm
## Overview
[[doc]](https://docs.google.com/document/d/1crGWlnyNGzeMiyU7aU-ASB3LHUfqGN0PjMI9Fk-QO90/edit#heading=h.1o0zogi4z3b1)

## Dependencies
- Python
- Jupyter
- [openai/whisper](https://github.com/openai/whisper)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [sox](https://pypi.org/project/sox/)

### Audio Files
Compiled a short list of debates to look into: [list_of_debates.csv](./transcription/list_of_debates.csv)

```shell
# yt-dlp
yt-dlp -x --audio-format wav "https://www.youtube.com/watch?v=example_video_id"
```

### Speed Reduction
```shell
# sox
pip install sox
```

### Transcripts
```shell
# whisper
pip install -U openai-whisper
```
Then run [openai_whisper.ipynb](./transcription/openai_whisper.ipynb) with the specified audio file.
```shell
# yt-dlp
yt-dlp --write-sub --skip-download --sub-lang en --convert-subs srt "https://www.youtube.com/watch?v=example_video_id"
```
Use [vtt_to_text.py](./transcription/vtt_to_text.py) to convert to plain text.

