from langchain_experimental.text_splitter import SemanticChunker
from langchain_text_splitters import RecursiveCharacterTextSplitter
from multi_document_rag.logger.logger import logger

def semantic_doc_splitter(embeddings, docs):
    text_splitter = SemanticChunker(embeddings=embeddings)
    splitted_doc = text_splitter.split_documents(docs)
    return splitted_doc

def recursive_text_splitter(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
        separators=["\n\n", "\n", " ", ""],
        add_start_index=True,
        # embeddings=embeddings,
    )
    splitted_docs = text_splitter.split_documents(docs)
    logger.info(f"Split documents into {len(splitted_docs)} chunks.")
    return splitted_docs
