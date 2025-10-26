emotion = {"sad": "sample/ref-sad.wav",
           "happy": "sample/ref-happy.wav",
           "disgust": "sample/ref-disgust.wav",
           "scared": "sample/ref-scared.wav",
           "excited": "sample/ref-excited.wav",
           "angry": "sample/ref-angry.wav"} #dict map user input to sound

transcript = {"sad": "sample/ref-sad.txt",
              "happy": "sample/ref-happy.txt",
              "disgust": "sample/ref-disgust.txt",
              "scared": "sample/ref-scared.txt",
              "excited": "sample/ref-excited.txt",
              "angry": "sample/ref-angry.txt"} #dict map input to transcript

scene = {
    "sad": (
        "<|scene_desc_start|> "
        "Voiceover booth; low energy; slower pace; softer volume; lower pitch; sad, mournful tone; "
        "<|scene_desc_end|>"
    ),

    "disgust": (
        "<|scene_desc_start|> "
        "Voiceover booth; tight, nasal resonance; shortened vowels; disgust; grossed out; subtle exhalations; "
        "<|scene_desc_end|>"
    ),

    "excited": (
        "<|scene_desc_start|> "
        "Voiceover booth; high energy; faster pace; wide pitch variability; bright, smiling tone; "
        "<|scene_desc_end|>"
    ),

    "scared": (
        "<|scene_desc_start|> "
        "Voiceover booth; trembling, frightened delivery; hushed volume; tense; irregular, shallow breathing; jittery pace; "
        "cautious"
        "<|scene_desc_end|>"
    ),

    "angry": (
        "<|scene_desc_start|> "
        "Voiceover booth; strong, firm; elevated intensity; forceful emphasis; hard consonants; "
        "short, decisive pauses; downward, final phrase endings. "
        "<|scene_desc_end|>"
    ),

    "happy": (
        "<|scene_desc_start|> "
        "Voiceover booth; warm, cheerful tone; moderately quick pace;"
        "gentle smile audible; light;"
        "subtle upward cadences at phrase ends. "
        "<|scene_desc_end|>"
    ),
}