from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

st.set_page_config(page_title='Multi Language Invoice Extractor')

st.header('Multi Language Invoice Extractor')

input= st.text_input("Input", key="input")

upload_file = st.file_uploader("choose a image", type=['jpg', 'jpeg', 'png'])
image=""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded", use_column_width=True)

def input_image_details(upload_file):
    if upload_file is not None:
        bytes_data = upload_file.getvalue()

        image_parts = [
            {
                "mime_type": upload_file.type,
                "data": bytes_data

            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

submit = st.button("Tell me about the Invoice")

input_prompt = """
you are the expert in understanding the Invoices. I will upload the Invoice as image and 
ask the questions based on the uploaded image.
"""

if submit:
    image_data = input_image_details(upload_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is")
    st.write(response)
