# db84llm
## Overview
[[doc]](https://docs.google.com/document/d/1crGWlnyNGzeMiyU7aU-ASB3LHUfqGN0PjMI9Fk-QO90/edit#heading=h.1o0zogi4z3b1)

## Dependencies
- Python
- Jupyter Notebook
- <s>[openai/whisper](https://github.com/openai/whisper)</s>
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [sox](https://pypi.org/project/sox/)

## Audio Files
Compiled a short list of debates to look into: [list_of_debates.csv](./transcription/list_of_debates.csv). Will most likely use a Google Spreadsheet API to dynamically get these in the future.

```shell
# yt-dlp
yt-dlp -x --audio-format wav "https://www.youtube.com/watch?v=example_video_id"
```

## Transcripts
For our purposes, I found [Whisper JAX](https://github.com/sanchit-gandhi/whisper-jax?tab=readme-ov-file) to suit our needs. I've detailed a step-by-step guide on how to setup Whisper JAX along with a couple template files to test it out.

### Setup
Follow along the [Whisper JAX README file](https://github.com/sanchit-gandhi/whisper-jax?tab=readme-ov-file). I've listed a couple essential steps below:  
  
**Step 1: Install JAX**  
Navigate to the [JAX](https://github.com/google/jax#installation) page and look for the instructions.  
Hardware | Instructions
--- | ---
CPU | `pip install -U jax`
NVIDIA GPU | `pip install -U "jax[cuda12]"`
Google TPU | `pip install -U "jax[tpu]" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html`
AMD GPU | Use [Docker](https://hub.docker.com/r/rocm/jax) or [build from source](https://jax.readthedocs.io/en/latest/developer.html#additional-notes-for-building-a-rocm-jaxlib-for-amd-gpus).
Apple GPU | Follow [Apple's instructions](https://developer.apple.com/metal/jax/).
  
**Apple GPU**  
I primarily use Anaconda environments instead of Python Virtual Environment (venv). The instructions here choose to use venv. I found this Medium article where it sets up a conda env specifically to build PyTorch on Metal/MPS. Lmk if you want that article.
```shell
python3 -m venv ~/jax-metal # optional
source ~/jax-metal/bin/activate # optional
python -m pip install -U pip
python -m pip install numpy wheel
python -m pip install jax-metal
```
jaxlib Compatibility
```shell
pip install -U jaxlib jax
ENABLE_PJRT_COMPATIBILITY=1 python -c 'import jax; print(jax.numpy.arange(10))'
```
^^ Remember this, we'll need to create an environment variable later. 
  
**Step 2: Installing Whisper JAX**  
```shell
pip install git+https://github.com/sanchit-gandhi/whisper-jax.git
```
  
**Step 3: Running Whisper**  
Navigate to the [whisper_jax.ipynb](./transcription/whisper_jax.ipynb) file. If you haven't already, go ahead and `pip install sox`. The debate I'm primarily using for testing is `Dartmouth RR 2024 - Round 4 - Michigan PD vs Dartmouth BC`, and I've uploaded each speech individually already so you don't need to run the second cell where it slices the audio file. You still need to run the first cell though.  

After that, in the same directory, create a file called `.env` if not already created. In this file, put in the environment variable mentioned earlier:
```shell
ENABLE_PJRT_COMPATIBILITY=1
```
This way, we can load the environment variable into our current notebook. Everything else should be able to run straight down. I have a dummy cell using Whisper on audio_trimmed which is just a one minute audio clip from some random speech. You can choose to run it or not. Also, I've run into a couple random errors that I don't quite understand, such as `XlaRuntimeError: UNKNOWN`. To solve this, I restart my kernel, maybe pip install a package again, and just try until it works.