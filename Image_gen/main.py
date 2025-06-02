# duild a simple app use generated images use streamlit snd openai api
import streamlit as st
import openai
import os
import requests
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
st.title("Image Generation with OpenAI API")


st.write("This app generates images based on user prompts using OpenAI's DALL-E model.")
user_prompt = st.text_input("Enter your image description:")
if user_prompt:
    response = openai.Image.create(
        prompt=user_prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    st.image(image_url, caption='Generated Image', use_column_width=True)


    # download the image
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open("generated_image.png", "wb") as f:
            f.write(image_response.content)
        st.success("Image downloaded successfully!")
    else:
        st.error("Failed to download the image.")
    st.write("Image URL:", image_url)
    st.write("Image saved as 'generated_image.png' in the current directory.")
    


