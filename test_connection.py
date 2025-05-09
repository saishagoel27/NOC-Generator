# Trying to connect to Azure OpenAI using Python
import openai

# Credentials for Azure OpenAI setup
api_key = "SqFPFd0NLxbblwsh2DPNsBzhHuXB1tQypKvSzpZHJ7hpVN4OI4wFJQQJ99BEACYeBjFXJ3w3AAABACOGsNls"  
azure_endpoint = "https://mishkatechopenai.openai.azure.com/"  

# Setting up the OpenAI API connection with Azure
openai.api_type = "azure"  
openai.api_key = "SqFPFd0NLxbblwsh2DPNsBzhHuXB1tQypKvSzpZHJ7hpVN4OI4wFJQQJ99BEACYeBjFXJ3w3AAABACOGsNls"  
openai.api_base = "https://mishkatechopenai.openai.azure.com/"  
openai.api_version = "2024-12-01-preview"

print("Testing if the Azure OpenAI connection works correctly")

try:
    
    chat_response = openai.ChatCompletion.create(
        engine="mishka-tech",  #deployment name
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},  
            {"role": "user", "content": "Hello! Can you understand me?"}  
        ]
    )

    
    print("Connection was established and here is the response:")
    print(chat_response['choices'][0]['message']['content'])  
except Exception as some_error:
    print("Something went wrong while connecting to Azure OpenAI:")
    print(some_error)
