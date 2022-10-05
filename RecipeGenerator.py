from gettext import install;
import os
from pydoc import tempfilepager;
import openai;

def GPT3(Text):
    openai.api_key = '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'
    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=Text,
            temperature=0.1,
            max_tokens=252,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0  
    )
    content = response.choices[0].text.split('.')
    print(content)
    return response.choices[0].text

query = "What is a recipe for cake that serves 4 people?"
response = GPT3(query)
print(response)
