import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file and set OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configure the Streamlit app
st.set_page_config(page_title="Transcribe & Translate", layout="centered")
st.title("🗣️🎯 Audio Transcription & Translation")

st.markdown("""
Upload an audio file, get its transcription in English, and translate it into your preferred language using OpenAI.
""")

# File uploader for audio files (mp3, wav, m4a)
audio_file = st.file_uploader("📤 Upload Audio", type=["mp3", "wav", "m4a"])

# Dropdown for selecting translation language
language = st.selectbox(
  "🌍 Translate to:",
  ["Arabic", "French", "Spanish", "German", "Chinese", "None (Keep English)"]
)

if audio_file:
  # Display audio player in the app
  st.audio(audio_file, format="audio/mp3")

  # Transcribe the uploaded audio file using OpenAI Whisper
  with st.spinner("Transcribing..."):
    response = openai.Audio.transcribe(
      model="whisper-1",
      file=audio_file,
      response_format="text"
    )
    st.success("✅ Transcription completed!")
    st.markdown("### 📜 Transcribed Text")
    st.write(response)

    # Save transcription to a text file and provide download button
    with open("transcription.txt", "w") as f:
      f.write(response)
    st.download_button("⬇️ Download Transcription", response, file_name="transcription.txt")

  # If a translation language is selected, translate the transcription
  if language != "None (Keep English)":
    with st.spinner(f"Translating to {language}..."):
      translation_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "system", "content": "You are a professional translator."},
          {"role": "user", "content": f"Translate the following text to {language}: {response}"}
        ]
      )
      translated_text = translation_response.choices[0].message.content
      st.success("✅ Translation completed!")
      st.markdown("### 🌐 Translated Text")
      st.write(translated_text)

      # Save translation to a text file and provide download button
      with open("translation.txt", "w") as f:
        f.write(translated_text)
      st.download_button("⬇️ Download Translation", translated_text, file_name="translation.txt")
