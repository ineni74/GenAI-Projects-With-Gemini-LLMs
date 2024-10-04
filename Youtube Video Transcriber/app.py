import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

prompt= """
You are the Youtube videos summarizer. you will be taking the transcript text and summarize the entire video
and provide the important summary in points. Please provide the summary of the text given here:
"""

def generate_gemini_content(transcript_text, prompt):
    model= genai.GenerativeModel('gemini-pro')
    response= model.generate_content(prompt+transcript_text)
    return response.text


def extract_transcript_details(youtub_video_url):
    try:
        video_id= youtub_video_url.split("=")[1]
        transcript_text= YouTubeTranscriptApi.get_transcript(video_id)
        
        transcript= ""
        for i in transcript_text:
            transcript += i["text"]      
        return transcript
        
    except Exception as e:
        print(e)

st.title("Youtube Transcript to detailed Notes Converter")

youtube_link= st.text_input("Enter the Youtube Link:")

if youtube_link:
    video_id= youtube_link.split("=")[1]
    print(video_id)
    print(f"https://img.youtube.com/vi/{video_id}/0.jpg")
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    
if st.button("Get Detailed Notes"):
    transcript_text= extract_transcript_details(youtube_link)
    
    if transcript_text:
        summary= generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Notes")
        st.write(summary)