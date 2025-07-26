from multi_document_rag.utils.pdf_loader import pdf_loader
from multi_document_rag.utils.chunker import recursive_text_splitter 
from multi_document_rag.utils.hugging_face_embeddings import load_embedding_model
from multi_document_rag.logger.logger import logger
from multi_document_rag.utils.vector_store import create_vector_store, add_documents_to_vector_store
from multi_document_rag.utils.paths import ROOT_DIR
import os

class DataIngestion():
    def __init__(self):
        pass

    def document_loader(self, pdf_path):
        docs = pdf_loader(pdf_path)
        return docs
    
    def document_splitter(self, docs):
        splitted_docs = recursive_text_splitter(docs)
        return splitted_docs
    
    def load_embeddings(self):
        embeddings = load_embedding_model()
        # embedded_docs = embeddings.embed_documents(splitted_docs)
        return embeddings
    
    def vector_store(self, embeddings):
        vector_store = create_vector_store(embeddings)
        # add_documents_to_vector_store(vector_store, embeddings)
        return vector_store
    
    def run(self, pdf_path):
        """
        Main method to run the data ingestion pipeline.
        Args:
            pdf_path (str): Path to the PDF document.
        Returns:
            vector_store: The created vector store with embedded documents.
        """
        file_name = pdf_path.split(sep='\\')[-1] if '\\' in pdf_path else pdf_path.split(sep='/')[-1]
        logger.info("Starting data ingestion process on PDF: " + file_name)
        docs = self.document_loader(pdf_path)
        splitted_docs = self.document_splitter(docs)
        embeddings = self.load_embeddings()
        vector_store = self.vector_store(embeddings)
        return vector_store
        
if __name__ == "__main__":
    pdf_path = os.path.join(ROOT_DIR, "data", "sample.pdf")  # Replace with your PDF path
    data_ingestion = DataIngestion()
    vector_store = data_ingestion.run(pdf_path)
    logger.info("Data ingestion process completed successfully.")
    