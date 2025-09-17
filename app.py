import streamlit as sl
import tiktoken
import random

# Pricing for OpenAI models (per 1k tokens) - as of early 2024, subject to change
OPENAI_PRICING = {
    "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},
    "gpt-4": {"input": 0.03, "output": 0.06},
    "gpt-4o": {"input": 0.005, "output": 0.015},
    "gpt-4-turbo": {"input": 0.01, "output": 0.03},
    "text-embedding-ada-002": {"input": 0.0001, "output": 0.0001}, # Embedding models usually have same input/output price
}

def get_token_colors(num_tokens):
    """Generates a list of distinct colors for tokens."""
    colors = ["#FFDDC1", "#DCF8C6", "#A7DBD8", "#E0BBE4", "#957DAD", "#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1"]
    return [colors[i % len(colors)] for i in range(num_tokens)]

def highlight_tokens(text, tokens, encoding):
    """Generates HTML to display text with highlighted tokens."""
    html_output = ""
    token_colors = get_token_colors(len(tokens))
    
    for i, token_id in enumerate(tokens):
        token_text = encoding.decode([token_id])
        color = token_colors[i]
        html_output += f"<span style='background-color: {color}; padding: 2px; border-radius: 3px; margin: 1px; display: inline-block;'>{token_text}</span>"
    return html_output

def calculate_cost(model, num_tokens):
    """Calculates estimated cost for OpenAI models."""
    if model in OPENAI_PRICING:
        # Assuming input tokens for cost estimation
        cost_per_1k_tokens = OPENAI_PRICING[model]["input"]
        estimated_cost = (num_tokens / 1000) * cost_per_1k_tokens
        return f"${estimated_cost:.6f}"
    return "N/A"

def app():
    sl.set_page_config(page_title="LLM Tokenizer", layout="wide")
    sl.title("LLM Tokenizer App")
    sl.write("Enter text to tokenize and select a model to see the token count and token details.")

    text = sl.text_area("Enter text to tokenize:", height=200, key="text_input")
    
    models = [
        "gpt-3.5-turbo",
        "gpt-4",
        "text-embedding-ada-002",
        "gpt-4o",
        "gpt-4-turbo",
        "claude-3-opus-20240229",
        "claude-3-sonnet-20240229",
        "claude-3-haiku-20240307",
        "gemini-pro",
        "llama-2-7b",
        "mistral-7b",
    ]
    selected_model = sl.selectbox("Select a model:", models, key="model_select")

    col1, col2 = sl.columns([1, 1])

    with col1:
        if sl.button("Tokenize", key="tokenize_button", use_container_width=True):
            if text:
                try:
                    encoding = tiktoken.encoding_for_model(selected_model)
                    tokens = encoding.encode(text)
                    sl.success(f"Tokenization successful using {selected_model}!")
                    
                    sl.write(f"**Number of tokens:** {len(tokens)}")
                    sl.write(f"**Characters:** {len(text)}")
                    sl.write(f"**Words:** {len(text.split())}")

                    estimated_cost = calculate_cost(selected_model, len(tokens))
                    if estimated_cost != "N/A":
                        sl.write(f"**Estimated Cost (Input):** {estimated_cost}")
                    
                    sl.subheader("Token Details:")
                    token_details_str = " ".join([f"`{encoding.decode([token_id])}` (ID: {token_id})" for token_id in tokens])
                    sl.markdown(token_details_str)

                    sl.subheader("Token Visualization:")
                    highlighted_html = highlight_tokens(text, tokens, encoding)
                    sl.markdown(highlighted_html, unsafe_allow_html=True)

                except KeyError:
                    sl.error(f"Model '{selected_model}' is not supported by tiktoken for encoding. Please choose an OpenAI model or a model supported by tiktoken.")
                except Exception as e:
                    sl.error(f"An error occurred: {e}")
            else:
                sl.warning("Please enter some text to tokenize.")
    
    with col2:
        if sl.button("Reset", key="reset_button", use_container_width=True):
            sl.session_state.text_input = ""
            sl.session_state.model_select = models[0]
            sl.experimental_rerun()

if __name__ == "__main__":
    app()