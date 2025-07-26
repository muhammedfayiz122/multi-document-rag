from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from multi_document_rag.logger.logger import logger
from multi_document_rag.exception.custom_exception import CustomException


def pdf_loader(pdf_path: str) -> list[Document]:
    """Load a PDF document from the specified path."""
    try:
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()
        file_name = pdf_path.split(sep='\\')[-1] if '\\' in pdf_path else pdf_path.split(sep='/')[-1]
        logger.info(f"Loaded {len(docs)} documents from {file_name}.")
        return docs
    except Exception as e:
        raise CustomException(e, custom_msg=f"Failed to load PDF document from {pdf_path}")


    