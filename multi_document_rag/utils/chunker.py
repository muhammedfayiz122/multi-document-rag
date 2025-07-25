from langchain_experimental.text_splitter import SemanticChunker
from multi_document_rag.utils.load_embeddings import load_embedding_model

def doc_splitter(docs):
    embeddings = load_embedding_model()
    text_splitter = SemanticChunker(embeddings=embeddings)
    splitted_doc = text_splitter.split_documents(docs)
    return splitted_doc

