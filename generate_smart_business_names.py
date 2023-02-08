import streamlit as st
import requests
import json
import pandas as pd
import os

url = "https://api.openai.com/v1/completions"


def generate_name(business_domain_industry):
    prompt = f"Please generate 10 business names with explanations for a company that is related to {business_domain_industry} industry. Make sure the business names are short, unique, and catchy, and the explanations provide insight into the thought process behind each name."
    payload = json.dumps({
        "model": "text-davinci-003",
        "prompt": prompt,
        "temperature": 0.9,
        "max_tokens": 1500,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0.6
    })
    OPENAPI_KEY = os.getenv('OPENAPI_KEY')

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAPI_KEY}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    business_names = json.loads(response.text)
    return business_names['choices'][0]['text']


def main():
    st.title("Smart Business Name Generator!")
    search_term = st.text_input("Enter your business industry")
    if search_term:
        with st.spinner('Wait for it...'):
            results = generate_name(search_term)
            st.write(results)
            st.success('Done!')


if __name__ == '__main__':
    main()
