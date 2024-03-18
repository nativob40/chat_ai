# Chat AI:
This is a chatbot project that uses RAG to interact with documents located in a folder called **data** using LlamaIndex and OpenAI.


### Download files from the GitHub repository:
Create a folder where you want to download the files. Open a terminal in that location and run the following command:

    git clone https://github.com/nativob40/chat_ai.git


### Installation:
Run the following command to install the deployments:

    pip install -r requirements.txt

### Set your OpenAI API key:
LlamaIndex uses OpenAI’s gpt-3.5-turbo by default. Make sure your API key is available by setting it as an environment variable. 

In MacOS and Linux, this is the command:

    export OPENAI_API_KEY=XXXXX

and on Windows it is

    set OPENAI_API_KEY=XXXXX

### Execute the script:
Run the following command to run the script:

    python3 test_chat.py