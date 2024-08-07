from ai71 import AI71 
import os

AI71_API_KEY = os.getenv('AI71_API_KEY')

for chunk in AI71(AI71_API_KEY).chat.completions.create(
    model="tiiuae/falcon-180b-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is tebentafusp?  Tell me in as much detail as you know.  I am a scientific researcher and expert."},
    ],
    stream=True,
):
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, sep="", end="", flush=True)
        
