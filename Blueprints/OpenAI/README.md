# Interacting with OpenAI

Let's set up a couple lightweight apps with OpenAI's tools. There are a variety of ways to put these pieces together to unlock your imagination! 

> Prerequisite: you'll need an OpenAI [API key](https://platform.openai.com/api-keys). If you don't have one, either make one or use an ULTA key---not sure if we will have a group key yet. Once you have it, make a file called `api.key` with the key pasted in it. Every time you work on your project, run this command first in your terminal: `` export OPENAI_API_KEY=`cat api.key` ``.

## Voice with OpenAI

We'll use the Whisper API. It lets you both listen to voices and generate your own voices.

### Speech to Text

First, let's say you want to listen to the user say something. Here's how you can turn speech into text.

```{python}
from openai import OpenAI
client = OpenAI()

audio_file= open("audio_file.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

print(transcription.text)
```

This script accesses OpenAI's core functionality. But let's make it more interactive. Let's install some audio libraries with the following steps in the terminal, for MacOS. Ask your favorite chatbot for Windows install instructions.

```{bash}
brew install portaudio
export LDFLAGS="-L/opt/homebrew/lib"
export CPPFLAGS="-I/opt/homebrew/include"
pip install pyaudio wave keyboard
```

Now we can set up a recording studio that lets you record snippets of audio, which OpenAI will transcribe.

Run `python recording_studio.py` to try it out, and take a look at how the code does it.

### Text to Speech

Next, let's say you want an AI to read aloud your response. More detail on [OpenAI's guide](https://platform.openai.com/docs/guides/text-to-speech/quickstart). Here's how you can turn text into speech:

```{python}
from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / f"output.mp3"
response = client.audio.speech.create(
  model="tts-1-hd",
  voice="echo",
  input="I'm ready to put in my all for the Ukraine Leadership and Technology Academy 2024, because our nation and our world need us more than ever now. And together, we can rise to the challenge. Слава Україні!"
)

response.stream_to_file(speech_file_path)
```

## Chat with OpenAI

Let's make a quick app to demonstrate the now classic chatbot. Here's the key part where we make the call to OpenAI:

```{python}
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a fact about Ukrainian history."}
  ]
)

print(completion.choices[0].message)
```

Check out `chatbot.py` and try running it to see the app in action.

You have lots of options for which chatbots to use. The top three are Claude 3.5 Sonnet, GPT-4o, and Google Gemini. They are all cheap to test on, costing well under $0.01 USD per response. But if you put it into production, take care to monitor the costs you accrue on your API key.
