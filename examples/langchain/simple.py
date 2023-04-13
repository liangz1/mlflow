import os
import mlflow

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

from langchain.chains import LLMChain
chain = LLMChain(llm=llm, prompt=prompt)



with mlflow.start_run():
    logged_model = mlflow.langchain.log_model(chain, "langchain_model")

loaded_model = mlflow.pyfunc.load_model(logged_model.model_uri)
print(loaded_model.predict([{"product": "colorful socks"}]))
