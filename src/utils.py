"""
Utility functions for the project.
"""
import os
import json
import openai
from chromadb.utils import embedding_functions


def get_openai_key():
    credentials_path = "../misc/credentials.json"
    with open(credentials_path, "r") as f:
        credentials = json.load(f)
    return credentials["openai_api"]["api_key"]


def set_openai_key():
    openai.api_key = get_openai_key()


def get_embedding_function():
    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                    api_key=get_openai_key(),
                    model_name="text-embedding-ada-002"
                )
    return openai_ef


def embed_text(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response['data'][0]['embedding']

