import sys
import os
from pathlib import Path
from pypdf import PdfReader
from ollama import Client


if(len(sys.argv) == 1):
  print("No input file found")
  sys.exit()

file_path = os.path.abspath(sys.argv[1])

print(file_path)
# Define the directory path
pdf_path = Path(file_path)

#Full text from the PDF files
full_text = ""

try:
  reader = PdfReader(pdf_path)
        
  # Extract text from every page
  for page in reader.pages:
      full_text += page.extract_text() + "\n"
    
except Exception as e:
    print(f"Error reading {pdf_path.name}: {e}")


#This part is from Ollama docs to create a client and a messages
client = Client()

messages = [
  {
    'role': 'user',
    'content': full_text,
  },
]
#This the gives the model the ability to store responses and queries, gives it memory
full_response = ""

for part in client.chat('llama3.1', messages=messages, stream=True):
  content = part.message.content
  print(content, end='', flush=True)
  full_response += content
messages.append({'role': 'assistant', 'content': full_response})

#If the user has input, continue looping, otherwise stop looping and stop the model
hasquestion = True
while(hasquestion):
  user_input = input("\n\nWhat would you like to ask? ")
  if len(user_input) > 0:
    messages.append({'role': 'user', 'content': user_input})
    print("\n\n\033[1mUser Input\033[0m: " + user_input)
    for part in client.chat('llama3.1', messages=messages, stream=True):
      content = part.message.content
      print(content, end='', flush=True)
      full_response += content
    messages.append({'role': 'assistant', 'content': full_response})
  else:
    hasquestion = False