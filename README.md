# PDFOllamaInterpreter
Takes in a PDF and extracts text from the document, then feeds it into any Ollama model, and can then ask the model questions about the text. Uses llama 3.1, but can be edited to use any model.

# Motivation for creating the script
ChatGPT and other online cloud models have limits on the size of a document you can upload, even with a paid subscription. I decided to run a model locally and extract the text through Python to bypass this restriction.

# How to use
Run using python3 pdfollamainterpreter.py *.pdf
