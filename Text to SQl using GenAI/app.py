from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_reponse(question, prompt):
    model= genai.GenerativeModel("gemini-pro")
    reponse= model.generate_content([prompt[0], question])
    return reponse.text

def read_sql_query(sql, db):
    conn= sqlite3.connect(db)
    cur= conn.cursor()
    print("excuting below query..")
    print(sql)
    cur.execute(sql)
    rows= cur.fetchall()
    for row in rows:
        print(row)
    return rows

prompt= [
    """
    you are the expert in converting English questions to sql query!
    The SQL database has a table name STUDENT and has the following column names- NAME, CLASS,
    SECTION and MARKS \n\n for example \n Example-1 How many entries of records present?, 
    the sql command will be like this SELECT COUNT(*) FROM STUDENT; \n Example-2 Tell me all the 
    students studying in Data science?, the SQL query will be something like this SELECT * FROM STUDENT 
    WHERE CLASS="Data Science";
    also the sql code should not have ``` in begining or end and sql word in the output

    """]
# also the sql code should not have ``` in begining or end and sql word in the output

st.set_page_config(page_title="I can Retrieve any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question= st.text_input("Input: ", key="input")

submit= st.button("Ask a Question")

if submit:
    response= get_gemini_reponse(question, prompt)
    print(response)
    data= read_sql_query(response, "student.db")
    st.subheader("The Response is:")
    for row in data:
        print(row)
        st.header(row)
