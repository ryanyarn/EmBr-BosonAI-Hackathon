EmBr is made using only: higgs-audio-generation-Hackathon

To use the localhost demo, run app.py and then the command: <streamlit run app.py>

main.py was used for testing
output has example generations 
sample holds all the reference audios and their respective transcriptions (to add your own voice it would be done here)
dictionaries.py hosts all the dictionaries used for organization and the different scene prompting used to invoke the emotions
best results were found using parameters of temperature = 0.8, top_p = 0.95, and top_k = 30-40
note that the generation has aspects of randomness so the results can vary heavily, also puncutation has major influence (especially apostrophies)

future developments aim to add further emotion encoding, test output variability based on punctuation input, implementing sarcasm as an additional tag, and implementing a system for user reference input 

Created in person working and later added to github in one go,
Created by: Ryan Qian, Kane Pan, and Gianna Fung

Voicing & Scene Descriptions by Kane
Large portion of testing and prompt engineering done by Gianna
UI and simple app implementation done by Ryan

General coding collaborated 
