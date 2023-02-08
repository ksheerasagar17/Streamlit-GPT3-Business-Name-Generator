# This is a Streamlit Python script for a web application that generates business names and explanations for a company in a specified industry. The script uses the OpenAI API for generating the names and explanations.

# The generate_name function takes the user's specified business industry as input and sends a prompt to the OpenAI API. The function then sends an API request with specified parameters and an API key obtained from an environment variable. The response from the API is in JSON format and contains the generated business names and explanations.

# The main function is the main UI function for the application. It includes a text input for the user to enter the business industry, and if a value is entered, the results of the generate_name function are displayed with a loading spinner. If the script is executed as the main module, the main function is called.

import streamlit as st
import requests
import json
import pandas as pd
import os

# URL for OpenAI API endpoint for completions
url = "https://api.openai.com/v1/completions"

# Function to generate business names and explanations
def generate_name(business_domain_industry):
    # Prompt to be sent to the API
    prompt = f"Please generate 10 business names with explanations for a company that is related to {business_domain_industry} industry. Make sure the business names are short, unique, and catchy, and the explanations provide insight into the thought process behind each name."
    
    # Payload with API parameters
    payload = json.dumps({
        "model": "text-davinci-003",
        "prompt": prompt,
        "temperature": 0.9,
        "max_tokens": 1500,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0.6
    })
    
    # API Key obtained from environment variable
    OPENAPI_KEY = os.getenv('OPENAPI_KEY')
    
    # API request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAPI_KEY}'
    }
    
    # API request to generate business names and explanations
    response = requests.request("POST", url, headers=headers, data=payload)
    
    # Response from API as JSON
    business_names = json.loads(response.text)
    
    # Return the generated business names and explanations
    return business_names['choices'][0]['text']

# Main function for UI
def main():
    # Title of the application
    st.title("Smart Business Name Generator!")
    
    # Text input for business industry
    search_term = st.text_input("Enter your business industry")
    
    # If a value is entered in the text input
    if search_term:
        # Display a loading spinner
        with st.spinner('Hang tight! Our AI business name generator is busy coming up with the next big thing. In the meantime, try counting the number of times the loading icon spins. Bonus points if you can do it without losing your mind!'):
            # Get the generated business names and explanations
            results = generate_name(search_term)
            
            # Display the results
            st.write(results)
            
            # Display a success message
            st.success('Done!')

# Call the main function only if the file is executed as the main module
if __name__ == '__main__':
    main()
