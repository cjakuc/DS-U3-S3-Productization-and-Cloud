import basilica
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")
connection = basilica.Connection(API_KEY)

sentences = ["Hello world!", "How are you?"]
print(sentences)
embeddings = connection.embed_sentences(sentences)
print(list(embeddings)) # [[0.8556405305862427, ...], ...]