from langchain_community.document_loaders import PyPDFLoader
from multi_document_rag.logger.logger import logger
from multi_document_rag.exception.custom_exception import CustomException

def pdf_loader(pdf_path):
    try:
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()
        logger.info(f"Loaded {len(docs)} documents from {pdf_path}.")
        return docs
    except Exception as e:
        logger.error(f"Error loading PDF document: {e}")
        raise CustomException(f"Failed to load PDF document from {pdf_path}: {e}")


    