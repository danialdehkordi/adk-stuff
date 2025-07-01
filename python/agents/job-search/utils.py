import os

def get_openai_api_key():
    # Try to get the API key from an environment variable first
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("OpenAI API key loaded from environment variable.")
        return api_key
    else:
        # Fallback: prompt the user for the key (less secure for production)
        # In a real application, avoid hardcoding or prompting like this.
        print("OPENAI_API_KEY environment variable not found.")
        api_key = input("Please enter your OpenAI API Key: ")
        return api_key

def get_serper_api_key():
    # Try to get the API key from an environment variable first
    api_key = os.getenv("SERPER_API_KEY")
    if api_key:
        print("Serper API key loaded from environment variable.")
        return api_key
    else:
        # Fallback: prompt the user for the key (less secure for production)
        # In a real application, avoid hardcoding or prompting like this.
        print("SERPER_API_KEY environment variable not found.")
        api_key = input("Please enter your Serper API Key: ")
        return api_key    