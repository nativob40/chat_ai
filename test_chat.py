from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from openai import AuthenticationError
import os
import time

# Set OpenAI API key
#os.environ['OPENAI_API_KEY']='MY_OPENAI_API_KEY' # Uncomment this line and enter your OPENAI_API_KEY if you do not have set the environment variable. THIS IS NOT RECOMMENDED IN "PRODUCTION"


def effect_gpt(response,prompt,o_system):
    """
    Generates a similar visual effect to ChatGPT but removes the conversation history from the screen.

    Args:
        response (str): Response received
        prompt (str): Query entered by user
        o_system (str): Your OS - 1=Linux/Mac, 2=Windows
    """
    try:
        response_list = [f'Prompt: {prompt}\n\n']

        for i in response.split(' '):
            os.system(o_system)
            response_list.append(i)
            print(' '.join(response_list))
            time.sleep(.08)
        return
    
    except Exception as err:
        print(f'ERROR in effect_gpt: {err}')

def set_config():

    try:
        # Set the command to clean the terminal when I choose the chat style "Without history"
        op=''
        while (True):
            print(f'\nType (1 or 2) to choose your OS:')
            op = input(f'  1 - Linux / Mac \n  2 - Windows \nOP: ')

            if op == '1':
                o_system = 'clear'
                os.system(o_system)
                break
            elif op == '2':
                o_system = 'cls'
                os.system(o_system)
                break
            else:
                print(f'\nERROR: Option not valid')

        # Style of conversation
        op=''
        while (op not in ['1','2']):
            print(f'Type (1 or 2) to choose the style of conversation:')
            op = input(f'  1 - With history \n  2 - Without history(Effect ChatGPT) \nOP: ')
            chat_style = op
            os.system(o_system)

        return chat_style, o_system

    except Exception as err:
        print(f'ERROR in set_config: {err}')


try:
    print('#### Welcome to ChatAI ####')

    chat_style, o_system = set_config()
    
    # Set the model
    llm = OpenAI(model="gpt-3.5-turbo-0125")
    # Load data and build an index
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # Configure chat engine
    chat_engine = index.as_chat_engine(chat_mode="context", llm=llm, verbose=True)

    while(True):

        print(f'\n>>> Type EXIT to finish <<<')
        prompt = input(f'\nEnter a prompt: ')

        if prompt.lower() != 'exit':
            response = chat_engine.chat(prompt)

            if chat_style == '1':
                print(f'\n{response.response}') # with history
            else:
                effect_gpt(response.response, prompt, o_system) # without history
        else:
            break

except AuthenticationError as err:
    print(f'\nERROR: {err.code}')

except Exception as err:
    print(f'\nERROR: {err}')

