import streamlit as sl
import tiktoken

def app():
    text = sl.text_input("Enter text to tokenize:", key="text_input")
    
    if sl.button("Tokenize", key="tokenize_button"):
        if text:
            encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
            tokens = encoding.encode(text)
            sl.write(f"Number of tokens: {len(tokens)}")
            sl.write(f"Tokens: {tokens}")
        else:
            sl.write("Please enter some text to tokenize.")

if __name__ == "__main__":
    app()