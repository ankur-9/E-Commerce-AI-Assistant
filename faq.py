import pandas as pd
from pathlib import Path
import chromadb
from IPython.core.debugger import prompt
from chromadb.utils import embedding_functions
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv() # will load both GROQ_API_KEY and GROQ_MODEL in the environment

# import os
# os.environ["GROQ_API_KEY"] --> will give GROQ_API_KEY value stored in .env file
# os.environ["GROQ_MODEL"] --> will give GROQ_MODEL value stored in .env file


faqs_path = Path(__file__).parent / "resources/faq_data.csv"
chroma_client = chromadb.Client()
collection_name_faq = "faqs"
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)
groq_client = Groq()

def ingest_faq_data(path):
    '''
    # store questions as embeddings in chromadb and answers as metadatas
    :param path:
    :return:
    '''
    if collection_name_faq not in [c.name for c in chroma_client.list_collections()]:
        print('Ingesting FAQs data into ChromaDB...')
        collection = chroma_client.get_or_create_collection(
            name=collection_name_faq,
        embedding_function=ef
        )
        df = pd.read_csv(path)
        docs = df['question'].to_list()
        metadata = [{'answer':i} for i in df['answer'].to_list()] #metadata is a list of dictionaries or json objects
        # [{'answer': 'You can return products within 30 days of delivery.'}, {'answer': 'Yes, HDFC credit card users get a 10% discount on select items.'},....]
        ids = [f'id_{i}' for i in range(len(df))]

        collection.add(
            documents=docs,
            ids = ids,
            metadatas = metadata
        )
        print(f'FAQs Data successfully ingested into collection : {collection_name_faq}')

    else:
        print(f'Collection {collection_name_faq} already exists!')



def get_relevant_qa(query):
    '''
    This functions will fetch relevant QnA from chromadb based on your query.
    :param query:
    :return:
    '''
    collection = chroma_client.get_or_create_collection(name=collection_name_faq)
    results = collection.query(
        query_texts=[query],
        n_results=2
    )
    return results

#===================LLM part======================

def faq_chain(query):
    '''
    This functions will generate context from chromadb results.
    :param query:
    :return:
    '''
    response = get_relevant_qa(query)
    context = ''.join([r.get('answer') for r in response['metadatas'][0]])
    answer = generate_answer(query,context)
    return answer


def generate_answer(query,context):
    '''
    This function will create a prompt using the response from chromadb and will call llm to generate a coherent answer.
    :param query:
    :param context:
    :return:
    '''
    prompt = f'''
    Answer the question based only on the following context.
    If you don't know the answer, just say you don't know.
    Do not make things up.
    
    Context:
    {context}
    
    Question: {query}
    '''

    #call LLM
    chat_completion = groq_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=os.environ["GROQ_MODEL"]
    )

    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    ingest_faq_data(faqs_path)
    query = "What's your policy on defective products?"
    answer = faq_chain(query)
    print(answer)


"""
Ingesting FAQs data into ChromaDB...
FAQs Data successfully ingested into collection : faqs
For defective products, you can contact our support team within 48 hours for a replacement or refund. Additionally, you can return products within 30 days of delivery.
"""





# {'ids': [['id_8', 'id_0']], 'embeddings': None, 'documents': [['What should I do if I receive a damaged product?', 'What is the return policy of the products?']], 'uris': None, 'included': ['metadatas', 'documents', 'distances'], 'data': None, 'metadatas': [[{'answer': 'Contact our support team within 48 hours for a replacement or refund.'}, {'answer': 'You can return products within 30 days of delivery.'}]], 'distances': [[0.3872276544570923, 0.4744042158126831]]}

"""
{'ids': [['id_8', 'id_0']],
 'embeddings': None,
 'documents': [['What should I do if I receive a damaged product?',
   'What is the return policy of the products?']],
 'uris': None,
 'included': ['metadatas', 'documents', 'distances'],
 'data': None,
 'metadatas': [[{'answer': 'Contact our support team within 48 hours for a replacement or refund.'},
   {'answer': 'You can return products within 30 days of delivery.'}]],
 'distances': [[0.3872276544570923, 0.4744042158126831]]}
"""
# ''.join([ans['answer'] for ans in response['metadatas'][0]])
# 'Contact our support team within 48 hours for a replacement or refund.You can return products within 30 days of delivery.'