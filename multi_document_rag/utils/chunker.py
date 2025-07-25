from langchain_text_splitters import RecursiveCharacterTextSplitter
from multi_document_rag.logger.logger import logger
from multi_document_rag.exception.custom_exception import CustomException

def recursive_text_splitter(docs):
    try:
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
    except Exception as e:
        raise CustomException(e, custom_msg="Failed to split documents")
