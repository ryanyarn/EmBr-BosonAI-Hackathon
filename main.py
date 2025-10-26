from openai import OpenAI
import base64, os
from dictionaries import emotion, transcript, scene
from client import client

def b64(p): return base64.b64encode(open(p, "rb").read()).decode("utf-8")

em_input = input("Enter an emotion (sad/happy/excited/disgust/angry/scared): ")

text_input = input("Enter what to say: ")

system = (
  "You convert text into speech following directorial notes.\n"
  f"{scene.get(em_input)}"
)

messages = [
  {"role": "system", "content": system},
  # Provide the reference transcript
  {"role": "user", "content": open(transcript.get(em_input), "r", encoding="utf-8").read().strip()},
  
  # Provide the reference audio
  {"role": "assistant", "content": [{
      "type": "input_audio",
      "input_audio": {"data": b64(emotion.get(em_input)), "format": "wav"}
  }]},
  # Spoken text input
  {"role": "user", "content": text_input},
]

resp = client.chat.completions.create(
    model="higgs-audio-generation-Hackathon",
    messages=messages,
    modalities=["text","audio"],
    max_completion_tokens=256,
    temperature=0.8, top_p=0.95,
    stop=["<|audio_eos|>", "<|end_of_text|>", "<|eot_id|>"],
    extra_body={"top_k": 40},
    stream=False,
)

audio_b64 = resp.choices[0].message.audio.data
open("output/" + em_input + text_input + ".wav", "wb").write(base64.b64decode(audio_b64))
print("Finished")