import streamlit as st
import requests 
import json 
from streamlit_chat import message 
import uuid
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def input_changed():
    chat_message = st.session_state.user_input
    st.session_state.all_text.append({"data":chat_message,"user":True,"key":str(uuid.uuid4())})
    # Wait for the bot's response and send it 
    #url = f'https://jsonplaceholder.typicode.com/todos/{len(st.session_state.all_text)}'
    url = "https://api.github.com"
    data = requests.get(url,headers)
    server_message = None
    if(data.ok):
        server_message = 'Success: I got a response from the server.'
        st.write(server_message)
    else:
        server_message = f'Something went wrong: {data.status}'
        st.write(server_message)
    st.session_state.all_text.append({"data":server_message,"user":False,"key":str(uuid.uuid4())})

with st.sidebar: 
        option = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)



# Create a chat without streamlit chat, just using session state 
# Initialization
if 'all_text' not in st.session_state:
    st.session_state['all_text'] =  [{"data":"I'm a bot. speak to me.","user":True,"key":str(uuid.uuid4())}]

for each_message in st.session_state.all_text:
    message(each_message['data'],is_user=each_message['user'],key=each_message['key'])


st.text_input("User input",on_change=input_changed,key="user_input")


