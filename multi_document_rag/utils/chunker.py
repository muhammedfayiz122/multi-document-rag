from langchain_experimental.text_splitter import SemanticChunker


def doc_splitter(embeddings, docs):
    text_splitter = SemanticChunker(embeddings=embeddings)
    splitted_doc = text_splitter.split_documents(docs)
    return splitted_doc

