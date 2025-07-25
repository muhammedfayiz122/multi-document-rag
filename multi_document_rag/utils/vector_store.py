from langchain_milvus import Milvus
from multi_document_rag.logger.logger import logger
from multi_document_rag.exception.custom_exception import CustomException
import sys

def create_vector_store(embeddings):
    """
    Create a vector store using Milvus with the provided embeddings.
    Args:
        embeddings: The embedding model to be used for the vector store.
    Returns:
        Milvus vector store instance.
    Raises:
        CustomException: If there is an error while creating the vector store.
    """    
    try:
        vector_store = Milvus(
            collection_name="multi_document_rag",
            embedding_function=embeddings,
            connection_args={
                "host": "milvus",
                "port": "19530"
            },
            index_params={
                "index_type": "IVF_FLAT",
                "metric_type": "COSINE",
                "params": {
                    "nlist": 100
                }
            }
        )
        logger.info("Vector store created successfully.")
        return vector_store
    except Exception as e:
        logger.error(f"Error creating vector store: {e}")
        raise CustomException(e)

def add_documents_to_vector_store(vector_store, documents):
    """
    Add documents to the vector store.
    Args:
        vector_store: The Milvus vector store instance.
        documents: List of documents to be added.
    Returns:
        None
    Raises:
        CustomException: If there is an error while adding documents.
    """
    # try:
    #     vector_store.add_documents(documents)
    #     logger.info("Documents added to vector store successfully.")
    # except Exception as e:
    #     logger.error(f"Error adding documents to vector store: {e}")
    #     raise CustomException(e)
    try:
        vector_store.add_documents(documents)
        logger.info("Documents added to vector store successfully.")
    except Exception as e:
        logger.error(f"Error adding documents to vector store: {e}")
        raise CustomException(e)