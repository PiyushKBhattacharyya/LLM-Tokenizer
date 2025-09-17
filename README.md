# LLM Tokenizer App

A comprehensive and user-friendly Streamlit application for tokenizing text using various Large Language Models (LLMs). This app provides detailed token analysis, visualization, and cost estimation for OpenAI models.

## Live Demo

Experience the app live here: [LLM Tokenizer](https://llmtokenizer.streamlit.app/)

## Features

- **Interactive Text Input:** Use a multi-line text area to input your text for tokenization.
- **Model Selection:** Choose from a wide range of popular LLM models for tokenization, including:
    - `gpt-3.5-turbo`
    - `gpt-4`
    - `text-embedding-ada-002`
    - `gpt-4o`
    - `gpt-4-turbo`
    - `claude-3-opus-20240229`
    - `claude-3-sonnet-20240229`
    - `claude-3-haiku-20240307`
    - `gemini-pro`
    - `llama-2-7b`
    - `mistral-7b`
- **Detailed Analysis:**
    - **Token Count:** See the total number of tokens generated.
    - **Character Count:** Get the total number of characters in your input text.
    - **Word Count:** View the total number of words in your input text.
    - **Token Details:** A comprehensive list of each token with its corresponding text and numerical ID.
- **Token Visualization:** The input text is displayed with each token highlighted in distinct colors, making it easy to visualize how the text is segmented.
- **Cost Estimation:** For OpenAI models, an estimated cost based on the input tokens is provided, helping users understand potential API usage expenses.
- **Copy to Clipboard:** Easily copy the entire list of token details to your clipboard with a dedicated button.
- **Reset Functionality:** A "Reset" button clears the text input and resets the model selection for a fresh start.
- **Robust Error Handling:** Informative error messages are displayed for unsupported models or other issues during tokenization.

## How to Run Locally

Follow these steps to set up and run the LLM Tokenizer app on your local machine:

### 1. Clone the Repository

```bash
gh repo clone PiyushKBhattacharyya/LLM-Tokenizer
cd LLM-Tokenizer
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

This command will open the application in your default web browser. If it doesn't open automatically, navigate to `http://localhost:8501` in your browser.

## Technologies Used

- [Streamlit](https://streamlit.io/) - For building the interactive web application.
- [Tiktoken](https://github.com/openai/tiktoken) - For fast BPE tokenization, used by OpenAI's models.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.
