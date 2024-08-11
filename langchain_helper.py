from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

def generate_pet_name(animal_type, pet_color, openai_api_key):
    llm = OpenAI(temperature = 0.5, openai_api_key=openai_api_key)

    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have a pet {animal_type} and it is {pet_color} in color, suggest me five cool names for my pet."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="pet_name")

    response = name_chain({
        'animal_type': animal_type,
        'pet_color': pet_color
    })
    
    return response
