from langchain_community.document_loaders import PyPDFLoader

def pdf_loader(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    return docs


    