import streamlit as st
from openai import OpenAI
import base64
import os
from dictionaries import emotion, transcript, scene
from client import client

st.set_page_config(page_title="EmBr", layout="centered")

# styling
st.markdown("""
    <style>
    /* Center container */
    .block-container {
        max-width: 700px;
        margin: auto;
        padding-top: 2rem;
    }

    /* Title and subtitle */
    .title {
        text-align: center;
        font-size: 2.5em;
        font-weight: 700;
        color: #A7D8F4;
        margin-bottom: 0.1em;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2em;
        color: #666;
        margin-bottom: 2em;
    }

    /* Buttons */
    div.stButton > button {
        width: 100%;
        background-color: #A7D8F4;
        color: white;
        border-radius: 10px;
        height: 3em;
        font-size: 1.1em;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #6ABCE8;
        color: white;
    }

    /* Labels */
    .stSelectbox label, .stTextArea label {
        font-weight: 600;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# title
st.markdown('<div class="title"> EmBr Speech Generation</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Generating expressive speech to bridge emotions using Boson AI</div>', unsafe_allow_html=True)

def b64(p): 
    return base64.b64encode(open(p, "rb").read()).decode("utf-8")

# dropdown for emotion selection
emotions = { # need dictionary so that emojis dont interfere with the dictionary used for classification
    "😊 happy": "happy",
    "☹️ sad": "sad",
    "🤢 disgust": "disgust",
    "🤩 excited": "excited",
    "😡 angry": "angry",
    "😮 surprised": "surprised"
}

em_display = st.selectbox("Select an Emotion", list(emotions.keys()))
em_input = emotions[em_display]  # maps to plain string key

# input
text_input = st.text_area("Enter the line you want to speak:", "", height=100)

# button ui 
if st.button("Generate Audio"):
    if not text_input.strip():
        st.warning("Please enter some text before generating audio.")
    else:
        with st.spinner("Generating expressive speech..."):
            system = (
                "You convert text into speech following directorial notes.\n"
                f"{scene.get(em_input)}"
            )

            messages = [
                {"role": "system", "content": system},
                {"role": "user", "content": open(transcript.get(em_input), "r", encoding="utf-8").read().strip()},
                {"role": "assistant", "content": [{
                    "type": "input_audio",
                    "input_audio": {"data": b64(emotion.get(em_input)), "format": "wav"}
                }]},
                {"role": "user", "content": text_input},
            ]

            resp = client.chat.completions.create(
                model="higgs-audio-generation-Hackathon",
                messages=messages,
                modalities=["text", "audio"],
                max_completion_tokens=1000,
                temperature=0.8,
                top_p=0.95,
                stop=["<|audio_eos|>", "<|end_of_text|>", "<|eot_id|>"],
                extra_body={"top_k": 30},
                stream=False,
            )

            audio_b64 = resp.choices[0].message.audio.data
            output_path = f"output/{em_input}_{text_input[:10].strip().replace(' ', '_')}.wav"
            os.makedirs("output", exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(base64.b64decode(audio_b64))

            st.success("Audio generated successfully!")
            st.audio(output_path, format="audio/wav")
