from google import genai
from dotenv import load_dotenv
import os
import io
from gtts import gTTS

# loading env file
load_dotenv()
my_api_key=os.getenv("GEMINI_API_KEY")


# initializing a client
client=genai.Client(api_key=my_api_key)

# note generator
def note_generator(pil_images):
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=pil_images + ["Summarize the picture in note format at max 100 words, make sure to add necessary marked down to differentiate different section"]
    )

    return response.text

# audio generator
def audio_generator(text):
    speech=gTTS(text,lang='en',slow=False)
    audio_buffer=io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

# Quiz question genarate
def Quiz_question_genaretor(text):
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[text ,"Summarize the text and generate topic wise question(at most 8 MCQ type) and its looks like Quiz and show the answe after the question, make sure to add necessary marked down to differentiate different section"]
    )
    return response.text
