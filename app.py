import streamkit as sk

def app():
    sk.text_input("Enter text to tokenize:", key="text_input")
    sk.button("Tokenize", key="tokenize_button")

if __name__ == "__main__":
    sk.run(app)