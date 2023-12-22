# https://ollama.ai/blog/ollama-is-now-available-as-an-official-docker-image

from langchain.llms import Ollama
from langchain.callbacks import StreamlitCallbackHandler
import os
import streamlit as st

llm = Ollama(model="orca-mini:3b")

if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = llm(prompt)
        st.write(response)
