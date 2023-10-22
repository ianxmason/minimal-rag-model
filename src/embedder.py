"""
Embeds documents to a VectorDB with OpenAI API
"""
import chromadb
import nltk
from nltk.corpus import reuters
from utils import get_embedding_function


def main(nltk_download=False):
    if nltk_download:
        nltk.download('reuters')
        nltk.download('punkt')
   
    reuters_subset = reuters.fileids()[0:100]
    reuters_subset = [id for id in reuters_subset if len(reuters.words(id)) < 500]
    
    client = chromadb.PersistentClient(path="../chromadb/test_db")
    # client.delete_collection("reuters_collection")  # To reset the collection if needed
    collection = client.create_collection(name="reuters_collection", embedding_function=get_embedding_function())

    for i, file_id in enumerate(reuters_subset):
        collection.add(
            documents=[reuters.raw(file_id)],
            metadatas=[{"nltk_file_id": file_id}],
            ids=[str(i)]
        )
    print(collection.peek())  # To see the first documents in the collection

    
if __name__ == "__main__":
    main()

