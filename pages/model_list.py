import streamlit as st 
import os 
import logging 

directory = os.environ.get('EFS_PATH')
if not directory: 
    logging.error("The path to the EFS directory is not set")
    st.write("Unable to find model directory. Set the EFS_PATH variable and try again.")
    var = st.text_input("Enter absolute path to model directory",key='user_input')
    if var: 
        st.write(f"Directory:{var}")
        directory = var 
 
st.header("Models accessible on the shared drive:")
subfolders = [f.path for f in os.scandir(directory) if f.is_dir()]
models = [item.split(directory)[1] for item in subfolders]
if "efs" in directory:
    st.write("Models:")
    for each_model in models: 
        st.write(each_model)
