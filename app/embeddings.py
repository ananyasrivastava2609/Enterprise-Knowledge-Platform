import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("sk-pr0rE8zQoIA"))


def get_embeddings(chunks):
    """
    Convert text chunks into embeddings.
    """
    embeddings = []

    for chunk in chunks:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunk
        )
        embeddings.append(response.data[0].embedding)

    return embeddings
