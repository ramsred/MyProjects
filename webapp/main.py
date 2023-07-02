from transformers import pipeline
from fastapi import FastApi, Response
from pydantic import BaseModel

generator = pipeline("text-generation", model='gpt3')

app = FastApi()

class Body(BaseModel):
    text:str


@app.get('/')
def root():
    return Response("</h1> self-documenting API to interact with a GPT model and generate text</h1>")



@app.post('/generate')
def predict(body:Body):
    results = generator(body.text, max_length=35, num_return_sequences=1)
    return results[0]