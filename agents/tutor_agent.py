import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama

def get_tutor_agent():
    prompt = PromptTemplate(
        input_variables=["concepto"],
        template="Explica de forma clara y sencilla el siguiente concepto de Álgebra Lineal: {concepto}"
    )
    llm = ChatOllama(model="mistral")
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain
