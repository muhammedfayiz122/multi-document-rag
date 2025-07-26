from langchain_huggingface import HuggingFaceEmbeddings
from multi_document_rag.logger.logger import logger
from multi_document_rag.exception.custom_exception import CustomException
import time

def load_embedding_model():
    try:
        start_time = time.time()
        logger.info("Loading HuggingFace embedding model...")
        embedding = HuggingFaceEmbeddings(
            model_name="intfloat/e5-base-v2",
            encode_kwargs={
                'normalize_embeddings': True,
                'convert_to_tensor': True
                } 
        )
        end_time = time.time()
        logger.info(f"Embedding model loaded in {end_time - start_time:.2f} seconds.")
        return embedding
    except Exception as e:
        raise CustomException(e, custom_msg="Failed to load HuggingFace embedding model")

"""
Hugging Face embedding models :  
-> e5-large-v2
-> intfloat/e5-base-v2
-> intfloat/e5-small-v2
-> bge-base-en
-> all-MiniLM-L6-v2
"""
    
