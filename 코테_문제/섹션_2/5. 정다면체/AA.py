from langchain_community.document_loaders import Docx2txtLoader

loader = Docx2txtLoader(file_path=f"C:\\dev2\\AI_Agent\\tax.docx")

from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=20)

document_list = loader.load_and_split(splitter)
