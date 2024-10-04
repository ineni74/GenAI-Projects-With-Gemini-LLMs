import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input_prompt, image):
    model= genai.GenerativeModel('gemini-1.5-flash')
    response= model.generate_content([input_prompt,image])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file:
        bytes_data= uploaded_file.getvalue()
        
        image_parts = [
            {
                'mime_type': uploaded_file.type,
                'data': bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File uploaded")

st.set_page_config(page_title= "GenAI Nutritionist")

st.header('Gemini Health App')
upload_file= st.file_uploader("Choose a image", type=['jpg', 'jpeg', 'png'])
image= ''
if upload_file:
    image= Image.open(upload_file)
    st.image(image, caption="uploaded image", use_column_width=True)
    
submit= st.button("Tell me about the total calories")


input_prompt= """
You are the expert in nutritionist where you need to see the food items from the image
and calculate the total calories, also provide the details od every food items with calories intake
in the below format.

    1. Item 1 - no of calories
    2. Itema 2 - no of calories
    ------
    -----
Finally you can also mention whether the food is healthy or not and also mention the percentage split of the 
ratio of carbohydrates, fats, fibers, sugar and other important things required in our diet.

"""

if submit:
    image_data= input_image_setup(upload_file)
    response= get_gemini_response(input_prompt, image_data)
    st.header("The Response is:")
    st.write(response)
    
