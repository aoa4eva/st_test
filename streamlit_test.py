import streamlit as st
import click
import webbrowser
from streamlit.components.v1 import html 


st.set_page_config(page_title="Streamlit Test",page_icon=":fire:")

st.header("Streamlit test for LLMs")

# Option 1
def launch_page():
    click.launch("https://www.google.com")


# Option 2
clicked = st.button('Click me')
if(clicked): 
    webbrowser.open_new("http://www.google.com")

# Option 3

def open_page(item):
    open_script=f"""<script type="text/javascript">window.open('{item}','_blank').focus();</script>"""
    st.write(open_script)
    html(open_script)

st.button('Open link', on_click=open_page, args=('https://streamlit.io',))
