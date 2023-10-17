## install packages : langchain, streamlit, openai    
## need openai api key

import streamlit as st
from langchain import llms, chains, prompts
from langchain.llms import OpenAI
import openai 

openai.api_key = "provide openai api key "
OPENAI_API_KEY="provide openai api key"


def translate(text_to_translate, provider, target_language):
    
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are a Translation assistant translate the user text into {target_language}."},
                     {"role": "user", "content": f"{text_to_translate}"}
                ],
                temperature=0,
                max_tokens=256
                )
    ans= response.get('choices')[0].get('message').get('content')
    return ans


def main():
    st.title("Translation App")

    text_to_translate = st.text_input("Enter text to translate")

    provider = st.selectbox("Select provider", ["Google", "Bing", "OpenAI"])

    target_language = st.selectbox("Select target language", ["Bhojpuri", "Dogri", "Haryanvi", "Marathi", "Marwari",, "Nimandi", "Malvi", "Dhakni", "Kinnauri", "Kangri", "Chambeali", "Garhwali", "Kumaoni", "Jaunsari", "Kannauji", "Brij Bhasha", "Bagdi", "Nimadi", "Bundeli", "Bagheli", "Awadhi", "Magahi", "Angika", "Nagpuri", "Khortha", "Kurmali", "Mundari", "Panch Pargania", "Chattisgarhi", "Surgujia", "Dhundhari", "Harauti", "Shekhawati", "Maithili", "Malvi"])

    translated_text= ""
    if st.button("Translate"):
        translated_text = translate(text_to_translate, provider, target_language)
        st.write(f"Translated Text: {translated_text}")
    
    if st.button("Translate New Text"):


        if 'conversation' not in st.session_state:
            st.session_state.conversation = []

        for original, translation in st.session_state.conversation:
           st.write(f"Original: {original}")
           st.write(f"Translated: {translation}")
           st.session_state.conversation.append((text_to_translate, translated_text))

    
if __name__ == "__main__":
    main()

## To run in terminal : "streamlit run indus.py"
