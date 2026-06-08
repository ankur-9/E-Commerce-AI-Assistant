import streamlit as st
from router import router
from faq import ingest_faq_data,faq_chain
from sql import sql_chain
from pathlib import Path



faqs_path = Path(__file__).parent / "resources/faq_data.csv"
ingest_faq_data(faqs_path)

st.title("Ecommerce Bot")
query = st.chat_input("Write your query")

def ask(query):
    route = router(query).name
    if route=='faq':
        return faq_chain(query)
    elif route=='sql':
        return sql_chain(query)
    else:
        return f'Route {route} not implemented yet'


if 'messages' not in st.session_state:
    st.session_state['messages'] = []

for message in st.session_state['messages']:
    with st.chat_message(name=message['role']):
        st.write(message['content'])

if query:
    with st.chat_message(name='user'):
        st.write(query)
    st.session_state['messages'].append({'role':'user','content':query})

    response = ask(query)
    with st.chat_message(name='assistant'):
        st.write(response)
    st.session_state['messages'].append({'role':'assistant','content':response})