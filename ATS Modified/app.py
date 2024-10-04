import streamlit as st
import google.generativeai as genai
import os
import PyPDF2
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input):
    model= genai.GenerativeModel('gemini-pro')
    response= model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader= PyPDF2.PdfReader(uploaded_file)
    text= ""
    for page in reader(len(reader.pages)):
        page= reader.pages[page]
        text+= str(page.extract_text())
    return text


input_prompt= """
hey Act like skilled or very experienced ATS (Application Tracking System) with a deep understanding of any one 
job role data science, Full stack web development, Big data engineering, DevOps, Data analyst and deep ATS 
functionality. your task is to evaluate the resume against the provided job description. You must consider the 
job market is very compitative and you should provide best assistance for improving the resume. Assign the percentage 
Matching based on the Job description and missing keywords with high accuracy.
resume: {text}
description: {JD}

I want the response in one single string having the structure
{{"JD Match": "%", "Missing Keywords":"[]", "Profile Summary": ""}}

"""

st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd= st.text_area("Provide Job Description")
uploaded_file= st.file_uploader("Upload your Resume", type="pdf", help="Please uoload PDF only")

submit= st.button("Submit")

if submit:
    if uploaded_file is not None:
        text= input_pdf_text(uploaded_file)
        response= get_gemini_response(input_prompt)
        st.subheader(response)
        