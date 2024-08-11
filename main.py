import streamlit as stlt
import langchain_helper as lch

stlt.title("Purrfect Name Generator")

animal_type = stlt.sidebar.selectbox("What is your pet?", ("Dog", "Cat", "Cow", "Hamster", "Snake", "Lizard"))

pet_color = stlt.sidebar.text_area(
    label="What color is your "+ animal_type + "?",
    max_chars=15
)

with stlt.sidebar:
    openai_api_key = stlt.text_input("OpenAI API Key (We do not store)", key="langchain_search_api_key_openai", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View Source Code](https://github.com/RaYu1200/purrfect-names-generator)"

# openai_api_key=""

if pet_color:
    if not openai_api_key:
        stlt.info("Please add your OpenAI API key to continue.")
        stlt.stop()
    response = lch.generate_pet_name(animal_type, pet_color, openai_api_key)
    stlt.text(response['pet_name'])