import streamlit as st
import requests
import json
import os

# URL for OpenAI API endpoint for completions
url = "https://api.openai.com/v1/completions"


def generate_name(business_domain_industry):
    prompt = f"Please generate 10 business names with explanations for a company that is related to {business_domain_industry} industry. Make sure the business names are short, unique, and catchy, and the explanations provide insight into the thought process behind each name."

    payload = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "temperature": 0.9,
        "max_tokens": 1500,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0.6
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.getenv("OPENAPI_KEY")}'
    }

    response = requests.post(url, headers=headers, json=payload)

    if not 200 <= response.status_code < 300:
        st.exception(f"HTTP error {response.status_code}. {response.text}")

    return response.json()['choices'][0]['text']


def prompt_name(prompt_text):
    payload = {
        "model": "text-davinci-003",
        "prompt": prompt_text,
        "temperature": 0.9,
        "max_tokens": 500,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0.6
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.getenv("OPENAPI_KEY")}'
    }

    response = requests.post(url, headers=headers, json=payload)

    if not 200 <= response.status_code < 300:
        st.exception(f"HTTP error {response.status_code}. {response.text}")

    return response.json()['choices'][0]['text']


def main():
    st.title("Open AI GPT-3 Prompter")

    genre = st.radio(
        "What do you want to use GPT-3 for?",
        ('Business Name Generation', 'Chat'))

    search_term = st.text_input("Enter your selection here")

    if genre == 'Business Name Gen':
        if search_term:
            with st.spinner('Generating names...'):
                results = generate_name(search_term)
                st.write(results)
                st.success("Done!")
    else:
        if search_term:
            with st.spinner('Getting chat response...'):
                results = prompt_name(search_term)
                st.write(results)
                st.success("Done!")


if __name__ == '__main__':
    main()
