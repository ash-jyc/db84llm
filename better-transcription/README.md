# Improving Transcriptions
Whisper transcriptions thus far are capable of capturing the sounds of words, but not the actual words. In order to overcome this hurdle, the goal is to create a model to learn what the actual words behind the sounds are. Many of these tend to be debate words, just to name a few:  
* Circus quo -> are the squo
* And how you manage -> advantage
* The act -> aff
* Contingent 2 -> contention 2
  
As you may observe in the data, many of the tags are largely correct, but the contents of the card are are typically lost due to spreading.

# ToDo
General procedure:
1. Transcribe and clean transcripts. Examples of cleaned transcripts can be found with the `-clean` suffix inside debate transcription folders.
2. Apply invisibility mode to files in the [docs](./docs/) folder. You can find the script to do so [here](./invis_folder). Ask Michi how to use this script. 
3. Run the [prepare_data.ipynb](./prepare_data.ipynb) file. To update the [list_of_debates.csv](../list_of_debates.csv) file, reference the general [README.md](../README.md) file. Also, consider making a new sheet with new debates, and I can work on transcribing them.
4. The notebook should output two json files, one called `data_transcripts.json` and the other `data_verbatim.json`. The transcripts one should be a list full of input text, while the Verbatim one should be one full of target text. Inside the `data_transcripts.json` file, start copying and pasting corresponding cards from the `data_verbatim.json` file. You can find an example in [data_cleaned.json](./data_cleaned.json). Once your done, you can directly add everything into the cleaned file.

I know these instructions are not entirely clear, so let me know if you have any questions. I've already started on the clean dataset, it's just I think I forgot to invis mode a file, and I don't want to restart....

## Thoughts
First, since Whisper is good enough to capture the speed of tags, this should prove the case for all other analytics and rebuttals. If this is true, we can shift more of our focus on organizing files into data instead of fixing the text of debates.  

Second, that being said, we still need a model to put emphasis on debate terms that are used in later speeches. Since we have transcript files and Verbatim files, this tool should be easy enough to build, but just might require some time.