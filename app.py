import streamlit as st
from openai import OpenAI 
import os

#connect to openai api

api_key = os.environ.get("OPENAI_API_KEY")  or st.secrets.get["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)

#set the pagetitle

st.title("My AI Chatbot")
st.title("Ask me anything!")


#create message history if ir does not exist
if "messages" not in st.session_state:
    st.session_state.messages = []

#display the messages in the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


#take input from user
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({
        "role": "user", 
        "content": user_input
    })   

#show user message on screen

    with st.chat_message("user"):
        st.write(user_input)

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )
    reply = response.choices[0].message.content
except Exception as e:
    reply = f"Error: {e}"

    #extract the reply text
    # reply = response.choices[0].message.content
    # st.session_state.messages.append({
    #     "role": "assistant",
    #     "content": reply
    # })

    #show reply on screen
    with st.chat_message("assistant"):
        st.write(reply)

