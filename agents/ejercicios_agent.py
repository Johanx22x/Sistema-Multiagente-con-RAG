import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama

def get_ejercicios_agent():
    prompt = PromptTemplate(
        input_variables=["tema"],
        template="Crea un ejercicio práctico sobre {tema}, incluyendo la solución paso a paso."
    )
    llm = ChatOllama(model="mistral")
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain
